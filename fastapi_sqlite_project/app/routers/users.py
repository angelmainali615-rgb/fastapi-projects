from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal, engine
from ..models import User, Base
from ..schemas import UserCreate, UserOut

router = APIRouter(prefix="/users", tags=["Users"])

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/", response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
