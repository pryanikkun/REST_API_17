from flask import request
from flask_restx import Resource, Namespace
from app.database import db
from app.models import Genre, GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = db.session.query(Genre).all()
        return genres_schema.dump(all_genres)

    def post(self):
        req_json = request.json
        new_genre = Genre(**req_json)
        db.session.add(new_genre)
        db.session.commit()
        return '', 201


@genre_ns.route('/<int:nid>')
class GenreView(Resource):
    def get(self, nid: int):
        genre = db.session.query(Genre).get(nid)
        return genre_schema.dump(genre)

    def put(self, nid: int):
        genre = db.session.query(Genre).get(nid)
        req_json = request.json
        genre.name = req_json.get("name")

        db.session.add(genre)
        db.session.commit()
        return "", 201

    def delete(self, nid: int):
        genre = db.session.query(Genre).get(nid)
        db.session.delete(genre)
        db.session.commit()
        return "", 204
