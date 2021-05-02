import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kasparov:ian@2304@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    

class TestConfig(Config):
    pass
    

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}