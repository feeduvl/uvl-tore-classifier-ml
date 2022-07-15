
import unittest
import os

import sys
sys.path.append("..")
from src.classifier.classifier import Classifier
from src.utility.annotation_handler import AnnotationHandler
from src.flask_setup.request_handler import RequestHandler

class MockLogger:
    def info(self, text):
        pass

class MockResponse:
    status_code = 200

    def json(self):
        json = {
            "uploaded_at": "2022-06-16T15:11:02.573Z",
            "last_updated": "2022-07-11T15:29:20.222Z",
            "name": "tore_training_data_annotated",
            "dataset": "tore_training_data",
            "docs": [],
            "tokens": [
                {
                    "index": 0,
                    "name": "Chrome",
                    "lemma": "chrome",
                    "pos": "n",
                    "num_name_codes": 0,
                    "num_tore_codes": 0
                },
                {
                    "index": 1,
                    "name": "double",
                    "lemma": "double",
                    "pos": "a",
                    "num_name_codes": 0,
                    "num_tore_codes": 0
                },
                {
                    "index": 2,
                    "name": "click",
                    "lemma": "click",
                    "pos": "n",
                    "num_name_codes": 0,
                    "num_tore_codes": 0
                },
                {
                    "index": 3,
                    "name": "bug",
                    "lemma": "bug",
                    "pos": "n",
                    "num_name_codes": 0,
                    "num_tore_codes": 0
                }
            ],
            "codes": [],
            "tore_relationships": []
        }
        return json

class MockRequestHandler:
    def get(self, http):
        return MockResponse()

    def post(self, http, json):
        return MockResponse()


class TestClassifier(unittest.TestCase):
    
    def setUp(self) -> None:
        self.mock_logger = MockLogger()

        java_path = 'C:/Program Files/Java/jre1.8.0_331/bin'
        os.environ['JAVAHOME'] = java_path
        pass

    def test_classifier(self):
        document = {"text":'Is there any extension I can add to chrome which gives a warning before closing all tabs in the window by mistake'}

        annotation_handler = AnnotationHandler('test_annotation', 'dataset_name', self.mock_logger)
        request_handler = RequestHandler(self.mock_logger, annotation_handler)
        codes = request_handler.process([document])

        self.assertEquals(codes[0]["name"], 'extension')
        self.assertEquals(codes[0]["tore"], 'Software')

        self.assertEquals(codes[1]["name"], 'add')
        self.assertEquals(codes[1]["tore"], 'Interaction')

        self.assertEquals(codes[2]["name"], 'chrome')
        self.assertEquals(codes[2]["tore"], 'Software')
        
        self.assertEquals(codes[3]["name"], 'tabs')
        self.assertEquals(codes[3]["tore"], 'Workspace')
        
        self.assertEquals(codes[4]["name"], 'window')
        self.assertEquals(codes[4]["tore"], 'Workspace')
        
        pass

    def test_classifier_with_annotation(self):
        document = {"text":'Chrome double click bug'}

        annotation_handler = AnnotationHandler('test_annotation', 'dataset_name', self.mock_logger, MockRequestHandler())
        request_handler = RequestHandler(self.mock_logger, annotation_handler)
        codes = request_handler.process([document], create=True)
        pass

if __name__ == '__main__':
    unittest.main()
    