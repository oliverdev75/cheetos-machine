from sqlalchemy import Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from dataclasses import dataclass
from app import db

#Tablas intermedias
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

#Tablas
@dataclass
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(Integer(), primary_key=True)
    name = db.Column(String(255), nullable=False)
    email = db.Column(String(255), unique=True)
    password = db.Column(String(255), nullable=False)
    created_at = db.Column(DateTime(), default=datetime.now(), nullable=False)
    updated_at = db.Column(DateTime(), default=None)
    roles = db.relationship("Role", secondary="user_role", backref="users")
    orders = db.relationship("Order", backref="user")

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'roles': self.roles,
            'orders': self.orders,
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
    price = db.Column(Float(2), nullable=False)
    image = db.Column(String(255), nullable=False)
    created_at = db.Column(DateTime(), default=datetime.now(), nullable=False)
    updated_at = db.Column(DateTime(), default=None)

    orders = db.relationship("Order", secondary="order_product", back_populates="products")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,

            'price': self.price,
            'image': self.image,
            'orders': self.orders,

            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def __repr__(self):
        return f"<Product >"


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(Integer(), primary_key=True)
    user_id = db.Column(Integer(), ForeignKey('users.id'), nullable=False)
    price = db.Column(Float(2), nullable=False)
    created_at = db.Column(DateTime(), default=datetime.now(), nullable=False)
    updated_at = db.Column(DateTime(), default=None)

    products = db.relationship("Product", secondary="order_product", back_populates="orders")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'price': self.price,
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


