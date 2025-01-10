from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.person import Person
from app.models.persontype import PersonType
from app.models.personaddress import PersonAddress
from app.models.address import Address
from sqlalchemy import or_

person_blueprint = Blueprint("person", __name__, url_prefix="/persons")

@person_blueprint.route("/", methods=["GET","OPTIONS"])
def get_persons():
    """
    Fetch a list of persons with advanced features like filtering, sorting, and pagination.
    ---
    parameters:
      - name: first_name
        in: query
        description: Filter by first name
        required: false
        schema:
          type: string
      - name: last_name
        in: query
        description: Filter by last name
        required: false
        schema:
          type: string
      - name: mobile
        in: query
        description: Filter by mobile number
        required: false
        schema:
          type: string
      - name: email
        in: query
        description: Filter by email address
        required: false
        schema:
          type: string
      - name: sort
        in: query
        description: Comma-separated field names for sorting (e.g., 'first_name,-email')
        required: false
        schema:
          type: string
      - name: page
        in: query
        description: "Page number (default: 1)"
        required: false
        schema:
          type: integer
          default: 1
      - name: per_page
        in: query
        description: "Number of records per page (default: 10)"
        required: false
        schema:
          type: integer
          default: 10
    responses:
      200:
        description: A list of persons
        content:
          application/json:
            schema:
              type: object
              properties:
                total:
                  type: integer
                  description: Total number of persons
                pages:
                  type: integer
                  description: Total number of pages
                persons:
                  type: array
                  items:
                    type: object
                    properties:
                      id:
                        type: integer
                        description: Person ID
                      first_name:
                        type: string
                        description: First name
                      last_name:
                        type: string
                        description: Last name
                      mobile:
                        type: string
                        description: Mobile number
                      email:
                        type: string
                        description: Email address
    """

    query = Person.query

    # Filtering 
    if "filter[name]" in request.args:
        filter_value = request.args.get("filter[name]", "")
        query = query.filter(
          or_(
              Person.first_name.ilike(f"%{filter_value}%"),
              Person.last_name.ilike(f"%{filter_value}%"),
              Person.email.ilike(f"%{filter_value}%")
          )
        )
    if "query" in request.args:
        query_value = request.args.get("query", "")
        query = query.filter(
          or_(
              Person.first_name.ilike(f"%{query_value}%"),
              Person.last_name.ilike(f"%{query_value}%"),
              Person.email.ilike(f"%{query_value}%"),
              Person.gst.ilike(f"%{query_value}%"),
              Person.mobile.ilike(f"%{query_value}%"),
          )
        )
            
    if "mobile" in request.args:
        query = query.filter(Person.mobile.ilike(f"%{request.args['mobile']}%"))

    if "person_type" in request.args:
        value = request.args['person_type']
        person_type = int(request.args['person_type'])
        query = query.filter(Person.person_type_id == person_type)

    # Sorting
    sort = request.args.get("sort", "id")
    for field in sort.split(","):
        if field.startswith("-"):
            query = query.order_by(db.desc(getattr(Person, field[1:], "id")))
        else:
            query = query.order_by(getattr(Person, field, "id"))

    # Pagination
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("items_per_page", 10))
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    persons = pagination.items

    result = [
        {
            "id": person.id,
            "first_name": person.first_name,
            "last_name": person.last_name,
            "mobile": person.mobile,
            "email": person.email,
            "gst": person.gst,
            "person_type": person.person_type.name,
        }
        for person in persons
    ]
    return jsonify({"pages": pagination.pages, "data": result , "pagination": { "total" : pagination.total}})


@person_blueprint.route("/", methods=["POST"])
def create_person():
    """
    Create a new person.
    """
    data = request.json

    # Validate person type
    person_type = PersonType.query.filter_by(id=data.get("person_type_id")).first()
    if not person_type:
        return jsonify({"error": "Invalid person type"}), 400

    # Create person
    person = Person(
        first_name=data["first_name"],
        last_name=data["last_name"],
        mobile=data["mobile"],
        email=data["email"],
        gst=data.get("gst"),
        person_type_id=data["person_type_id"],
    )
    db.session.add(person)
    db.session.commit()

    return jsonify({"message": "Person created successfully", "id": person.id}), 201


@person_blueprint.route("/<int:person_id>", methods=["PUT"])
def update_person(person_id):
    """
    Update an existing person's details.
    """
    data = request.json

    # Fetch person
    person = Person.query.get_or_404(person_id)

    # Update fields
    person.first_name = data.get("first_name", person.first_name)
    person.last_name = data.get("last_name", person.last_name)
    person.mobile = data.get("mobile", person.mobile)
    person.email = data.get("email", person.email)
    person.gst = data.get("gst", person.gst)
    person_type_id = data.get("person_type_id")
    if person_type_id:
        person_type = PersonType.query.filter_by(id=person_type_id).first()
        if not person_type:
            return jsonify({"error": "Invalid person type"}), 400
        person.person_type_id = person_type_id

    db.session.commit()
    return jsonify({"message": "Person updated successfully"})

@person_blueprint.route("/<int:person_id>", methods=["DELETE"])
def delete_person(person_id):
    """
    Delete a person by ID.
    """
    person = Person.query.get_or_404(person_id)
    db.session.delete(person)
    db.session.commit()

    return jsonify({"message": "Person deleted successfully"})
