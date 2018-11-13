from redis import StrictRedis

def get_db_uri(conf):
    uri = "{backend}+{engine}:///{user}:{pw}@{ip}:{port}/{db}".format(
        backend=conf.get('backend'),
        engine=conf.get('engine'),
        user=conf.get('user'),
        pw=conf.get('pw'),
        ip=conf.get('ip'),
        port=conf.get('port'),
        db=conf.get('db')
    )
    return uri

class Config:
    # 公共配置
    Debug = False,
    Test = False,
    Online = False,
    SECRET_KEY = 'qwertyuiop',
    SESSION_TYPE = 'redis',
    SESSION_KEY_PREFIX = 'myapp:',
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DebugConfig(Config):
    Debug = True,
    SESSION_REDIS = StrictRedis(host='127.0.0.1',db=5)
    # 数据库配置
    DATABASE = {
        "engine":"pymysql",
        "bacfend":"mysql",
        "user":"xiao_hu",
        "pw":123,
        "host":"127.0.0.1",
        "port":3306,
        "db":"hzfl02"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

class TestConfig(Config):
    Test = True,
    SESSION_REDIS = StrictRedis(host='127.0.0.1',db=6)
    # 数据库配置
    DATABASE = {
        "engine":"pymysql",
        "bacfend":"mysql",
        "user":"xiao_hu",
        "pw":123,
        "host":"127.0.0.1",
        "port":3306,
        "db":"hzfl03"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

class OlineConfig(Config):
    Online = True,
    SESSION_REDIS = StrictRedis(host='127.0.0.1',db=7)
    # 数据库配置
    DATABASE = {
        "engine":"pymysql",
        "bacfend":"mysql",
        "user":"xiao_hu",
        "pw":123,
        "host":"127.0.0.1",
        "port":3306,
        "db":"hzfl04"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

conf = {
    "debug":DebugConfig,
    "test":TestConfig,
    "online":OlineConfig
}