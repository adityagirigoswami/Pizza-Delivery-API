from fastapi import FastAPI
from database import Base, engine
from routers import users, pizzas, orders
from fastapi.responses import HTMLResponse


app = FastAPI(title="🍕 Pizza Delivery API")

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(pizzas.router)
app.include_router(orders.router)

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <h1>🍕 Pizza Delivery API</h1>
    <p>Go to <a href="/docs">/docs</a> for the Swagger UI.</p>
    """