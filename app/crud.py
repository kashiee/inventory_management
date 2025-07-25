"""
CRUD operations for users and products.
"""
from sqlalchemy.orm import Session
from . import models, schemas, auth
from fastapi import HTTPException, status

def get_user_by_username(db: Session, username: str):
    """Retrieve a user by username."""
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    """Create a new user with hashed password. Raises 409 if username exists."""
    db_user = get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=409, detail="Username already registered")
    hashed_password = auth.get_password_hash(user.password)
    new_user = models.User(username=user.username, password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def authenticate_user(db: Session, username: str, password: str):
    """Authenticate a user by username and password. Returns user or None."""
    user = get_user_by_username(db, username)
    if not user or not auth.verify_password(password, user.password_hash):
        return None
    return user

def create_product(db: Session, product: schemas.ProductCreate):
    """Create a new product."""
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product_quantity(db: Session, product_id: int, quantity: int):
    """Update the quantity of a product by ID. Raises 404 if not found."""
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product.quantity = quantity
    db.commit()
    db.refresh(product)
    return product

def get_products(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a paginated list of products."""
    return db.query(models.Product).offset(skip).limit(limit).all() 