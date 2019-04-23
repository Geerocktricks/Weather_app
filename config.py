import os
class Config:
    WEATHER_API_BASE_URL='http://api.openweathermap.org/data/2.5/weather?appid={}&q={}'
    WEATHER_API_KEY=os.environ.get('WEATHER_API_key')
    SECRET_KEY=os.environ.get('SECRET_KEY')
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG=True

config_options = {
    'production':ProdConfig,
    'development':DevConfig
}