from app.extensions import db
from app.models.user import User
from app.models.role import Role
from app.models.persontype import PersonType
from app.models.businesstype import BusinessType
from app.models.industrytype import IndustryType
from app.models.businessregistrationtype import BusinessRegistrationType

def seed_data():
    # Define initial roles
    roles = ["Admin", "User"]

    # Add roles if not already present
    for role_name in roles:
        role = Role.query.filter_by(name=role_name).first()
        if not role:
            role = Role(name=role_name)
            db.session.add(role)
    
    db.session.commit()

    # Add a default super admin user
    admin_role = Role.query.filter_by(name="Admin").first()
    if not User.query.filter_by(username="admin").first():
        admin = User(username="admin", email="info@evototechnologies.com", role=admin_role)
        admin.set_password("admin123")  # Change password in production!
        db.session.add(admin)
    
    db.session.commit()
    print("Seeding completed.")

def seed_person_types():
    types = ["Customer", "Vendor"]
    for t in types:
        if not PersonType.query.filter_by(name=t).first():
            db.session.add(PersonType(name=t))
    db.session.commit()
    print("Person types seeded.")

def seed_business_types():
    business_types = ["Retailer", "Wholesaler", "Distributor", "Manufacturer", "Services"]
    for b_type in business_types:
        if not BusinessType.query.filter_by(name=b_type).first():
            db.session.add(BusinessType(name=b_type))
    db.session.commit()
    print("Business Types seeded.")

def seed_industry_types():
    industry_types = ["Other", "Agriculture", "Automobile", "Consulting", "Engineering"]
    for i_type in industry_types:
        if not IndustryType.query.filter_by(name=i_type).first():
            db.session.add(IndustryType(name=i_type))
    db.session.commit()
    print("Industry Types seeded.")

def seed_business_registration_types():
    registration_types = [
        "Private Limited Company",
        "Public Limited Company",
        "Partnership Firm",
        "Limited Liability Partnership"
    ]
    for r_type in registration_types:
        if not BusinessRegistrationType.query.filter_by(name=r_type).first():
            db.session.add(BusinessRegistrationType(name=r_type))
    db.session.commit()
    print("Business Registration Types seeded.")