from fastapi import FastAPI
from app.routers import home_router, click_router
from app.database.connection import init_db

app = FastAPI()

init_db()

app.include_router(home_router.router)
app.include_router(click_router.router)