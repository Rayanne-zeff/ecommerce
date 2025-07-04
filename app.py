from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = "123456789"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

login_manager = LoginManager()
db = SQLAlchemy(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
CORS(app)

#Model
#User (id, username, password)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=True)

#Product (id, name,price, description)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

#Autentication
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get("username")).first()

    if user and data.get("password") == user.password:
            login_user(user)
            return jsonify({"message": "Logged in successfully"}), 200
        
    return jsonify({"message": "Unauthorized. Invalid credentials"}), 401

@app.route('/logout', methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout in successfully"}), 200 

@app.route('/api/products/add', methods=["POST"])
@login_required
def add_product():
    data = request.json

    # Se for uma lista de produtos
    if isinstance(data, list):
        added = 0
        for item in data:
            if 'name' in item and 'price' in item:
                new_product = Product(
                    name=item["name"],
                    price=item["price"],
                    description=item.get("description", "")
                )
                db.session.add(new_product)
                added += 1
            else:
                continue  # pula item inválido
        db.session.commit()
        return jsonify({"message": f"{added} products added successfully"}), 200

    # Se for um único produto
    elif isinstance(data, dict) and 'name' in data and 'price' in data:
        new_product = Product(
            name=data["name"],
            price=data["price"],
            description=data.get("description", "")
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify({"message": "Product added successfully"}), 200

    return jsonify({"message": "Invalid product data"}), 400

@app.route('/api/products/delete/<int:product_id>', methods=["DELETE"])
@login_required
def delete_product(product_id):
    prod = Product.query.get(product_id)
    if prod:
        db.session.delete(prod)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"}), 200
    return jsonify({"message": "Product not found"}), 400

@app.route('/api/products/<int:product_id>', methods=["GET"])
def get_product_details(product_id):
    prod = Product.query.get(product_id)
    if prod:
        return jsonify({
            "id": prod.id,
            "name": prod.name,
            "price": prod.price,
            "description": prod.description
        }), 200
    return jsonify({"message": "Product not found"}), 404

@app.route('/api/products/update/<int:product_id>', methods=["PUT"])
@login_required
def update_product(product_id):
    prod = Product.query.get(product_id)
    if not prod :
        return jsonify({"message": "Product not found"}),404
    
    data = request.json
    if 'name' in data:
        prod.name = data['name']

    if 'price' in data:
        prod.price = data['price']

    if 'description' in data:
        prod.description = data['description']

    db.session.commit()     
    return jsonify({"message": "Product updated successfully"}), 200

@app.route('/api/products', methods=['GET'])
def get_prods():
    prods = Product.query.all()
    products_list=[]
    for product in prods:
        products_data = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description
        } 
        products_list.append(products_data)

    return jsonify(products_list)

@app.route('/')
def hello_world():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True)
