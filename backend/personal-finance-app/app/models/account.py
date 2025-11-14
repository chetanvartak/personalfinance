from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Date, DateTime, CheckConstraint, func
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base
from app.models.user import User
from app.models.institution import Institution

class AccountType(Base):
    __tablename__ = "account_types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    institution_id = Column(Integer, ForeignKey("institutions.id"))
    account_type_id = Column(Integer, ForeignKey("account_types.id"))
    account_name = Column(String(255))
    account_number_last4 = Column(String(4))
    balance = Column(Numeric(18, 2), default=0)
    currency = Column(String(10), default='USD')
    opened_date = Column(Date)
    closed_date = Column(Date)
    status = Column(String(20), default='active')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    user = relationship("User")
    institution = relationship("Institution")
    account_type = relationship("AccountType")
    transactions = relationship("Transaction", back_populates="account", foreign_keys="[Transaction.account_id]")