from sqlalchemy import Column, Integer, String, Date, Boolean
from database import Base

class FormData(Base):
    __tablename__ = "form_data"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    phone_number = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True, nullable=True)
    date_of_birth = Column(Date, nullable=True)
    gender = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)