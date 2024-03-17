import os.path

from fastapi import FastAPI, Request, HTTPException
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

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


# Generic exception handler for HTTPException (internal server errors)
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})


# Custom exception handler for internal server errors (generic)
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})


@app.exception_handler(500)
async def internal_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content=jsonable_encoder({"detail": "Internal Server Error"}))


app.include_router(user.router, prefix="/api/v1/user")
app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(transaction.router, prefix="/api/v1/transactions")
