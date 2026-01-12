from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from routes.url_routes import url_router
from service.logger_serivce import LoggerService
# from app.database import connect_to_mongo, close_mongo_connection
# from app.routers import url_router
logger_service=LoggerService(nameLogger=__name__)
app = FastAPI(title="Mini URL Shortener")

# Templates & static
app.mount("/static", StaticFiles(directory="templates/static"), name="static")
templates = Jinja2Templates(directory="templates")
# CORS middleware (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Include our routes
app.include_router(url_router)


# @app.on_event("startup")
# async def startup_event():
#     await connect_to_mongo()


# @app.on_event("shutdown")
# async def shutdown_event():
#     await close_mongo_connection()


# Optional: nice root endpoint
# @app.get("/")
# async def root(request: Request):
#     return templates.TemplateResponse(
#         "index.html",
#         {"request": request, "base_url": request.base_url}
#     )
@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )
if __name__=='__main__':
    import uvicorn
    logger_service.info('🎯🚀App is running on port 8000!')
    uvicorn.run(app)
    