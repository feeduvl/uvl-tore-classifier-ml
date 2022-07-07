
from src.classifier.classifier import Classifier

class RequestHandler:
    
    def __init__(self, logger, annotation_handler) -> None:
        self.logger = logger
        self.annotation_handler = annotation_handler

    def process(self, documents, create = False):
        self.logger.info(f'Start classification of dataset')

        annotated_docs = []
        classifier = Classifier()
        for document in documents:
            annotated_docs += classifier.annotate(document["text"])
        
        self.logger.info(f'Finished classification')
        self.logger.info(annotated_docs) # remove later

        self.annotation_handler.initialize()
        self.annotation_handler.get()
        self.annotation_handler.add_tokens(annotated_docs)

        if create:
            self.annotation_handler.store()
        
        return self.annotation_handler.get_data()


    