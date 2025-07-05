from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

class PizzaOut(BaseModel):
    id: int
    name: str
    price: float
    class Config:
        orm_mode = True

class PizzaCreate(BaseModel):
    name: str
    price: float

class OrderCreate(BaseModel):
    pizza_id: int
    quantity: int

class OrderOut(BaseModel):
    id: int
    user_id: int
    pizza_id: int
    quantity: int
    class Config:
        orm_mode = True
