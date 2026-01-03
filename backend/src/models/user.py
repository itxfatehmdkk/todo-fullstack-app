"""User model for the Todo Full-Stack Web Application."""

from datetime import datetime
from typing import Optional
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """User model for the database (managed by Better Auth)."""
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    theme_preference = Column(String(20), default="system")  # light, dark, or system


# Pydantic models for API
from pydantic import BaseModel


class UserBase(BaseModel):
    """Base model for user with common fields."""
    email: str
    name: str


class UserPublic(UserBase):
    """Public model for user with ID and timestamps."""
    id: str
    created_at: datetime
    theme_preference: Optional[str] = "system"  # light, dark, or system