from fastapi import APIRouter, Request, Depends, HTTPException, status,Form
from fastapi.responses import RedirectResponse, HTMLResponse

from fastapi.templating import Jinja2Templates

from schemas.url_schema import URLCreate,URLPublic
from service.url_service import UrlService
templates = Jinja2Templates(directory="templates")
url_service=UrlService()

url_router=APIRouter(prefix='',tags=['urls'])

@url_router.post('/shorten',response_model=URLPublic)
async def creat_short_url(
    req: Request,
    original_url: str = Form(...)
):
    if not original_url.startswith(("http://", "https://")):
        original_url = "https://" + original_url  
    base_url=str(req.base_url).rstrip('/')
    data = URLCreate(original_url=original_url)

    result=await url_service.create_short_url(data,base_url=base_url)
    return templates.TemplateResponse(
            "success.html",
            {
                "request": req,
                "short_url": result.short_url,
                "original_url": result.original_url,
                "created_at": result.created_at,
                "clicks": result.clicks
            }
        )

@url_router.get('/{short_code}',response_class=RedirectResponse)
async def redirect_to_original(short_code:str,request:Request):
    url_doc=await url_service.get_url_by_short_code(short_code)
    if not url_doc:
        return templates.TemplateResponse(
            "404.html",
            {
                "request": request
            },
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    await url_service.record_click(short_code)

    return RedirectResponse(
        url=url_doc.original_url,
        status_code=status.HTTP_307_TEMPORARY_REDIRECT
    )
