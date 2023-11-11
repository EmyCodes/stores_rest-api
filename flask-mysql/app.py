#!/usr/bin/python3

from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
# from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

from db import username, host, password, database

app = Flask(__name__)
db_uri = f'mysql+pymysql://{username}:{password}@{host}/{database}'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)


class Author(db.Model):
    """
    Starting our to create an author database application
    which will provide RESTful CRUD APIs
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    specialisation = db.Column(db.String(50))

    def __init__(self, name, specialisation):
        self.name = name
        self.specialisation = specialisation

    def __repr__(self):
        return f"Product {self.id}"

# class AuthorSchema(ModelSchema)
class AuthorSchema(SQLAlchemyAutoSchema):
	"""
	class serves JSON response from our API
	using the data returned by SQLAlchemy
	"""
	# class Meta(ModelSchema.Meta)
	class Meta(SQLAlchemyAutoSchema):
		model = Author
	sqla_session = db.session

	id = fields.Number(dump_only=True)
	name = fields.String(required=True)
	specialisation = fields.String(required=True)


@app.route("/authors", methods = ["GET"])
def index():
	get_authors = Author.query.all()
	author_schema = AuthorSchema(many=True)
	# authors, error = author_schema.dump(get_authors)
	authors = author_schema.dump(get_authors)
	return make_response(jsonify({"authors": authors}))


if __name__ == "__main__":
	with app.app_context():
		db.create_all()
	app.run(debug=True)
