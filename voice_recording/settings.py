
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='../.env',
    )

    api_key: SecretStr
    secret_key: SecretStr
    endpoint_url: str
    bucket: str



