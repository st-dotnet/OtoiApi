from app.extensions import db

class PersonAddress(db.Model):
    __tablename__ = "person_address"
    
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    
    # Relationships
    person = db.relationship("Person", backref="person_addresses")
    address = db.relationship("Address", backref="address_persons")
