from tmdbv3api import TMDb, Movie
from libs.config import config
# init(autoreset=True)

tmdb = TMDb()
tmdb.api_key = config["TMDB_KEY"]
tmdb.language = 'fr'
tmdb.debug = True

def get_plot(id: int) -> str:
    movie = Movie()

    # recommendations = movie.recommendations(movie_id=id)
    print(movie.details(id).overview)
        

def deleteCopy(tab: list) -> dict:
    dic = {}
    for i, word in enumerate(tab):
        word = str(word)
        if word in dic:
            dic[word].append(i)
        else :
            dic[word] = [i]
    return dic


plot = get_plot(185) #orange mécanique