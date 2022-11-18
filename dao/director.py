from dao.model.director import Director

class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Director).get(uid)  # обращаемся к модели Director и достаем поле

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, director_id):
        ent = Director(**director_id)
        self.session.add(ent)
        self.session.commit()
        return ent

    def update(self, director_id):
        director = self.get_one(director_id.get("id"))
        director.name = director_id.get("name")

        self.session.add(director)
        self.session.commit()

    def __delete__(self, uid):
        director = self.get_one(uid)

        self.session.delete(director)
        self.session.commit()
