from app.extensions import db
from app.models.associations import user_business

class Business(db.Model):
    __tablename__ = "business"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    phone_number = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    is_gst_registered = db.Column(db.Boolean, nullable=False, default=False)
    gst_number = db.Column(db.String(20), nullable=True, unique=True)
    pan_number = db.Column(db.String(10), nullable=True, unique=True)
    terms_and_conditions = db.Column(db.Text, nullable=True)
    signature = db.Column(db.Text, nullable=True)

    users = db.relationship(
        "User",
        secondary= user_business,
        back_populates="businesses"
    )