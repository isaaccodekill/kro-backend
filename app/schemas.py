from pydantic import BaseModel, Field
import uuid as uuidpkg

from app.enums import TransactionType

from datetime import datetime


class Transaction(BaseModel):
    id: int
    amount: float
    type: TransactionType = Field(default=TransactionType.DEPOSIT)
    timestamp: datetime
    payment_method: str = None
    user_id: int


class CreateUser(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


class LoginUser(BaseModel):
    email: str
    password: str


class User(BaseModel):
    id: uuidpkg.UUID
    first_name: str
    last_name: str
    email: str
