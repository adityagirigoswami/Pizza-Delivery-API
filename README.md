# 🍕 Pizza Delivery API

The **Pizza Delivery API** is a backend web service built using **FastAPI** that handles **user registration**, **pizza listings**, and **order placement** for a fictional online pizza delivery platform.

It provides a modular, clean, and scalable backend architecture ideal for learning modern API development.

---

## 📦 Project Structure

```
Pizza-Delivery-API/
├── main.py              # FastAPI app entry point
├── models.py            # SQLAlchemy DB models
├── schemas.py           # Pydantic request/response schemas
├── database.py          # DB engine and session setup
├── auth.py              # Authentication and login logic
├── routers/             # Route modules (APIRouters)
│   ├── users.py         # User registration/login routes
│   ├── pizzas.py        # Pizza listing & management
│   └── orders.py        # Order placement and retrieval
├── requirements.txt     # Project dependencies
```

---

## 🚀 Features

- 🔐 User Registration and Login
- 🍕 Add/List Available Pizzas
- 📦 Place Orders and Track Them
- 📃 Interactive API Docs (Swagger & ReDoc)
- 🧱 Modular and Extensible Design

---

## 🛠️ Tech Stack

- **FastAPI** – High-performance Python API framework
- **SQLite** – Lightweight relational database
- **SQLAlchemy** – ORM for DB operations
- **Pydantic** – Schema validation
- **Uvicorn** – ASGI server for FastAPI

---

## ⚙️ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/adityagirigoswami/Pizza-Delivery-API.git
cd Pizza-Delivery-API
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Server

```bash
uvicorn main:app --reload
```

### 5️⃣ Access API Docs

- Swagger UI → http://127.0.0.1:8000/docs  
- ReDoc UI → http://127.0.0.1:8000/redoc

---

## 🧪 Example Endpoints

| Method | Endpoint        | Description                 |
|--------|------------------|-----------------------------|
| POST   | `/register/`     | Register a new user         |
| POST   | `/login/`        | Login and get token         |
| GET    | `/pizzas/`       | List all available pizzas   |
| POST   | `/orders/`       | Place a new pizza order     |
| GET    | `/orders/{id}`   | Retrieve order by ID        |

---

## 📌 Future Improvements

- ✅ JWT Authentication Support
- ⏳ Docker & Docker Compose Setup
- ⏳ Admin Panel for Managing Pizzas
- ⏳ Payment Gateway Integration (Razorpay, Paytm)
- ⏳ Unit Testing with `pytest`

---

## 📜 License

This project is licensed under the **MIT License**.  
© 2024 [Aditya Giri Goswami](https://github.com/adityagirigoswami)

---

## 🤝 Contributing

Contributions, suggestions, and forks are welcome!  
If you find a bug or want to improve something, feel free to open an issue or submit a PR.

---

## 📬 Contact

📧 adityagirigoswami@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/adityagirigoswami)

---

## ⭐ Star the Repo

If you like this project, give it a ⭐ to help others discover it!
