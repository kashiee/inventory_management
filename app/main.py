"""
Main FastAPI application with all API endpoints for inventory management.
"""
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from . import models, schemas, crud, auth
from .database import engine, Base
from .dependencies import get_db, get_current_user
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inventory Management Tool", description="Backend APIs for Inventory Management", version="1.0.0")

# Allow all CORS for testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/register", response_model=schemas.UserOut, status_code=201)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Register a new user."""
    return crud.create_user(db, user)

@app.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Authenticate user and return JWT token."""
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/products", response_model=schemas.ProductOut, status_code=201)
def add_product(product: schemas.ProductCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    """Add a new product (auth required)."""
    return crud.create_product(db, product)

@app.put("/products/{product_id}/quantity", response_model=schemas.ProductOut)
def update_quantity(product_id: int, update: schemas.ProductQuantityUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    """Update product quantity (auth required)."""
    return crud.update_product_quantity(db, product_id, update.quantity)

@app.get("/products", response_model=List[schemas.ProductOut])
def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    """Get a paginated list of products (auth required)."""
    return crud.get_products(db, skip=skip, limit=limit) 