from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database connection settings
DATABASE_URL = "sqlite:///./database.db"

# Create a new database engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a database session
session = SessionLocal()

# Import your database models here
# e.g., from .models import User, Item
