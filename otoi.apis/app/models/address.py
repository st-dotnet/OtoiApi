from app.extensions import db

class Address(db.Model):
    __tablename__ = "address"
    
    id = db.Column(db.Integer, primary_key=True)
    address1 = db.Column(db.String(255), nullable=False)
    address2 = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    pin = db.Column(db.String(20), nullable=False)  # Postal Code
