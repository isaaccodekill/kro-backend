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
