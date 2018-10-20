import os

class Config:
    SECRET_KEY=os.environ.get("SECRET_KEY")
    UPLOADED_PHOTOS_DEST='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS=True

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    #simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_JS_CDN = True

class TestConfig(Config):
    pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joe:killshot18@localhost/blog'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'testconfig':TestConfig
}
