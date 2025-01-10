from app.extensions import db

class BusinessRegistrationType(db.Model):
    __tablename__ = "business_registration_type"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
