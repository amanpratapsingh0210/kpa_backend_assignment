from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
import database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="KPA Form Data API",
    description="An API to submit and retrieve form data for the KPA ERP assignment.",
    version="1.0.0"
)

@app.post("/api/v1/form-data/", response_model=schemas.FormData, status_code=201)
def create_form_data(form_data: schemas.FormDataCreate, db: Session = Depends(database.get_db)):
    
    # Check if a user with the same phone number or email already exists to avoid duplicates.
    db_form_data_phone = db.query(models.FormData).filter(models.FormData.phone_number == form_data.phone_number).first()
    if db_form_data_phone:
        raise HTTPException(status_code=400, detail="Phone number already registered")
    
    if form_data.email:
        db_form_data_email = db.query(models.FormData).filter(models.FormData.email == form_data.email).first()
        if db_form_data_email:
            raise HTTPException(status_code=400, detail="Email already registered")
        
    new_entry = models.FormData(**form_data.dict())
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    
    return new_entry

@app.get("/api/v1/form-data/", response_model=List[schemas.FormData])
def read_all_form_data(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    
    all_entries = db.query(models.FormData).offset(skip).limit(limit).all()
    return all_entries

@app.get("/")
def read_root():
    return {"message": "Welcome to the KPA Form Data API. Go to /docs to see the API documentation."}
