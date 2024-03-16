from pydantic import BaseModel, Field

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


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str