from tmdbv3api import TMDb, Movie
# from libs.config import config

class Tmdb():
    def __init__(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = config["TMDB_KEY"]
        self.tmdb.language = 'fr'
        self.tmdb.debug = True

    def get_plot(self, id: int) -> str:
        movie = Movie()
        # recommendations = movie.recommendations(movie_id=id)
        return movie.details(id).overview
