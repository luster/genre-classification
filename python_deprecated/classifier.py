#!ENV/bin/python -W ignore::DeprecationWarning

from sklearn import svm
from sklearn import neighbors
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from CONFIG import algorithm
from scipy.io import wavfile
from store import Store
from features import compute_mfcc, featurize
import numpy as np
import pylab as pl
import MFCC
import os
import sys

mfcc_key = 'mfcc'

class Classifier:

    def __init__(self):
        self.training_data = []
        self.training_targets = []
        self.testing_data = []
        self.testing_targets = []
        #self.classifier = neighbors.KNeighborsClassifier()
        self.classifier = svm.SVC()
        #self.classifier = DecisionTreeClassifier()
        self.db = Store()

    def add_training_data(self, data, target):
        self.training_data.append(np.array(data))
        self.training_targets.append(target)

    def add_testing_data(self, data, target):
        self.testing_data.append(np.array(data))
        self.testing_targets.append(target)

    def fit(self, scale=True):
        self.training_data = np.array(self.training_data)
        self.training_targets = np.array(self.training_targets)
        if scale:
            self.training_data = preprocessing.scale(self.training_data)
        self.classifier.fit(self.training_data, self.training_targets)

    def preprocess(self):
        self.training_data = preprocessing.scale(self.training_data)
        self.testing_data = preprocessing.scale(self.testing_data)

    def predict(self, data, scale=True):
        data = np.array(data)
        if scale:
            data = preprocessing.scale(data)
        return self.classifier.predict(data)

def main():
    classifier = Classifier()
    targets = dict()
    data = dict()
    for (i, genre) in enumerate(algorithm['genres']):
        targets[genre] = i
        targets[i] = genre
    # Get all training data
    for genre in algorithm['genres']:
        print "training", genre
        data[genre] = classifier.db.get_tracks_by_genre(genre)
        for track in data[genre][:algorithm['training_size']]:
            try:
                if mfcc_key in track:
                    mfcc = track[mfcc_key]
                else:
                    mfcc = compute_mfcc(track, classifier.db)
                feature = featurize(mfcc)
                classifier.add_training_data(feature, targets[genre])
            except Exception, e:
                print e

    print "Fitting"
    classifier.fit()
    print "Starting Classification"

    start_index = algorithm['training_size']
    prediction_data = []
    prediction_targets = list()
    for genre in algorithm['genres']:
        data[genre] = classifier.db.get_tracks_by_genre(genre)
        for track in data[genre][start_index:start_index+algorithm['testing_size']]:
            try:
                if mfcc_key in track:
                    mfcc = track[mfcc_key]
                else:
                    mfcc = compute_mfcc(track, classifier.db)
                feature = featurize(mfcc)
                prediction_data.append(feature)
                prediction_targets.append(targets[genre])
            except Exception, e:
                print e

    predictions = classifier.predict(prediction_data)

    cm = confusion_matrix(predictions, prediction_targets)

    print(cm)

    # Show confusion matrix in a separate window
    pl.matshow(cm)
    pl.title('Confusion matrix')
    pl.colorbar()
    pl.ylabel('True label')
    pl.xlabel('Predicted label')
    pl.show()

if __name__ == '__main__':
    main()
