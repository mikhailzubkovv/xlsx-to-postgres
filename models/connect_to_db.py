from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import configparser
import os


def create_config(path):
    """
    Create a config file
    """
    config = configparser.ConfigParser()
    config.add_section('Config')
    config.set('Config', 'username', 'None')
    config.set('Config', 'password', 'None')
    config.set('Config', 'host', '127.0.0.1')
    config.set('Config', 'port', '5432')
    config.set('Config', 'database', 'None')

    with open(path, "w") as config_file:
        config.write(config_file)


def change_config(username, password, host, port, database):
    config = configparser.ConfigParser()
    config.read(filenames='config.ini', encoding='utf-8')
    config.set('Config', 'username', username)
    config.set('Config', 'password', password)
    config.set('Config', 'host', host)
    config.set('Config', 'port', port)
    config.set('Config', 'database', database)

    with open('config.ini', 'w') as new_config:
        config.write(new_config)


def read_config(path='config.ini'):
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(filenames=path, encoding='utf-8')
    username = config['Config']['username']
    password = config['Config']['password']
    host = config['Config']['host']
    port = config['Config']['port']
    database = config['Config']['database']

    return username, password, host, port, database


Base = declarative_base()


def connect_db():
    username, password, host, port, database = read_config()
    engine = create_engine(f'postgresql+psycopg://{username}:{password}@{host}:{port}/{database}')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    return Session()


if __name__ == '__main__':
    connect_db()


