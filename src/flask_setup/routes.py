from flask import Flask, request, json, jsonify

from src.flask_setup import app
from src.classifier import classifier


@app.route('/hitec/classify/concepts/stanford-ner/run', methods=['POST'])
def classify_tore():

    app.logger.info('Stanford NER Classification run requested')

    content = json.loads(request.data.decode('utf-8'))
    app.logger.info(content)

    dataset = content["dataset"]["documents"]

    app.logger.info(dataset)

    classified_text = classifier.classify(dataset)

    app.logger.info(classified_text)
    app.logger.info('OK')

    return 'OK'

@app.route('/hitec/classify/concepts/stanford-ner/status', methods=["GET"])
def get_status():
    status = {
        "status": "operational",
    }

    return jsonify(status)

