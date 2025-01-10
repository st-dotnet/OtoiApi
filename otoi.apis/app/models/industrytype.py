from app.extensions import db

class IndustryType(db.Model):
    __tablename__ = "industry_type"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
