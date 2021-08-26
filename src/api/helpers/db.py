import os
from sqlalchemy.engine.url import URL


def get_url():
    env_config = {
        "drivername": "postgresql+psycopg2",
        "username": os.getenv("POSTGRES_USERNAME"),
        "password": os.getenv("POSTGRES_PASSWORD"),
        "host": os.getenv("POSTGRES_HOST"),
        "port": os.getenv("POSTGRES_PORT"),
        "database": os.getenv("POSTGRES_DATABASE"),
    }

    url = URL(**env_config)

    return str(url)
