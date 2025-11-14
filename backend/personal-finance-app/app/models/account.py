from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Date, DateTime, CheckConstraint, func
from sqlalchemy.orm import relationship, synonym
from app.core.database import Base
from app.models.user import User
from app.models.institution import Institution


class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    institution_id = Column(Integer, ForeignKey('institutions.id'), nullable=True)

    account_type = Column(String(50), nullable=True)
    account_name = Column(String(255), nullable=True)
    # Backwards-compatible attribute used elsewhere in the codebase
    name = synonym('account_name')

    account_number_last4 = Column(String(4), nullable=True)
    balance = Column(Numeric(18, 2), nullable=False, server_default="0")
    currency = Column(String(10), nullable=False, server_default='USD')
    opened_date = Column(Date, nullable=True)
    closed_date = Column(Date, nullable=True)
    status = Column(String(20), nullable=False, server_default='active')

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    owner = relationship('User')
    institution = relationship('Institution')

    __table_args__ = (
        CheckConstraint("account_type IN ('checking','savings','credit_card','investment','loan','retirement')", name='accounts_account_type_check'),
    )
