import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    STORMY_QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/quotes.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kasparov:ian@2304@localhost/blog'


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