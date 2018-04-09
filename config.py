import os #importatnt to acess the application keys which should be reference somewhere else
    #data structure
class Config:
     NEWS_ARTICLE_BASE_URL= "https://newsapi.org/v2/everything?q=bitcoin&apiKey=a90264f52639408089753bdeca75f6b8"
     NEWS_SOURCE_BASE_URL="https://newsapi.org/v2/sources?apiKey=a90264f52639408089753bdeca75f6b8"
     NEWS_API_KEY="a90264f52639408089753bdeca75f6b8"
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig ,
    'production' : ProdConfig
}