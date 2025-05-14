from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# Database configuration
DB_USER = os.getenv('MYSQL_USER', 'myuser')
DB_PASSWORD = os.getenv('MYSQL_PASSWORD', 'mypassword')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('MYSQL_DATABASE', 'mydatabase')

# Using PyMySQL as the driver
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Create engine with pool_pre_ping to handle connection issues
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 