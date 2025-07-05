from flask import Blueprint, request, jsonify
from flask_login import login_required
from app.models import Product
from app.extensions import db

products_bp = Blueprint('products', __name__, url_prefix='/api/products')

@products_bp.route('', methods=['GET'])
def get_prods():
    prods = Product.query.all()
    return jsonify([
        {"id": p.id, "name": p.name, "price": p.price, "description": p.description}
        for p in prods
    ])

@products_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    prod = Product.query.get(product_id)
    if not prod:
        return jsonify({"message": "Product not found"}), 404
    return jsonify({"id": prod.id, "name": prod.name, "price": prod.price, "description": prod.description}), 200

@products_bp.route('/add', methods=['POST'])
@login_required
def add_product():
    data = request.json

    if isinstance(data, list):
        added = 0
        for item in data:
            if 'name' in item and 'price' in item:
                db.session.add(Product(name=item['name'], price=item['price'], description=item.get('description', '')))
                added += 1
        db.session.commit()
        return jsonify({"message": f"{added} products added successfully"}), 200

    elif isinstance(data, dict) and 'name' in data and 'price' in data:
        db.session.add(Product(name=data['name'], price=data['price'], description=data.get('description', '')))
        db.session.commit()
        return jsonify({"message": "Product added successfully"}), 200

    return jsonify({"message": "Invalid product data"}), 400

@products_bp.route('/delete/<int:product_id>', methods=['DELETE'])
@login_required
def delete_product(product_id):
    prod = Product.query.get(product_id)
    if prod:
        db.session.delete(prod)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"}), 200
    return jsonify({"message": "Product not found"}), 400

@products_bp.route('/update/<int:product_id>', methods=['PUT'])
@login_required
def update_product(product_id):
    prod = Product.query.get(product_id)
    if not prod:
        return jsonify({"message": "Product not found"}), 404
    data = request.json
    prod.name = data.get('name', prod.name)
    prod.price = data.get('price', prod.price)
    prod.description = data.get('description', prod.description)
    db.session.commit()
    return jsonify({"message": "Product updated successfully"}), 200