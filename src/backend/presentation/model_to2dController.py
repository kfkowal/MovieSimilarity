from flask import Blueprint, jsonify, request
import json
import requests
import concurrent.futures
import typing
from service.model_to_2dService import ModelTo2D

bp = Blueprint('map', __name__, url_prefix='/')
titles=[]
with open("./tytuly.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if line.strip() !="":
            titles.append(line.strip())

cache = {}
@bp.route('/', methods=['GET'])
def Model_to_2d_Controller():

    number_of_topics     = int(request.args.get("topics"))
    create_new_model = str(request.args.get("new")).lower()
    check = cache.get(number_of_topics)

    resp = None
    if check == None:
        model = ModelTo2D(number_of_topics)
        resp = model.get_2d_coordinates()
        cache[number_of_topics] = resp
    elif create_new_model == 'false' or 'none':
        resp = cache[number_of_topics]
    else:
        model = ModelTo2D(number_of_topics)
        resp = model.get_2d_coordinates()
        cache[number_of_topics] = resp

    resp['titles'] = titles
    return jsonify(resp)
