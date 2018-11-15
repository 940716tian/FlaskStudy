from redis import StrictRedis

def get_db_uri(conf):
    uri = "{backend}+{engine}://{user}:{pw}@{ip}:{port}/{db}".format(
        backend=conf.get('backend'),
        engine=conf.get('engine'),
        user=conf.get('user'),
        pw=conf.get('pw'),
        ip=conf.get('host'),
        port=conf.get('port'),
        db=conf.get('db')
    )
    print(uri)
    return uri

CACHES = {
    "default":{'CACHE_TYPE':'redis',
            'CACHE_REDIS_URL':'redis://127.0.0.1:6379/7'},
    "debug":{'CACHE_TYPE':'redis',
            'CACHE_REDIS_URL':'redis://127.0.0.1:6379/7'},
}

class Config:
    # 公共配置
    Debug = False,
    Test = False,
    Online = False,
    SECRET_KEY = 'asdfghjkl;zxcvbn',
    SESSION_TYPE = 'redis',
    SESSION_KEY_PREFIX = 'myapp:',
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DebugConfig(Config):
    DEBUG = True,
    SESSION_REDIS = StrictRedis(host='127.0.0.1',db=5)
    # 数据库配置
    DATABASE = {
        "engine":"pymysql",
        "backend":"mysql",
        "user":"xiao_hu",
        "pw":123,
        "host":"127.0.0.1",
        "port":3306,
        "db":"hzfl04"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

class TestConfig(Config):
    Test = True,
    SESSION_REDIS = StrictRedis(host='127.0.0.1',db=6)
    # 数据库配置
    DATABASE = {
        "engine":"pymysql",
        "backfend":"mysql",
        "user":"xiao_hu",
        "pw":123,
        "host":"127.0.0.1",
        "port":3306,
        "db":"hzfl05"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

class OlineConfig(Config):
    Online = True,
    SESSION_REDIS = StrictRedis(host='127.0.0.1',db=7)
    # 数据库配置
    DATABASE = {
        "engine":"pymysql",
        "backfend":"mysql",
        "user":"xiao_hu",
        "pw":123,
        "host":"127.0.0.1",
        "port":3306,
        "db":"hzfl06"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

conf = {
    "debug":DebugConfig,
    "test":TestConfig,
    "online":OlineConfig
}