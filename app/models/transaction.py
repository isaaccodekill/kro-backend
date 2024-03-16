import uuid as uuidpkg
from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from uuid import uuid4
import datetime
from decimal import Decimal


class Transaction(SQLModel, table=True):
    id: uuidpkg.UUID = Field(default_factory=uuid4, primary_key=True, index=True,nullable=False)
    amount: Decimal = Field(default=0.0, sa_column_kwargs={"sa_column": Decimal()})
    type: str = "deposit"
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.now, nullable=False)
    payment_method: Optional[str] = None
    user_id: uuidpkg.UUID = Field(default_factory=uuid4, primary_key=True, index=True,nullable=False)
    user: "User" = Relationship(back_populates="transactions")


from app.models.user import User

Transaction.update_forward_refs()
