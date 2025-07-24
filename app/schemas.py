from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ProductBase(BaseModel):
    name: str
    type: str
    sku: str
    image_url: Optional[str] = None
    description: Optional[str] = None
    quantity: int
    price: float

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    class Config:
        orm_mode = True

class ProductQuantityUpdate(BaseModel):
    quantity: int 