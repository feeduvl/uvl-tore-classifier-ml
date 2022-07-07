from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

class Classifier:
    def annotate(self, dataset):
        st = StanfordNERTagger('ner/classifiers/tore-model.ser.gz',
                            'ner/stanford-ner.jar',
                            encoding='utf-8')

        tokenized_text = word_tokenize(dataset)
        print(tokenized_text)
        classified_text = st.tag(tokenized_text)

        return classified_text
