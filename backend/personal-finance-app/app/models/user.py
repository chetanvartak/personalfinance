from sqlalchemy import Column, Integer, String, Date, DateTime, func
from sqlalchemy.orm import synonym
from app.core.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    # Column name matches the existing DB dump
    password_hash = Column(String(255), nullable=False)
    # Backwards-compatible attribute used elsewhere in the codebase
    #hashed_password = synonym('password_hash')

    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    date_of_birth = Column(Date, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
