from sqlalchemy.orm import declarative_base

ModelBase = declarative_base()


class Base(ModelBase):
    __abstract__ = True
