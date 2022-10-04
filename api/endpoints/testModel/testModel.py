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
        title = request.json.get("title")
        compare = model.nlp(word)

        data = [{
            w : {
                float(max(tokens[words[w][0]].similarity(compare), w == word)): [ words[w] ] 
             }
        } for w in words
        ]

        # A mettre dans une petit methode
        res = {"score": [], "word": word, "title": []}
        # Check if the word exist
        check = 0
        for item in data:
            key = list(item.keys())[0]
            value = item.get(key)
            percent = list(value.keys())[0]
            if(percent == 0):
                check += 1
        if (len(data) == check):
            return {"score": "Incorect word"}, 404
        for item in data:
            key = list(item.keys())[0]
            value = item.get(key)
            percent = list(value.keys())[0]
            for w in model.plot_non_obsucred:
                if (w.get("word").lower() == key):
                    if (percent == 1.0):
                        res.get("score").append({"id": w.get("id"), "value": percent * 100, "word": w.get("word")})
                    else:
                        res.get("score").append({"id": w.get("id"), "value": percent * 100, "word": word})
        ## Check title
        for index, w in enumerate(model.title_non_obsucred):
            if (word == w.get("word").lower()):
                res.get("title").append({"id": w.get("id"), "value": 100, "word": w.get("word")})
            else:
                res.get("title").append({"id": w.get("id"), "value": title[index].get("value"), "word": title[index].get("guess")})
        
        ##check victory
        count = 0
        for index, w in enumerate(model.title_non_obsucred):
            if (res.get("title")[index].get("word") == w.get("word")):
                count += 1
        if (count == len(model.title_non_obsucred)):
            res["victory"] = True
            return res
        return res
