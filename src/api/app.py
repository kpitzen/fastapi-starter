from api.routers.users.views import users_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(users_router, prefix="/users")
