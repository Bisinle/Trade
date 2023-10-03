from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData,UniqueConstraint
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    company = db.Column(db.String)  # Corrected column name
    phone_number = db.Column(db.Integer)
    email = db.Column(db.String)
    __table_args__ = (UniqueConstraint("phone_number", "email", name="Vendor_unique_constraint"),)

    products = db.relationship('Product', backref ='vendor')



    def __repr__(self):
        return f'(id: {self.id}, name: {self.name}, company: {self.company}, phone_number: {self.phone_number}, email: {self.email} )'

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone_number = db.Column(db.Integer)
    email = db.Column(db.String)
    joined = db.Column(db.DateTime, server_default=db.func.now())
    __table_args__ = (UniqueConstraint("phone_number", "email", name="Customer_unique_constraint"),)



    def __repr__(self):
        return f'(id: {self.id}, name: {self.name}, phone_number: {self.phone_number}, email: {self.email} , joined: {self.joined})'



class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prod_name = db.Column(db.String)
    prod_description = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    category = db.Column(db.String)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))


    def __repr__(self):
        return f'(id: {self.id}, prod_name: {self.prod_name}, price: {self.price}, category: {self.category}, quantity: {self.quantity} ,vendor_id: {self.vendor_id})'
