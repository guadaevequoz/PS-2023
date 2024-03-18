from os import getenv
from dotenv import load_dotenv


class Config(object):
    """
    Configuración base
    """


class DevelopmentConfig(Config):
    """
    Configuracion de development.
    """


class ProductionConfig(Config):
    """
    Configuracion de produccion
    """


# config = {"development": DevelopmentConfig}
config = {"production": ProductionConfig}
