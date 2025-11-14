from sqlalchemy import Column, Integer, String, CheckConstraint
from app.core.database import Base


class Institution(Base):
    __tablename__ = 'institutions'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    type = Column(String(50), nullable=True)
    website = Column(String(255), nullable=True)

    __table_args__ = (
        CheckConstraint("type IN ('bank','investment','credit','loan','other')", name='institutions_type_check'),
    )
