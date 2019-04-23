import os
class Config:
    pass
class ProdConfig(Config):
    pass
class DevConfig(config):
    DEBUG=True

config_options = {
    'production':ProdConfig,
    'development':DevConfig
}