from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from schedule import every, repeat
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shopping_lists.db"
db = SQLAlchemy(app)

class ShoppingList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    items = db.relationship("Item", backref="shopping_list", lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    shopping_list_id = db.Column(db.Integer, db.ForeignKey("shopping_list.id"), nullable=False)

@app.route("/shopping_lists", methods=["GET"])
def get_shopping_lists():
    shopping_lists = ShoppingList.query.all()
    return jsonify([{"id": list.id, "name": list.name} for list in shopping_lists])

@app.route("/shopping_lists", methods=["POST"])
def create_shopping_list():
    data = request.get_json()
    shopping_list = ShoppingList(name=data["name"])
    db.session.add(shopping_list)
    db.session.commit()
    return jsonify({"id": shopping_list.id, "name": shopping_list.name})

@app.route("/shopping_lists/<int:list_id>/items", methods=["GET"])
def get_items(list_id):
    items = Item.query.filter_by(shopping_list_id=list_id).all()
    return jsonify([{"id": item.id, "name": item.name, "quantity": item.quantity} for item in items])

@app.route("/shopping_lists/<int:list_id>/items", methods=["POST"])
def create_item(list_id):
    data = request.get_json()
    item = Item(name=data["name"], quantity=data["quantity"], shopping_list_id=list_id)
    db.session.add(item)
    db.session.commit()
    return jsonify({"id": item.id, "name": item.name, "quantity": item.quantity})

if __name__ == "__main__":
    app.run(debug=True)