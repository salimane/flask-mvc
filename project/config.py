import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    if not SECRET_KEY:
        raise ValueError("SECRET_KEY environment variable is not set")

    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class DevelopmentConfig(Config):
    DEBUG = True
    DEBUG_TB_ENABLED = True


class TestingConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY", "test-secret-key-not-for-production")
    TESTING = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = False


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
