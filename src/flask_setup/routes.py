from flask import request, json, jsonify

from src.flask_setup import app
from src.classifier import classifier
from src.utility.annotation_handler import AnnotationHandler

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
    app.logger.info(content)

    documents = content["dataset"]["documents"]
    dataset_name = content["dataset"]["names"]
    #annotation_name = content["params"]["annotation_name"] # this is missing in the frontend atm
    annotation_name = dataset_name + '_jw' # tmp

    for document in documents:
        app.logger.info(f'Start classification of dataset {document["id"]}') 
        annotated_docs = classifier.classify(document["text"])
    
    app.logger.info(annotated_docs) # remove later


    app.logger.info(f'Initialize annotation {annotation_name} of dataset {dataset_name}') 

    return 'OK' # debugging


    annotation_handler = AnnotationHandler(annotation_name, dataset_name)
    annotation_handler.initialize()
    annotation_handler.get()
    annotation_handler.add_tokens(annotated_docs)
    
    app.logger.info(f'Writing {annotation_name} to DB') 
    annotation_handler.store()

    return 'OK'

@app.route('/hitec/classify/concepts/stanford-ner/status', methods=["GET"])
def get_status():
    status = {
        "status": "operational",
    }

    return jsonify(status)

