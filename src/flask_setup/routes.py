from flask import Flask, request, json, jsonify
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

from src.flask_setup import app

#import os
#java_path = 'C:/Program Files/Java/jre1.8.0_331/bin'
#os.environ['JAVAHOME'] = java_path



@app.route('/hitec/classify/concepts/stanford-ner/run', methods=['POST'])
def classify_tore():

    app.logger.info('Stanford NER Classification run requested')

    content = json.loads(request.data.decode('utf-8'))
    app.logger.info(content)

    dataset = content["dataset"]["documents"]

    app.logger.info(dataset)


    st = StanfordNERTagger('ner/classifiers/english.all.3class.distsim.crf.ser.gz',
                        'ner/stanford-ner.jar',
                        encoding='utf-8')

    text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'

    tokenized_text = word_tokenize(text)
    classified_text = st.tag(tokenized_text)

    print(classified_text)
    app.logger.info('OK')

    return 'OK'

@app.route('/hitec/classify/concepts/stanford-ner/status', methods=["GET"])
def get_status():
    status = {
        "status": "operational",
    }

    return jsonify(status)

