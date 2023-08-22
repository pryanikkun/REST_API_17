from flask import Flask
from flask_restx import Api
from data import data
from app.config import Config
from app.database import db
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns
from app.models import Movie, Genre, Director


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 4}
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


def load_data():
    db.drop_all()
    db.create_all()

    movies_list = data['movies']
    list_m_objects = []
    for movie in movies_list:
        list_m_objects.append(Movie(**movie))

    genres_list = data['genres']
    list_g_objects = []
    for genre in genres_list:
        list_g_objects.append(Genre(**genre))

    directors_list = data['directors']
    list_d_objects = []
    for director in directors_list:
        list_d_objects.append(Director(**director))

    with db.session.begin():
        db.session.add_all(list_m_objects)
        db.session.add_all(list_d_objects)
        db.session.add_all(list_g_objects)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)

    configure_app(app)
    load_data()

    app.run()
