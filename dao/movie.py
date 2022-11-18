from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Movie).get(uid)  # обращаемся к модели Movie и достаем поле

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director_id(self, value):
        return self.session.query(Movie).filter(Movie.director_id == value).all()

    def get_by_genre_id(self, value):
        return self.session.query(Movie).filter(Movie.genre_id == value).all()

    def get_by_year(self, value):
        return self.session.query(Movie).filter(Movie.year == value).all()

    def create(self, movie_id):
        ent = Movie(**movie_id)
        self.session.add(ent)
        self.session.commit()
        return ent

    def update(self, movie_id):
        movie = self.get_one(movie_id.get("id"))

        movie.title = movie_id.get("title")
        movie.description = movie_id.get("description")
        movie.trailer = movie_id.get("trailer")
        movie.year = movie_id.get("year")
        movie.rating = movie_id.get("rating")
        movie.genre = movie_id.get("genre_id")
        movie.director = movie_id.get("director_id")

        self.session.add(movie)
        self.session.commit()

    def delete(self, uid):
        movie = self.get_one(uid)

        self.session.delete(movie)
        self.session.commit()