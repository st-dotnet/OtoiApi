from app.extensions import db

class BusinessType(db.Model):
    __tablename__ = "business_type"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
