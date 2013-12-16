clear all
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

% genres = {'classical'; 'rock'; 'k-pop'; 'country'; 'jazz'; 'pop'; ...
%                   'techno'; 'opera'};
                
genres = {'classical' ; 'rock' ; 'jazz' ; 'pop'};
                
genres_str = regexprep(strjoin(sort(genres).'), ' ', '_');
classifier_filename = sprintf('%s.mat', genres_str);

if exist(fullfile(cd, classifier_filename), 'file') ~= 2
  
  genreTraining = [];
  genreTesting = [];

  for ii=1:length(trainData)
    if strmatch(trainData(ii).name, genres)
      genreTraining = [ genreTraining, trainData(ii)];
      genreTesting = [ genreTesting, testData(ii)];
    end
  end

  trainData = addCovFeature(genreTraining);
  testData = addCovFeature(genreTesting);

  classifier = prtClassMatlabTreeBagger;
  classifier.nTrees = 2000;
  % classifier = prtClassBinaryToMaryOneVsAll;

  % baseClassifier = prtClassNnet;
  % classifier = prtClassBinaryToMaryOneVsAll;
  % classifier.baseClassifier = prtClassAdaBoost;
  % baseClassifier = prtClassRvm;
  % baseClassifier.kernels.kernelCell{2}.sigma = 10;

  % classifier.baseClassifier = baseClassifier;
  % classifier.baseClassifier = prtClassLibSvm;
  classifier.internalDecider = prtDecisionMap;

  [classifier,tawf] = trainClassifier(trainData, classifier);
  
  save(classifier_filename, 'classifier');
else
  load(classifier_filename)
end

[classified,ds] = testClassifier(testData, classifier);

prtScoreConfusionMatrix(classified,ds)

% confMat = prtScoreConfusionMatrix(guess,classified.targets)
% percent = sum(diag(confMat)/sum(confMat(:)))