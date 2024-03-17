import os.path

from fastapi import FastAPI
from dotenv import load_dotenv

print("on_startup")
dotenv_path = os.path.join('..', '.env')
print(dotenv_path, "dotenv_path")
load_dotenv()

from app.controllers import user, auth, transaction
from app.database import create_tables
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# add CORS middleware
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)


# on start up, create the tables
@app.on_event("startup")
async def on_startup():
    create_tables()


app.include_router(user.router, prefix="/api/v1/user")
app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(transaction.router, prefix="/api/v1/transactions")
