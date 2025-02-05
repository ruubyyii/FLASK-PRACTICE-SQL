class Config():
    SECRET_KEY = '8a300460aa9a13bdf8cd9fc531cef4a4d00c19ca02b09310db4c7686e0a7d236'

class DevelopmentConfig(Config):

    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'flask_practice_sql'

class ProductionConfig(Config):

    DEBUG = False
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'flask_practice_sql'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}