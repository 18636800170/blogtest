import os


class DefaultConfig(object):
    DEBUG = True
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

    TYPE = "mysql+pymysql"
    USER = "root"
    PASSWORD = "root"
    HOST = "127.0.0.1"
    PORT = 3306
    DATABASENAME = "blogtest"
    SQLALCHEMY_DATABASE_URI = "{}://{}:{}@{}:{}/{}".format(TYPE, USER, PASSWORD, HOST, PORT, DATABASENAME)
    SQLALCHEMY_TRACK_MODIFICATION = False

    SQLALCHEMY_ECHO = True

    # LOG_DIR = os.path.join(BASE_DIR, "logs")
