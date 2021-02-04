""" V1.1--update for project 11"""
import json
from flask import Flask, render_template
from flask_cors import CORS
from flask import request as req
from grandpy import req_grandpy

app = Flask(__name__)
CORS(app=app)


@app.route("/")
@app.route("/index")
def index():
    """call the template and disp it"""
    return render_template("/index.html")


@app.route("/api_google/")
def req_for_api():
    """this fonction create an object for the module who make requests"""
    objet = req_grandpy()
    objet.parse(req.args.get("user_raw_text"))
    objet.search_by_google()
    objet.search_by_wiki()
    objet.search_by_openweathermap()
    dict_return = objet.search_by_wiki_bio()

    response = app.response_class(
        response=json.dumps(dict_return, ensure_ascii=False),
        status=200,
        mimetype="application/json",
    )
    return response
