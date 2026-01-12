from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mongodb_uri:str
    mongodb_db_name: str = "url_shortener"
    url_collection:str='urls'
    base_url: str = "http://localhost:8000"
    

    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)


settings = Settings()