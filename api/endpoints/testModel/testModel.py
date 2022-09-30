from flask_restplus import Resource
from libs.restplus import api_restplus
from endpoints.testModel.serializers import model_payload
from flask import request
from endpoints.testModel.modelClass import Model
# from colorama import Fore, init
# init(autoreset=True)



ns = api_restplus.namespace(
    'testModel', description='Status method')

model = Model()
print('start')

@ns.route('/')
class TestModelResources(Resource):
    @api_restplus.expect(model_payload)
    def post(self):
        tokens, words = model.tokens #tokens == nlp tokens; words == dict unique tokens cf bottom modelClass.

        word = request.json.get("word")
        compare = model.nlp(word)

        if not compare.has_vector:
            return {'message': 'no vector'}, 400

        return {
            tokens[words[w][0]].similarity(compare): [ words[w] ] for w in words
        }