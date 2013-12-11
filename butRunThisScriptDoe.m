clear all
close all
clc

fprintf('Loading training data.\n');
% trainData = loadData('training');
% fprintf('Loaded train data.\nLoading test data.\n');
% testData = loadData('testing');
% fprintf('Loaded test data.\nAdding covariance features.\n');

load data.mat
% load paperDataReal.mat

trainData = addCovFeature(trainData);
testData = addCovFeature(testData);

classifier = trainClassifier(trainData);
[classified,ds] = testClassifier(testData,classifier);

% [~,guess] = max(classified.data,[],2);
% prtScoreConfusionMatrix(classified,ds);

% confMat = prtScoreConfusionMatrix(guess,classified.targets)
% percent = sum(diag(confMat)/sum(confMat(:)))