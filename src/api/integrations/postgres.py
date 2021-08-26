from api.helpers.db import get_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_session():
    engine = create_engine(get_url())
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return session


def get_db():
    session = get_session()
    db = session()
    try:
        yield db
    finally:
        db.close()
