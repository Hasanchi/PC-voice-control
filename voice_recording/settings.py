
from pydantic import SecretStr, BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class S3Settings(BaseModel):
    api_key: SecretStr
    secret_key: SecretStr
    endpoint_url: SecretStr
    bucket: SecretStr


class LocalSettings(BaseModel):
    tmp_path: SecretStr


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_nested_delimiter='__',
        # env_prefix = 'PC_VOICE',
        case_sensitive=False
    )

    local: LocalSettings
    s3: S3Settings



