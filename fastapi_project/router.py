from fastapi import FastAPI, Depends
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from model import ProductModel
from schema import ProductCreate
from database import get_db
from database import Base
from database import engine

app = FastAPI()


# Create the tables (just in case you add models later)
Base.metadata.create_all(bind=engine)


@app.get("/products/")
async def read_products(
    db: Session = Depends(get_db)
):
    # You can now use 'db' to query the database
    products = db.query(ProductModel).all()
   
    return {
        "message": "Products retrieved",
        "params": products,
        "db_status": "Database session is active"
    }

@app.get("/orders/")
async def read_orders(
    db: Session = Depends(get_db)
):
    return {
        "message": "Orders retrieved",
        "params": "",
        "db_status": "Database session is active"
    }
    
@app.post("/products")
def create_product(
    product:ProductCreate,
    db:Session =Depends(get_db)):
        new_product=ProductModel(
            name=product.name,
            description=product.description,
            price=product.price,
            quantity=product.quantity
        )
    
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
