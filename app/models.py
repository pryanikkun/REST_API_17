from app.database import db
from marshmallow import Schema, fields


class Movie(db.Model):
    __tablename__ = 'movie'

    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.pk'))
    director_id = db.Column(db.Integer, db.ForeignKey('director.pk'))
    pk = db.Column(db.Integer, primary_key=True)


class MovieSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
    pk = fields.Int(dump_only=True)


class Genre(db.Model):
    __tablename__ = 'genre'

    name = db.Column(db.String)
    pk = db.Column(db.Integer, primary_key=True)


class GenreSchema(Schema):
    name = fields.Str()
    pk = fields.Int(dump_only=True)


class Director(db.Model):
    __tablename__ = 'director'

    name = db.Column(db.String)
    pk = db.Column(db.Integer, primary_key=True)


class DirectorSchema(Schema):
    name = fields.Str()
    pk = fields.Int(dump_only=True)
