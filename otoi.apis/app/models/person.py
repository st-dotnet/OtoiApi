from app.extensions import db

class Person(db.Model):
    __tablename__ = "person"
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    person_type_id = db.Column(db.Integer, db.ForeignKey('person_type.id'), nullable=False)
    mobile = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    gst = db.Column(db.String(20), nullable=True)  # GST Number
    
    # Relationships
    person_type = db.relationship("PersonType", backref="persons")
