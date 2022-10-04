from database.postgres import DatabasePostgres
from libs.tmdb import Tmdb
import re

ponctuation = [',', '.', ':', '\'', '"', '-', "'", "’"]

def create_obstructed_plot(plot):
    data = []
    for word in plot:
        skip = False
        for i in ponctuation:
            if i in word.get('word'):
                skip = True
                data.append({"id": word.get('id'), "word": word.get('word')})
        if not skip: 
            w = ''
            for _ in word.get('word'):
                w += "\u00A0"
            data.append({"id": word.get('id'), "word": w})
    return data

def create_non_obstructed_plot(plot):
    data = []
    rgx = re.compile("([\s,.;\-\'\’:\(\)]+)")
    caca = rgx.split(plot)
    for index, i in enumerate(caca):
        if (i == " "):
            del caca[index]
    for index, word in enumerate(caca):
        data.append({"id": index, "word": word})
    return data

def create_today_plot():
    db = DatabasePostgres()
    tmdb_instance = Tmdb()
    plot = tmdb_instance.get_plot(1865)
    plot["plot_non_obsucred"] = create_non_obstructed_plot(plot.get("plot"))
    plot["plot_obsucred"] = create_obstructed_plot(plot["plot_non_obsucred"])
    plot["title_non_obsucred"] = create_non_obstructed_plot(plot.get("title"))
    plot["title_obsucred"] = create_obstructed_plot(plot["title_non_obsucred"])
    db.create_plot(plot)
    del db