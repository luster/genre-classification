%trainData = loadData('training');
%testData = loadDat('testing');
trainData = g;
testData = gtest;
classifier = trainClassifier(trainData);
classified = testClassifier(testData,classifier);
[~,guess] = max(classified.data,[],2);

confMat = prtScoreConfusionMatrix(guess,classified.targets)
percent = sum(diag(confMat)/sum(confMat(:)))