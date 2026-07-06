import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


class Config:
    """
    Base configuration for HawkEye.
    """

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "change-this-secret-key-before-production"
    )

    ENV = os.getenv("FLASK_ENV", "development")

    DEBUG = ENV == "development"

    TESTING = False

    TEMPLATES_AUTO_RELOAD = True

    JSON_SORT_KEYS = False

    MAX_CONTENT_LENGTH = 5 * 1024 * 1024

    SEND_FILE_MAX_AGE_DEFAULT = 0


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}