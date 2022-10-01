import spacy
from database.postgres import DatabasePostgres

class Model:
    def __init__(self):
        self.db = DatabasePostgres()
        self.day = None
        self.plot_non_obsucred = None
        self.nlp = spacy.load('fr_core_news_lg')
        self.update()
        
    @property
    def tokens(self):
        plot = self.dbPlot
        if plot.get('to_char') != self.day:
            self.update(plot)
        return  self._tokens, self.words
    
    def update(self, pPlot = None):
        plot = pPlot if pPlot else self.dbPlot
        if not plot:
            return
        self.day = plot.get('to_char')
        self.plot_non_obsucred = plot.get('plot_non_obsucred')
        self._tokens = self.nlp(' '.join(items['word'] for items in plot.get('plot_non_obsucred')))
        self.deleteCopy()

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
        return self.db.get_last_plot()


# words = {
    # key: value
    # word: [indices]
# }