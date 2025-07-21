from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class FormDataBase(BaseModel):
    full_name: str
    phone_number: str
    email: Optional[EmailStr] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    
class FormDataCreate(FormDataBase):
    pass

class FormData(FormDataBase):
    id: int
    is_active: bool
    
    class Config:
        from_attributes = True