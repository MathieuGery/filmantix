from flask_restplus import Resource
from libs.restplus import api_restplus
from endpoints.testModel.serializers import model_payload
from flask import request
from libs.modelClass import Model
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

        word = request.json.get("word").lower()
        compare = model.nlp(word)

        data = [{
            w : {
                float(max(tokens[words[w][0]].similarity(compare), w == word)): [ words[w] ] 
             }
        } for w in words
        ]

        # A mettre dans une petit methode
        res = {"score": []}
        for item in data:
            key = list(item.keys())[0]
            value = item.get(key)
            percent = list(value.keys())[0]
            for word in model.plot_non_obsucred:
                if (word.get("word").lower() == key):
                    if (percent == 1.0):
                        res.get("score").append({"id": word.get("id"), "value": word.get("word")})
                    else:
                        res.get("score").append({"id": word.get("id"), "value": percent,})
        return res
