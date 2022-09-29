from flask_restplus import Resource
from libs.restplus import api_restplus
from endpoints.testModel.serializers import model_payload
from flask import request
from tmp import get_plot, deleteCopy
# from colorama import Fore, init
# init(autoreset=True)

import spacy

nlp = spacy.load('fr_core_news_lg')
plot = get_plot(185) #matrix
print("ijqiosjfs", plot)
tokens = nlp(plot)
wordCount = len(tokens)
words = deleteCopy(tokens)

print('start')

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

        return {'message': 'Status Ok',
                'similarity': [
                    {
                        w: {
                            'value': tokens[words[w][0]].similarity(compare),
                            'index': words[w]
                        } for w in words
                    }
                ], 
            'wordCount': wordCount,
            'word': word
        }