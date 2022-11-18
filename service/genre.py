from dao.genre import GenreDAO

class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        movies = self.dao.get_all()
        return movies

    def create(self, director_d):
        return self.dao.create(director_d)

    def update(self, director_d):
        self.dao.update(director_d)
        return self.dao

    def delete(self,director_d):
        self.dao.delete(director_d)