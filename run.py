from flask import Flask, jsonify, request, render_template,send_file,send_from_directory
from app.controllers import classification
import json
import numpy as np
import sys
from app.json_encoder import myJSONEncoder

_app = Flask(__name__)
_app.json_encoder = myJSONEncoder


@_app.route('/')
def index():
    return render_template("index.html")

@_app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@_app.route('/leadranking_manufactor', methods=['POST'])
def lead_ranking():
    try:
        _data=request.json
        print("JSON DATA printing ------\n")
        print(_data)

        # case = 1, classification
        # case = 2, regression
        
        _prob, _cls, _id = classfication.lead_ranking(_data)

        # randomize the probability for demo purpose
        if(_cls == 'N'):
            _prob= float(np.random.uniform(0,0.5,(1,1)))
        else:
            _prob = float(np.random.uniform(0.5,1,(1,1)))

        return jsonify({
            "success": True, 
            "lead_id":_id, 
            "status":200, 
            "score": _prob, 
            "class": _cls
            })
    except Exception as e:
        return jsonify({"success": False, "status":500 ,"err":e.args,})

@_app.route('/leadconversion', methods=['POST'])
def lead_conversion():
    try:
        _data=request.json
        print("JSON DATA printing ------\n")
        print(_data)

        # case = 1, classification
        # case = 2, regression

        _prob, _cls, _id = classification.lead_conversion(_data)

        # randomize the probability for demo purpose
        if(_cls == 'N'):
            _prob= float(np.random.uniform(0,0.5,(1,1)))
        else:
            _prob = float(np.random.uniform(0.5,1,(1,1)))

        return jsonify({
            "success": True,
            "lead_id":_id,
            "status":200,
            "score": _prob,
            "class": _cls
            })
    except Exception as e:
        return jsonify({"success": False, "status":500 ,"err":e.args,})

if __name__ == '__main__':
    _app.run(host="0.0.0.0", port=8089)
