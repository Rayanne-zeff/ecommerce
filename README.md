# 🛒 E-commerce API with Flask + Docker + AWS

This is a RESTful API built with **Flask** and **SQLAlchemy**, simulating core features of an e-commerce system. It provides user authentication, product management, and cart operations — all containerized with Docker and deployed on AWS Elastic Beanstalk.

---

## 🚀 Technologies Used

- [Python 3.13](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Flask-Login](https://flask-login.readthedocs.io/)
- [Flask-CORS](https://corydolphin.com/flask-cors/)
- [SQLite](https://www.sqlite.org/index.html)
- [Docker](https://www.docker.com/)
- [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)

---

## 📦 API Features

- ✅ Product CRUD (Create, Read, Update, Delete)
- ✅ User login/logout with session-based authenticationa
- ✅ Add, remove, and view items in the shopping cart
- ✅ Checkout functionality (clear cart)
- ✅ Fully Dockerized for consistent deployment
- ✅ Deployed to AWS Elastic Beanstalk

---

## 🌐 Base URL (Example)

```
https://api-ecommerce-dev.eba-xxxxx.us-east-1.elasticbeanstalk.com/
```

---

## 🔓 Public Endpoints

| Method | Route                   | Description           |
|--------|-------------------------|-----------------------|
| GET    | `/`                     | Health check          |
| GET    | `/api/products`         | Retrieve all products |
| GET    | `/api/products/<id>`    | Get product by ID     |

---

## 🔐 Authenticated Endpoints (Login required)

| Method | Route                              | Description                         |
|--------|-------------------------------------|-------------------------------------|
| POST   | `/login`                            | Log in a user                       |
| POST   | `/logout`                           | Log out the current user            |
| POST   | `/api/products/add`                 | Add one or more products            |
| PUT    | `/api/products/update/<id>`         | Update product details              |
| DELETE | `/api/products/delete/<id>`         | Delete a product                    |
| GET    | `/api/cart`                         | View the current user's cart        |
| POST   | `/api/cart/add/<product_id>`        | Add a product to the cart           |
| DELETE | `/api/cart/remove/<product_id>`     | Remove a product from the cart      |
| POST   | `/api/cart/checkout`                | Checkout (clear all items in cart)  |

---

## 🧾 Sample JSON for Product Creation

```json
{
  "name": "Notebook A5",
  "price": 19.90,
  "description": "60 sheets, hardcover, ruled."
}
```

---

## 🐳 Running with Docker

```bash
# Build the image
docker build -t ecommerce-api .

# Run the container
docker run -p 8080:8080 ecommerce-api
```

---

## ☁️ Deploying to AWS Elastic Beanstalk

```bash
# 1. Initialize your app
eb init -p docker ecommerce-api --region us-east-1

# 2. Create the environment
eb create api-ecommerce-dev

# 3. Deploy changes
eb deploy
```

---

## 📄 License

This project is licensed under the **MIT License**.  
Feel free to use, fork, and modify it.

---

## ✨ Contributions

Contributions are welcome!  
Feel free to open an issue or submit a pull request.