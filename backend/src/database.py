"""Database setup for the Todo Full-Stack Web Application."""

from sqlmodel import create_engine, Session
from .models.task import Task  # Import all models to register them
from .models.user import User


# Using environment variable for database URL with SQLite fallback for local development
import os
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo_app.db")


# Create the engine
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