from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)

class Pizza(Base):
    __tablename__ = "pizzas"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    pizza_id = Column(Integer, ForeignKey("pizzas.id"))
    quantity = Column(Integer)

    user = relationship("User")
    pizza = relationship("Pizza")

