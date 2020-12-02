# class Config:
#     '''
#     General configuration parent class
#     '''
#     MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/popular?api_key=0487fea15940e98dccf85967b8133d0f'



# class ProdConfig(Config):
#     '''
#     Production  configuration child class

#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''
#     pass


# class DevConfig(Config):
#     '''
#     Development  configuration child class

#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''

#     DEBUG = True
import os

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/popular?api_key=0487fea15940e98dccf85967b8133d0f'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/watchlist'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}