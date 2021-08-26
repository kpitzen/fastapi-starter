import models
from sqlalchemy.orm import Session


def get_all_users(pg: Session):
    return pg.query(models.User).all()
