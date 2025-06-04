from sqlalchemy import Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from dataclasses import dataclass
from app import db

user_role = db.Table(
    'user_role',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True)
)

product_order = db.Table(
    'order_product',
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), primary_key=True)
)

@dataclass
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(Integer(), primary_key=True)
    name = db.Column(String(255), nullable=False)
    email = db.Column(String(255), unique=True)
    password = db.Column(String(255), nullable=False)
    tokens = db.Column(Float(precision=2), default=0.0, nullable=False)
    created_at = db.Column(DateTime(), default=datetime.now(), nullable=False)
    updated_at = db.Column(DateTime(), default=None)
    roles = db.relationship("Role", secondary="user_role", backref="users")
    orders = db.relationship("Order", backref="user")

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'tokens': self.tokens,
            'roles': self.roles,
            'orders': [order.to_dict() for order in self.orders],
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
        return data

    def __repr__(self):
        return f"<User >"


@dataclass
class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(Integer(), primary_key=True)
    name = db.Column(String(255), nullable=False)
    tokens = db.Column(Integer(), nullable=False)
    image = db.Column(String(255), nullable=False)
    created_at = db.Column(DateTime(), default=datetime.now(), nullable=False)
    updated_at = db.Column(DateTime(), default=None)

    orders = db.relationship("Order", secondary="order_product", back_populates="products")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'tokens': self.tokens,
            'image': self.image,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def __repr__(self):
        return f"<Product >"


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(Integer(), primary_key=True)
    user_id = db.Column(Integer(), ForeignKey('users.id'), nullable=False)
    tokens = db.Column(Integer(), nullable=False)
    delivered_at = db.Column(DateTime(), default=None)
    created_at = db.Column(DateTime(), default=datetime.now, nullable=False)
    updated_at = db.Column(DateTime(), default=None)
    products = db.relationship("Product", secondary="order_product", back_populates="orders")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'tokens': self.tokens,
            'delivered_at': self.delivered_at,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'products': [p.id for p in self.products]
        }



@dataclass
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(Integer(), primary_key=True)
    name = db.Column(String(255), unique=True)
    created_at = db.Column(DateTime(), default=datetime.now(), nullable=False)
    updated_at = db.Column(DateTime(), default=None)

    def to_dict(self):
        data = { 'id': self.id, 'name': self.name, 'created_at': self.created_at, 'updated_at': self.updated_at }
        return data

    def __repr__(self):
        return f"<Role >"


