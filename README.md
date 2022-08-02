# uvl-tore-classifier-ml

This service is responsible for the ML TORE classification that is part of Feed.UVL's detection tools. The classification uses Stanford NER and a custom model trained for TORE classification.

## Using a new model 

The Stanford NER classifier uses a pre-trained model for classification which has to be available to the classifier at runtime. To use a new model, the current model at /ner/classifiers/ has to be replaced by the new model. Additionally, the call to the Stanford NER function in /src/classifier/classifier.py  has to adapted.

## Training a new model

Stanford NER models can be trained on a local machine using the following commands.

Training the new model on a Windows machine:

`java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop ner_training.prop`

The option `-Xmx3744M` can be added if Java runs out of memory. Using the ner_training.prop file from the repository, the file with the trainig data has to be tab-separated and named 'tore_training_for_SNER.txt'.
