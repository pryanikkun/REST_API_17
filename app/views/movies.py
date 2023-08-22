from flask import request
from flask_restx import Resource, Namespace
from app.database import db
from app.models import Movie, MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        req_dir = request.args.get("director_id")
        req_genre = request.args.get("genre_id")
        t = db.session.query(Movie)
        if req_dir:
            t = t.filter(Movie.director_id == req_dir)
        if req_genre:
            t = t.filter(Movie.genre_id == req_genre)
        all_movies = t.all()
        return movies_schema.dump(all_movies)

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)
        db.session.add(new_movie)
        db.session.commit()
        return '', 201


@movie_ns.route('/<int:nid>')
class MovieView(Resource):
    def get(self, nid: int):
        movie = db.session.query(Movie).get(nid)
        return movie_schema.dump(movie)

    def put(self, nid: int):
        movie = db.session.query(Movie).get(nid)
        req_json = request.json

        movie.title = req_json.get("title")
        movie.description = req_json.get("description")
        movie.trailer = req_json.get("trailer")
        movie.year = req_json.get("year")
        movie.rating = req_json.get("rating")
        movie.genre_id = req_json.get("genre_id")
        movie.director_id = req_json.get("director_id")

        db.session.add(movie)
        db.session.commit()
        return "", 201

    def delete(self, nid: int):
        movie = db.session.query(Movie).get(nid)
        db.session.delete(movie)
        db.session.commit()
        return "", 204
