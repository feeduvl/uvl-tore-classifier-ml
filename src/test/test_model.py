from src.classifier.classifier import classify

import unittest
import os


class TestClassifier(unittest.TestCase):
    
    def setUp(self) -> None:
        java_path = 'C:/Program Files/Java/jre1.8.0_331/bin'
        os.environ['JAVAHOME'] = java_path
        pass

    def test_classifier(self):
        test_string = 'Is there any extension I can add to chrome which gives a warning before closing all tabs in the window by mistake'

        print(classify(test_string))


if __name__ == '__main__':
    unittest.main()
    