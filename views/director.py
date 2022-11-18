
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema #импортируем модель
from implemented import director_service

director_ns = Namespace("directors")

@director_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        objects = director_service.get_all()
        result = DirectorSchema(many = True).dump(objects)
        return result, 200

@director_ns.route("/<int:uid>")
class DirectorView(Resource):
    def get(self, uid):
        object = director_service.get_one(uid)
        result = DirectorSchema().dump(object)
        return result, 200



