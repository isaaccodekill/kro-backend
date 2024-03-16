import uuid as uuidpkg
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from datetime import datetime
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID


class User(SQLModel, table=True):
    id: uuidpkg.UUID = Field(default_factory=uuid4, primary_key=True, index=True,nullable=False)
    first_name: str
    last_name: str
    email: str
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.now, nullable=False)
    transactions: list["Transaction"] = Relationship(back_populates="user")


from app.models.transaction import Transaction

User.update_forward_refs()
