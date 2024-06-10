import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'your_default_secret_key')

db = SQLAlchemy(app)

class GeneralUser(db.Model):
    __tablename__ = 'general_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone_number = db.Column(db.String(16), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username

class AdminStaffData(db.Model):
    __tablename__ = 'admin_staff_data'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone_number = db.Column(db.String(16), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=True)
    city = db.Column(db.String(50), nullable=True)
    state = db.Column(db.String(50), nullable=True)
    zipcode = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<AdminStaffData %r>' % self.username


class GeneralQuotation(db.Model):
    __tablename__ = 'general_quotation'
    id = db.Column(db.Integer, primary_key=True)
    shippment_type = db.Column(db.String(10))
    commodity = db.Column(db.String(100))
    container_type = db.Column(db.Text, nullable=True)
    number_of_containers = db.Column(db.String(100), nullable=True)
    type_of_vessel = db.Column(db.String(50), nullable=True)
    gross_weight = db.Column(db.Text)
    cbm = db.Column(db.Float, nullable=True)
    number_of_packages = db.Column(db.Integer, nullable=True)
    remark = db.Column(db.Text, nullable=True)
    port_of_receipt = db.Column(db.String(50))
    port_of_loading = db.Column(db.String(50))
    port_of_discharge = db.Column(db.String(50))
    final_place_of_delivery = db.Column(db.String(50))
    commodity_type = db.Column(db.String(50))
    un_number = db.Column(db.String(10), nullable=True)
    haz_class = db.Column(db.String(10), nullable=True)
    status = db.Column(db.String(100))
    created_by = db.Column(db.String(50))
    quotation_pdf = db.Column(db.LargeBinary, nullable=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<GeneralQuotation {self.id}>'
