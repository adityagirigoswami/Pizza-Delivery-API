from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Order, Pizza, User
from schemas import OrderCreate, OrderOut
from database import SessionLocal

router = APIRouter(prefix="/orders", tags=["Orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{user_id}", response_model=OrderOut)
def place_order(user_id: int, order: OrderCreate, db: Session = Depends(get_db)):
    pizza = db.query(Pizza).filter(Pizza.id == order.pizza_id).first()
    if not pizza:
        raise HTTPException(status_code=404, detail="Pizza not found")
    
    new_order = Order(user_id=user_id, pizza_id=order.pizza_id, quantity=order.quantity)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@router.get("/{user_id}", response_model=list[OrderOut])
def get_user_orders(user_id: int, db: Session = Depends(get_db)):
    return db.query(Order).filter(Order.user_id == user_id).all()
