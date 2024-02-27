from pydantic import RedisDsn
from pydantic_settings import BaseSettings


class AppConfigSettings(BaseSettings):
    """应用配置"""

    """基础配置"""
    app_name: str = "FastAPI学习"
    app_host: str = "0.0.0.0"
    app_port: int = 8080
    app_env: str = "dev"
    app_debug: bool = False
    """jwt配置"""
    jwt_enable: bool = True
    jwt_secret_key: str = "12345789@98765431"
    jwt_algorithm: str = "HS256"
    jwt_expired: int = 30
    jwt_iss: str = "猿码记"
    jwt_no_check_uris: str = ""
    """数据库配置"""
    db_host: str | None = None
    db_port: int | None = None
    db_user: str | None = None
    db_password: str | None = None
    db_database: str | None = None
    """redis配置"""
    redis_dsn: RedisDsn | None = None
