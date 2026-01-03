"""Database models for the Todo Full-Stack Web Application."""

from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Task(Base):
    """Task model for the database."""
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)


# Pydantic models for API
from pydantic import BaseModel


class TaskBase(BaseModel):
    """Base model for task with common fields."""
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskCreate(TaskBase):
    """Model for creating a new task."""
    pass


class TaskUpdate(BaseModel):
    """Model for updating an existing task."""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskPublic(TaskBase):
    """Public model for task with ID and timestamps."""
    id: int
    user_id: str
    created_at: datetime
    updated_at: datetime