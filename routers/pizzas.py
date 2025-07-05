from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Pizza
from schemas import PizzaOut, PizzaCreate
from database import SessionLocal

router = APIRouter(prefix="/pizzas", tags=["Pizzas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PizzaOut)
def create_pizza(pizza: PizzaCreate, db: Session = Depends(get_db)):
    new_pizza = Pizza(name=pizza.name, price=pizza.price)
    db.add(new_pizza)
    db.commit()
    db.refresh(new_pizza)
    return new_pizza

@router.get("/", response_model=list[PizzaOut])
def list_pizzas(db: Session = Depends(get_db)):
    return db.query(Pizza).all()
