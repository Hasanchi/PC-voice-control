
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix='voice'
    )

    api_key: SecretStr
    secret_key: SecretStr
    bucket: str



