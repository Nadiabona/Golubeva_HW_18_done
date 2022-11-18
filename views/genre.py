from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema  # импортируем модель
from implemented import genre_service

genre_ns = Namespace("genres")


@genre_ns.route("/")
class GenresView(Resource):
    def get(self):
        objects = genre_service.get_all()
        result = GenreSchema(many=True).dump(objects)
        return result, 200


@genre_ns.route("/<int:uid>")
class GenreView(Resource):
    def get(self, uid):
        object = genre_service.get_one(uid)
        result = GenreSchema().dump(object)
        return result, 200