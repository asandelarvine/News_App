class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://api.thenewsdb.org/3/news/{}?api_key={}'

class Config:
    '''
    General configuration parent class
    '''
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True