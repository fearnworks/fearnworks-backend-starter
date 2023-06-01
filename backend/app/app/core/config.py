"""
This module manages the settings for the application, such as API version, JWT secret,
algorithm, CORS origins, and SQLAlchemy database URI.
"""
from loguru import logger
import logging
import pathlib
import sys

from dotenv import load_dotenv, find_dotenv
from app.core.logging import InterceptHandler
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, Field, validator
from typing import List, Optional, Union

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Defines the project root directory
ROOT = pathlib.Path(__file__).resolve().parent.parent


class DBSettings(BaseSettings):
    # SQLAlchemy database URI
    SQLALCHEMY_DATABASE_URI: str
    # Superuser credentials
    FIRST_SUPERUSER: EmailStr
    FIRST_SUPERUSER_PW: str

class LoggingSettings(BaseSettings):
    LOGGING_LEVEL: int = logging.INFO  # logging levels are ints
    
class AuthSettings(BaseSettings):
    LOGGING_LEVEL: int = logging.INFO  # logging levels are ints
    # Secret key for JWT generation and verification
    JWT_SECRET: str
    # Algorithm to be used for JWT encoding and decoding
    ALGORITHM: str = Field(..., env="JWT_ALGORITHM")
    # Expiry time for the access token in minutes (60 min/hr * 24 hr/day * 8 days = 8 days)
    ACCESS_TOKEN_EXPIRE_MINUTES: int


class Settings(BaseSettings):
    """
    Settings model that parses and validates the environment variables.
    """

    # API version
    API_V1_STR: str = "/api/v1"



    # List of origins for CORS (Cross-Origin Resource Sharing)
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    # Origins that match this regex OR are in the above list are allowed
    BACKEND_CORS_ORIGIN_REGEX: Optional[str]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        """
        A validator for the CORS origins to ensure that they are in the correct format.

        Args:
            v (Union[str, List[str]]): The CORS origins, either as a string or a list of strings.

        Returns:
            Union[List[str], str]: The validated CORS origins.
        """
        if isinstance(v, str):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, list):
            return v
        raise ValueError(v)

    db: DBSettings = DBSettings()
    logging: LoggingSettings = LoggingSettings()
    auth: AuthSettings = AuthSettings()

    class Config:
        case_sensitive = True

def setup_app_logging(config: Settings) -> None:
    """Prepare custom logging for our application."""
    LOGGERS = ("uvicorn.asgi", "uvicorn.access")
    logging.getLogger().handlers = [InterceptHandler()]
    for logger_name in LOGGERS:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler(level=config.logging.LOGGING_LEVEL)]

    logger.configure(
        handlers=[{"sink": sys.stderr, "level": config.logging.LOGGING_LEVEL}]
    )

# Instantiate the settings
settings = Settings()