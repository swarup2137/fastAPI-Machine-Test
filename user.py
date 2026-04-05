from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, dependencies, auth

router = APIRouter()

@router.post("/users/")
def register(user: schemas.UserCreate, db: Session = Depends(dependencies.get_db)):
    existing = db.query(models.User).filter(models.User.email == user.email).first()
    if existing:
        raise HTTPException(400, "Email already exists")

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    return {"message": "User created"}

@router.post("/auth/login")
def login(user: schemas.Login, db: Session = Depends(dependencies.get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()

    if not db_user or db_user.password != user.password:
        raise HTTPException(401, "Invalid credentials")

    token = auth.create_token({"user_id": db_user.id})
    return {"access_token": token}

@router.get("/users/")
def get_users(db: Session = Depends(dependencies.get_db)):
    return db.query(models.User).all()
