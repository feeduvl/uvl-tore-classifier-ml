from flask import request, json, jsonify

from src.flask_setup import app
from src.utility.annotation_handler import AnnotationHandler
from src.flask_setup.request_handler import RequestHandler

"""
Concept:
  initialize new annotation for selected dataset
    POST /hitec/orchestration/concepts/annotationinit/ with {name: "{name_anno}", dataset: ""}
  GET new annotation json from database
    /hitec/repository/concepts/annotation/name/{name_anno}
  insert data about codes
  insert tokens
  write to DB
    POST hitec/repository/concepts/store/annotation/ with JSON from GET
"""

@app.route('/hitec/classify/concepts/stanford-ner/run', methods=['POST'])
def classify_tore():

    app.logger.info('Stanford NER Classification run requested')

    content = json.loads(request.data.decode('utf-8'))

    documents = content["dataset"]["documents"]
    dataset_name = content["dataset"]["name"]
    annotation_name = content["params"]["annotation_name"]
    create = content["params"]["create"]

    annotation_handler = AnnotationHandler(annotation_name, dataset_name, app.logger)
    request_handler = RequestHandler(app.logger, annotation_handler)
    result = request_handler.process(documents, create)

    return 'OK'

@app.route('/hitec/classify/concepts/stanford-ner/status', methods=["GET"])
def get_status():
    status = {
        "status": "operational",
    }

    return jsonify(status)

