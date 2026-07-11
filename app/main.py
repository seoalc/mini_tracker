from fastapi import FastAPI
from app.routers import home_router

app = FastAPI()
app.include_router(home_router.router)