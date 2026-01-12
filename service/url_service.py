from database import DataBase
from models.url_model import URLDocument
from schemas.url_schema import URLCreate, URLPublic
from shortuuid import uuid
from datetime import datetime
from fastapi import HTTPException
from .logger_serivce import LoggerService
from typing import Optional
from config import settings
database=DataBase()
logger_service=LoggerService(nameLogger=__name__)

# COLLECTION_NAME = "urls"

class UrlService:

    def __init__(self):
        self.collection=database.get_collection(settings.url_collection)
        self.collection.create_index('short_code',expireAfterSeconds=120)

    async def generate_unique_short_code(self,length: int = 6) -> str:
        """
        Generate short code and make sure it's unique
        use shortuuid, uuid, or custom base62
        """
        short_code=uuid()[:length]
        

        return short_code

    async def create_short_url(self,data: URLCreate, base_url: str) -> URLPublic:
        """
        Main function to create new short link
        Steps:
        1. Generate unique short code
        2. Create document
        3. Save to MongoDB
        4. Return public response with full short url
        """
       

     
      
        short_code=await self.generate_unique_short_code()
        url_document=URLDocument(
            original_url=str(data.original_url),
            short_code=short_code,
            last_clicked=datetime.now()

        )
        logger_service.info(f'🎯🚀 Creat short url:{str(data.original_url)} --> short code :{short_code}')

        self.collection.insert_one(url_document.model_dump(by_alias=True))
        return URLPublic(
            short_url=f'{base_url.rstrip('/')}/{short_code}',
            original_url=str(data.original_url),
            short_code=short_code,
            created_at=datetime.now()
        )

                
      
    async def get_url_by_short_code(self,short_code: str) -> Optional[URLDocument]:
        """
        Find original url by short code
        Return None if not found
        """
        # ---------------- YOUR CODE HERE ----------------
        url=self.collection.find_one({
            'short_code':short_code
        },{'_id':0})
        if not url:
            return None
        logger_service.info(f'🚀🚀 Short code {short_code} match url {url}')
        return URLDocument(**url)


    async def record_click(self,short_code: str) -> bool:
        """
        Increase click counter + update last_clicked time
        Return True if success, False if url not found
        """
        # ---------------- YOUR CODE HERE ----------------
        if self.collection.find_one({
            'short_code':short_code
        }):
           self.collection.find_one_and_update(
               {'short_code':short_code},
               {    '$inc': {'clicks':1},
                   '$set':{'last_clicked':datetime.now()}

               }
           )
           return True
        
        return False