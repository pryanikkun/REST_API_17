from flask import request
from flask_restx import Resource, Namespace
from app.database import db
from app.models import Director, DirectorSchema

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = db.session.query(Director).all()
        return directors_schema.dump(all_directors)

    def post(self):
        req_json = request.json
        new_director = Director(**req_json)
        db.session.add(new_director)
        db.session.commit()
        return '', 201


@director_ns.route('/<int:nid>')
class DirectorView(Resource):
    def get(self, nid):
        director = db.session.query(Director).get(nid)
        return director_schema.dump(director)

    def put(self, nid: int):
        director = db.session.query(Director).get(nid)
        req_json = request.json
        director.name = req_json.get("name")
        db.session.add(director)
        db.session.commit()
        return '', 201

    def delete(self, nid: int):
        director = db.session.query(Director).get(nid)
        db.session.delete(director)
        db.session.commit()
        return '', 204
