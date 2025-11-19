from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base

class Merchant(Base):
    __tablename__ = "merchant"

    id = Column(Integer, primary_key=True, index=True)
    merchant_name = Column(String(100), unique=True, nullable=False)
    default_category_id = Column(Integer, ForeignKey("categories.id"))
    default_account_id = Column(Integer, ForeignKey("accounts.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

    account = relationship("Account", foreign_keys=[default_account_id])
    category = relationship("Category", foreign_keys=[default_category_id]) 
    descriptions = relationship("MerchantDescription", back_populates="merchant", cascade="all, delete-orphan")

class MerchantDescription(Base):
    __tablename__ = "merchant_description"

    id = Column(Integer, primary_key=True, index=True)
    merchant_id = Column(Integer, ForeignKey("merchant.id", ondelete="CASCADE"), nullable=False)
    description = Column(String(200), nullable=False)

    merchant = relationship("Merchant", back_populates="descriptions")