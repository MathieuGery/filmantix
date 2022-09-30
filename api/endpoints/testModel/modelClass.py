import spacy
from database.postgres import DatabasePostgres


db = DatabasePostgres()

class Model:
    def __init__(self):
        self.nlp = spacy.load('fr_core_news_lg')
        self.update()
        
    @property
    def tokens(self):
        plot = self.dbPlot
        if plot.get('to_char') != self.day:
            self.update(plot)
        return  self._tokens, self.words
    
    def update(self, pPlot = None):
        plot = pPplot if pPlot else self.dbPlot
        self.day = plot.get('to_char')
        self._tokens = self.nlp(plot.get('plot_non_obsucred'))
        self.deleteCopy()
        print(self.words.keys())

    def deleteCopy(self):
        self.words = {}
        for i, word in enumerate(self._tokens):
            word = str(word)
            if word in self.words:
                self.words[word].append(i)
            else :
                self.words[word] = [i]
    
    @property
    def dbPlot(self):
        return db.get_last_plot()


# words = {
    # key: value
    # word: [indices]
# }