import os #importatnt to acess the application keys which should be reference somewhere else
    #data structure
class Config:
     NEWS_A_BASE_URL= "https://newsapi.org/v2/everything?q={}&apiKey={}"
     NEWS_S_BASE_URL="https://newsapi.org/v2/sources?apiKey={}"
     NEWS_API_KEY="a90264f52639408089753bdeca75f6b8"
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig ,
    'production' : ProdConfig
}