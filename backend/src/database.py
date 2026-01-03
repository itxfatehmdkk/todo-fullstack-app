"""Database setup for the Todo Full-Stack Web Application."""

from sqlmodel import create_engine, Session
from .models.task import Task  # Import all models to register them
from .models.user import User


# Using SQLite for Railway deployment compatibility
import os
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo_app.db")

# For SQLite, we need to handle the URL differently
if DATABASE_URL.startswith("sqlite"):
    # SQLite URLs should use three slashes for relative paths
    connect_args = {"check_same_thread": False}
    engine = create_engine(DATABASE_URL, echo=True, connect_args=connect_args)
else:
    # For PostgreSQL
    engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    """Create database tables."""
    # Create all tables
    Task.metadata.create_all(bind=engine)
    User.metadata.create_all(bind=engine)


def get_session():
    """Get database session."""
    with Session(engine) as session:
        yield session