from flask import Blueprint, render_template, request, jsonify, make_response
from .models import (
    get_pinecone_connection,
    upload_vectors,
    query_vectors,
    delete_index,
    query_langchain
)
import pandas as pd
import numpy as np

main_blueprint = Blueprint("main", __name__)
pc = get_pinecone_connection()


@main_blueprint.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # return render_template("index.html", data=data)
        return "<h1>ELLO</h1>"
    else:
        return "<h1>404: POST method doesn't exist</h1>"


@main_blueprint.route("/uploadVectors", methods=["GET"])
def upload_vectors_route():
    upload_vectors(pc)
    return "<h1>Vectors uploaded!</h1>"

@main_blueprint.route("/queryVectors", methods=["POST"])
def query_vectors_route():
    json_data = request.get_json()
    query_string = json_data["queryString"]
    results = query_vectors(pc, query_string)
    return jsonify(data=results)

@main_blueprint.route("/queryLangchain", methods=["POST"])
def query_langchain_route():
    json_data = request.get_json()
    vector = json_data["vector"]
    results = query_langchain(vector)
    return jsonify(data=results)

@main_blueprint.route("/deleteIndex", methods=["GET"])
def delete_index_route():
    delete_index(pc)
    return "<h1>Index deleted!</h1>"