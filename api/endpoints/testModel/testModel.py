from flask_restplus import Resource
from libs.restplus import api_restplus
from flask import request

import spacy

nlp = spacy.load('fr_core_news_lg')
tokens = nlp('jour nuit matin midi soir miniut')

ns = api_restplus.namespace(
    'testModel', description='Status method')

@ns.route('/')
class TestModelResources(Resource):

    def post(self):
        word = request.json.get("mabite")
        compare = nlp(word)
        print([token.similarity(compare) for token in tokens])
        return {'message': 'Status Ok'}, 200