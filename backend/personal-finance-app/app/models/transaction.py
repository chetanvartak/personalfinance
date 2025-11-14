from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Numeric, CheckConstraint, func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    date = Column(DateTime(timezone=True), nullable=True)
    amount = Column(Numeric(18, 2), nullable=False)
    transaction_type = Column(String(50), nullable=True)
    category = Column(String(50), nullable=True)
    description = Column(Text, nullable=True)
    related_account_id = Column(Integer, ForeignKey('accounts.id'), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    account = relationship('Account', foreign_keys=[account_id])
    related_account = relationship('Account', foreign_keys=[related_account_id])

    __table_args__ = (
        CheckConstraint("transaction_type IN ('deposit','withdrawal','payment','transfer','investment','fee','interest')", name='transactions_transaction_type_check'),
    )
