# 🛒 E-commerce API with Flask

This is a simple RESTful API built with **Flask** and **SQLAlchemy**, simulating basic operations of an e-commerce system such as product creation, retrieval, updating, and deletion.

## 🚀 Technologies Used

- [Python 3.x](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- SQLite3 (as a local database)

## 📦 API Features

- ✅ **Add a product**  
- ✅ **List all products**  
- ✅ **Retrieve a product by ID**  
- ✅ **Update a product by ID**  
- ✅ **Delete a product by ID**

## 🧪 Available Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| `POST` | `/api/products/add` | Add a new product |
| `GET`  | `/api/products` | Get all products |
| `GET`  | `/api/products/<id>` | Get details of a specific product |
| `PUT`  | `/api/products/update/<id>` | Update an existing product |
| `DELETE` | `/api/products/delete/<id>` | Delete a product |

## 🧰 JSON Example for Product Creation

```json
{
    "name": "Notebook A5",
    "price": 19.90,
    "description": "60 sheets, hardcover, ruled."
}
