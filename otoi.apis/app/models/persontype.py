from app.extensions import db

class PersonType(db.Model):
    __tablename__ = "person_type"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)  # e.g., "Customer", "Vendor"
