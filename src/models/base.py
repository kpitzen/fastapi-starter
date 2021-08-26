from sqlalchemy.ext.declarative import declarative_base

ModelBase = declarative_base()


class Base(ModelBase):  # type: ignore
    __abstract__ = True
