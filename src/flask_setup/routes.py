from flask import Flask, request
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

from src.flask_setup import app

#import os
#java_path = 'C:/Program Files/Java/jre1.8.0_331/bin'
#os.environ['JAVAHOME'] = java_path



@app.route('/hitec/tore/classify_ml', methods=['POST'])
def classify_tore():

    st = StanfordNERTagger('ner/classifiers/english.all.3class.distsim.crf.ser.gz',
                        'ner/stanford-ner.jar',
                        encoding='utf-8')

    text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'

    tokenized_text = word_tokenize(text)
    classified_text = st.tag(tokenized_text)

    print(classified_text)
    app.logger.info('OK')

    return 'OK'