from api.integrations.postgres import get_db
from api.routers.users.actions import get_all_users
from api.schemas import User
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter

users_router = APIRouter(tags=["users"], responses={404: {"description": "Not Found"}})

@users_router.get("/", response_model=List[User])
async def get_users(pg: Session = Depends(get_db)):
    users = get_all_users(pg)
    return users
