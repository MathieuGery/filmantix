from flask_restplus import Resource
from libs.restplus import api_restplus
from endpoints.testModel.serializers import model_payload
from flask import request
from tmp import get_plot
# from colorama import Fore, init
# init(autoreset=True)

import spacy

# print(Fore.GREEN + 'loading model')
nlp = spacy.load('fr_core_news_lg')
# print(Fore.GREEN + 'loaded model')

plot, worldCount = get_plot('0133093') #matrix

# print(Fore.GREEN + 'parsing text')
tokens = nlp(plot)
# print(Fore.GREEN + 'text parsed')

ns = api_restplus.namespace(
    'testModel', description='Status method')

@ns.route('/')
class TestModelResources(Resource):
    @api_restplus.expect(model_payload)
    def post(self):
        word = request.json.get("word")
        compare = nlp(word)

        if not compare.has_vector:
            return {'message': 'no vector'}, 400

        return {'message': 'Status Ok' , 'similarity': [
                {str(token): token.similarity(compare) for token in tokens}
            ],
            'worldCount': worldCount}, 200,