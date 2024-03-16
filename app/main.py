from fastapi import FastAPI
from app.controllers import user, auth

app = FastAPI()
app.include_router(user.router, prefix="api/v1/user")
app.include_router(auth.router, prefix="api/v1/auth")
