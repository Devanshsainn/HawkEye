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

    DEBUG = False
    TESTING = False

    JSON_SORT_KEYS = False

    TEMPLATES_AUTO_RELOAD = True

    REPORTS_DIR = BASE_DIR / "reports"

    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False