from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
import datetime
from decimal import Decimal

from app.models.user import User


class Transaction(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True, sa_column_kwargs={"sa_column": UUID()})
    amount: Decimal = Field(default=0.0, sa_column_kwargs={"sa_column": Decimal()})
    type: str = "deposit"
    timestamp: datetime
    payment_method: Optional[str] = None
    user_id: Optional[UUID] = Field(default=None, sa_column_kwargs={"sa_column": UUID(), "foreign_key": "user.id"})
    user: User = Relationship(back_populates="transactions")