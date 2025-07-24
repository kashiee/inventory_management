from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from .database import SessionLocal
from .auth import decode_access_token
from .models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_access_token(token)
    if payload is None or "sub" not in payload:
        raise credentials_exception
    username = payload["sub"]
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception
    return user 