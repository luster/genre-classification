% clear all
close all
clc

if exist(fullfile(cd, 'data.mat'), 'file') ~= 2
  fprintf('Loading training data.\n');
  trainData = loadData('training');
  fprintf('Loaded train data.\nLoading test data.\n');
  testData = loadData('testing');
  fprintf('Loaded test data.\nAdding covariance features.\n');
  save('data.mat','trainData','testData');
else
  load data.mat
end

trainData = addCovFeature(trainData);
testData = addCovFeature(testData);

[classifier,tawf] = trainClassifier(trainData);
[classified,ds] = testClassifier(testData,classifier);

prtScoreConfusionMatrix(classified,ds)

% confMat = prtScoreConfusionMatrix(guess,classified.targets)
% percent = sum(diag(confMat)/sum(confMat(:)))