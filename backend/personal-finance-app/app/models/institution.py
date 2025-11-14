from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base

class InstitutionType(Base):
    __tablename__ = "institution_types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)

class Institution(Base):
    __tablename__ = "institutions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    institution_type_id = Column(Integer, ForeignKey("institution_types.id"))
    website = Column(String(255))

    institution_type = relationship("InstitutionType")
    accounts = relationship("Account", back_populates="institution")