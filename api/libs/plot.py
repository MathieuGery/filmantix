from database.postgres import DatabasePostgres
from libs.tmdb import Tmdb
import re

def create_obstructed_plot(plot):
    data = []
    for index, word in enumerate(plot):
        for i in range(0, len(word)):
            w += "\u00A0"
        data.append({"id": index, "word": w})
    return data

def create_non_obstructed_plot(plot):
    data = []
    rgx = re.compile("([\s,.;\-\':\(\)]+)")
    caca = rgx.split(plot)
    for index, i in enumerate(caca):
        if (i == " "):
            del caca[index]
    for index, word in enumerate(caca):
        data.append({"id": index, "word": word})
    print(data)
    return data

def create_today_plot():
    db = DatabasePostgres()
    tmdb_instance = Tmdb()
    plot = tmdb_instance.get_plot(1416)
    plot["plot_non_obsucred"] = create_non_obstructed_plot(plot.get("plot"))
    plot["plot_obsucred"] = create_obstructed_plot(plot["plot_non_obsucred"])
    db.create_plot(plot)
    del db
    return