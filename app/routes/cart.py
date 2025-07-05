from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import CartItem, Product
from app.extensions import db

cart_bp = Blueprint('cart', __name__, url_prefix='/api/cart')

@cart_bp.route('', methods=['GET'])
@login_required
def view_cart():
    cart_items = db.session.query(CartItem).join(Product).filter(CartItem.user_id == current_user.id).with_entities(
        CartItem.id.label('cart_id'), Product.id.label('product_id'), Product.name, Product.price
    ).all()

    return jsonify([
        {"cart_id": c.cart_id, "product_id": c.product_id, "name": c.name, "price": c.price}
        for c in cart_items
    ]), 200

@cart_bp.route('/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.add(CartItem(user_id=current_user.id, product_id=product.id))
        db.session.commit()
        return jsonify({"message": "Item added to the cart successfully"}), 200
    return jsonify({"message": "Failed to add item to the cart"}), 400

@cart_bp.route('/remove/<int:product_id>', methods=['DELETE'])
@login_required
def remove_from_cart(product_id):
    item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if item:
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": "Item removed from the cart successfully"}), 200
    return jsonify({"message": "Failed to remove item from the cart"}), 400

@cart_bp.route('/checkout', methods=['POST'])
@login_required
def checkout():
    CartItem.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    return jsonify({"message": "Checkout successful. Cart has been cleared."}), 200
