from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base

class TransactionType(Base):
    __tablename__ = "transaction_types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    date = Column(DateTime(timezone=True), nullable=False)
    amount = Column(Numeric(18, 2), nullable=False)
    transaction_type_id = Column(Integer, ForeignKey("transaction_types.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    description = Column(Text)
    related_account_id = Column(Integer, ForeignKey("accounts.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    account = relationship("Account", back_populates="transactions", foreign_keys=[account_id])
    related_account = relationship("Account", foreign_keys=[related_account_id])
    transaction_type = relationship("TransactionType")
    category = relationship("Category")