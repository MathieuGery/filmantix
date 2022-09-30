
from tmdbv3api import TMDb, Movie
from libs.config import config

class Tmdb():
    def __init__(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = config["TMDB_KEY"]
        self.tmdb.language = "fr"
        self.tmdb.debug = True

    def __get_directing(self, crew):
        for crewmate in crew:
            if (crewmate.get("known_for_department").lower() == "directing"):
                return crewmate.get("name")
        return ""

    def get_plot(self, id: int) -> str:
        movie = Movie()
        res = {
            "link": f"https://www.themoviedb.org/movie/{id}-{movie.details(id).original_title}",
            "poster": f"https://image.tmdb.org/t/p/original{movie.details(id).poster_path}",
            "title": movie.details(id).title,
            "plot": movie.details(id).overview,
            "origin_country": movie.details(id).original_language,
            "director": self.__get_directing(movie.credits(id).crew),
            "release_date": movie.details(id).release_date,
            "runtime": movie.details(id).runtime
        }
        return res
