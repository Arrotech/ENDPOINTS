import os

class Config():
    DEBUG=False
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_HOST = os.getenv('DB_HOST')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    SECRET_KEY = os.getenv('SECRET_KEY')

class DevelopmentConfig(Config):
    """Allow debug to restart after changes."""
    DEBUG = True
    DATA_BASE_URL=os.getenv("DATABASE_URL")

class TestingConfig(Config):
    """Testing the application."""
    TESTING = True
    DEBUG = True
    DATABASE_URL=os.getenv("TEST_DATABASE_URL")

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True
    
class ReleaseConfig(Config):
    """Releasing app configurations"""
    DEBUG = False
    TESTING = False

app_config={
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'Staging': StagingConfig,
    'release': ReleaseConfig,
}