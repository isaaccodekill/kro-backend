from fastapi import FastAPI
from app.controllers import user, auth
from app.database import create_tables

app = FastAPI()

# on start up, create the tables
@app.on_event("startup")
async def on_startup():
    # create_tables()
    create_tables()

app.include_router(user.router, prefix="/api/v1/user")
app.include_router(auth.router, prefix="/api/v1/auth")
