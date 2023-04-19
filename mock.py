import string
import random

from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/", methods=["POST"])
def process():
    genes = request.json["genes"]
    algo = request.json["prioritiser"]
    results = []

    for gene in genes:
        results.append({
            "geneId": gene,
            "geneSymbol": ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(5)),
            "score": random.random() * 10,
            "priorityType": algo.upper(),
        })

    return jsonify({"results": results})