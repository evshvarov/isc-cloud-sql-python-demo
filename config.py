import os


class Config:
    DEBUG = False
    DEVELOPMENT = False
    SECRET_KEY = os.getenv("SECRET_KEY", "this-is-the-default-key")
    HOST=os.getenv("HOST","hostserver")
    IRIS_USERNAME = os.getenv("IRIS_USERNAME","login")
    IRIS_PASSWORD = os.getenv("IRIS_PASSWORD","pass")


class ProductionConfig(Config):
    pass


class StagingConfig(Config):
    DEBUG = True


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
