from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from datetime import datetime
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

from app.models.transaction import Transaction


class User(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True, sa_column_kwargs={"sa_column": UUID()})
    first_name: str
    last_name: str
    email: str
    created_at: datetime
    updated_at: datetime
    transactions: list["Transaction"] = Relationship(back_populates="user")
