from sqlalchemy.orm import sessionmaker, Session, declarative_base
from sqlalchemy import create_engine

# ==========================================
# 1. DATABASE SETUP (SQLite)
# ==========================================
# Create a file named 'test.db' in the current directory
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for your database models (if you create tables later)
Base = declarative_base()

# Create the tables (just in case you add models later)
Base.metadata.create_all(bind=engine)

# ==========================================
# 2. THE DATABASE DEPENDENCY
# ==========================================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()