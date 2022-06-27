import requests

class AnnotationHandler:

    def __init__(self, annotation_name, dataset_name) -> None:
        self.annotation_name = annotation_name
        self.dataset_name = dataset_name
        self.data = None
        pass

    def initialize(self):
        """
        Initialize a new annotation in Feed.UVL.

        Arguments:
            annotation_name: Name of the new annotation
            dataset_name: Name of the dataset that will be annotated
        Returns:
            Status code of the request to Feed.UVL
        """
        annotation = {
            'name': self.annotation_name, 
            'dataset': self.dataset_name
        }
        request = requests.post('https://feed-uvl.ifi.uni-heidelberg.de/hitec/orchestration/concepts/annotationinit/', json=annotation)

        return request.status_code


    def get(self):
        """
        Get the annotation in JSON data.

        Arguments:
            annotation_name: Name of the annotation
        Returns:
            JSON that describes the annotation
        """
        request = requests.get(f'https://feed-uvl.ifi.uni-heidelberg.de/hitec/repository/concepts/annotation/name/{self.annotation_name}')
        self.data = request.json()
        pass


    def store(self):
        """
        Write the annotation to the database.

        Arguments:
            annotation_data: The deserialized JSON that contains the annotation data
        Returns:
            Status code of the request to Feed.UVL
        """
        request = requests.post('https://feed-uvl.ifi.uni-heidelberg.de/hitec/repository/concepts/store/annotation/', json=self.data)

        return request.status_code

    def add_tokens(self, annotated_docs):
        """
        Add the new tokens to the annotation JSON

        Arguments:
            annotated_docs: Full text with labels
        """
        
        code_index = 0

        for index, annotation in enumerate(annotated_docs):
            # loop at tokens 
            if annotation[1] != 'O':
                # set num_name_codes and num_tore_codes
                self.data["tokens"][index]["num_name_codes"] = 1
                self.data["tokens"][index]["num_tore_codes"] = 1
                
                # create code and append to list of codes
                code = {
                    "tokens": [
                        index
                    ],
                    "name": annotation[0],
                    "tore": annotation[1],
                    "index": code_index,
                    "relationship_memberships": []
                }

                self.data["codes"].append(code)

                code_index += 1
            else:
                continue

        pass
