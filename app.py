from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///ecommerce.db'

db= SQLAlchemy(app)

# Modelagem
# produto (id,name,price, description)
class Product(db.Model):
   id = db.Column(db.Integer, primary_key= True)
   name = db.Column(db.String(120), nullable= False)
   price = db.Column(db.Float, nullable= False)
   description = db.Column(db.Text, nullable= True)

@app.route('/api/products/add', methods=["POST"])
def add_product():
   data = request.json
   if not data or "name" not in data or "price" not in data:
      return jsonify({"error" : "Dados invalidos"}), 400
   product = Product(
      name=data["name"], 
      price=data["price"], 
      description=data.get("description", "")
      )
   db.session.add(product)
   db.session.commit()
   return jsonify({"message": "Produto cadastrado com sucesso"}), 201

@app.route('/')
def hello_world():
  return "Hello world"

if __name__ == "__main__":
    app.run(debug=True)