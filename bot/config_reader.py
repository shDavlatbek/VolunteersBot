from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: SecretStr
    redis_url: str
    
    allowed_hosts: list[str]
    debug: bool
    django_db_engine: SecretStr
    django_db_name: SecretStr
    django_db_user: SecretStr
    django_db_password: SecretStr
    django_db_port: SecretStr
    django_db_host: SecretStr
    
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


config = Settings()
