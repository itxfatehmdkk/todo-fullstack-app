"""Database setup for the Todo Full-Stack Web Application."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models.task import Task, Base  # Import all models to register them
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

# Create session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_db_and_tables():
    """Create database tables."""
    # Create all tables
    Base.metadata.create_all(bind=engine)


def get_session():
    """Get database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()