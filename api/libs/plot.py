def create_obstructed_plot(plot):
    data = []
    for index, word in enumerate(plot.split(" ")):
        w = ""
        for i in range (0, len(word)):
            w += " "
        data.append({"id": index, "word": w})
    return data