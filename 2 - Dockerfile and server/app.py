from flask import Flask, request, jsonify
from joblib import load
import requests
import os
from os import getcwd


def model(v):
	url = "https://raw.github.com/nuttka/ml_model_americantweet/main/v" + v + ".joblib"
	file = getcwd() + "/v" + v + ".joblib"
	res = requests.get(url)
	open(file, 'wb').write(res.content)
	return load("v" + v + ".joblib")


m_version = os.environ.get('MODEL_VERSION')

clf = model(m_version)

app = Flask(__name__)

@app.route("/api/american", methods=["POST"])
def isAmerican():
	data = request.get_json(force=True)
	res = clf.predict([data['text']])
	
	return jsonify({
        	"is_american": str(res[0]),
		"version": str(m_version),
		"model_date": "22/06/2022"
    	})
