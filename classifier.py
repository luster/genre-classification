#!ENV/bin/python

from sklearn import svm
from CONFIG import algorithm
from scipy.io import wavfile
import numpy as np
import MFCC
import os
import sys

class Classifier:

    def __init__(self):
        self.training_data = []
        self.training_targets = []
        self.testing_data = []
        self.testing_targets = []
        self.classifier = svm.SVC(gamma=0.001, C=100.)

    def compute_mfcc(self, filename):
        sampleRate, signal = wavfile.read(filename)
        mfcc = MFCC.extract(signal, show=False)
        return mfcc

    def add_data(self, data, target):
        self.training_data.append(np.array(data))
        self.training_targets.append(target)

    def fit(self):
        self.training_data = np.array(self.training_data)
        self.training_targets = np.array(self.training_targets)
        self.classifier.fit(self.training_data, self.training_targets)

    def predict(self, data):
        return self.classifier.predict(np.array(data))


def main():
    classifier = Classifier()
    cur_dir = os.getcwd() + '/raw_audio/training'
    targets = dict()
    for (i, genre) in enumerate(algorithm['genres']):
        targets[genre] = i
        targets[i] = genre
    # Get all training data
    if os.path.exists(cur_dir):
        for genre in os.listdir(cur_dir):
            cur_dir_2 = cur_dir + '/' + genre
            if os.path.isdir(cur_dir_2):
                print >> sys.stderr, "Training on", genre
                num_trained = 0
                for letter in os.listdir(cur_dir_2):
                    root = cur_dir_2 + '/' + letter
                    if os.path.isdir(root):
                        for f in os.listdir(root):
                            if os.path.isfile(os.path.join(root, f)):
                                try:
                                    if num_trained < 10:
                                        mfcc = classifier.compute_mfcc(os.path.join(root, f))
                                        mfcc = np.mean(mfcc, 0)
                                        classifier.add_data(mfcc, targets[genre])
                                        num_trained += 1
                                    else:
                                        break
                                except Exception, e:
                                    print e
    classifier.fit()
    print "Starting Classification"
    cur_dir = os.getcwd() + '/raw_audio/testing'
    # Get all training data
    if os.path.exists(cur_dir):
        for genre in os.listdir(cur_dir):
            cur_dir_2 = cur_dir + '/' + genre
            if os.path.isdir(cur_dir_2):
                for letter in os.listdir(cur_dir_2):
                    root = cur_dir_2 + '/' + letter
                    if os.path.isdir(root):
                        for f in os.listdir(root):
                            if os.path.isfile(os.path.join(root, f)):
                                try:
                                    mfcc = classifier.compute_mfcc(os.path.join(root, f))
                                    mfcc = np.mean(mfcc, 0)
                                    prediction = classifier.predict(mfcc)
                                    genre_prediction = targets[prediction[0]]
                                    print >> sys.stderr, f, "Genre:", genre, "Predicted Genre:", genre_prediction
                                except Exception, e:
                                    print e

if __name__ == '__main__':
    main()
