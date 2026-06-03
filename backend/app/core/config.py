from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Open Cashback"
    app_env: str = "development"
    app_debug: bool = True
    database_url: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/open_cashback"
    jwt_secret_key: str = "change_me"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 60
    cors_origins: str = "http://localhost:5173,http://localhost:3000"
    blockchain_enabled: bool = False
    blockchain_network: str = "ganache"
    blockchain_rpc_url: str = "http://127.0.0.1:8545"
    blockchain_contract_address: str | None = None
    cashback_default_rate: str = "0.01"
    cashback_default_expiration_days: int = 90

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
