function [classifier, ds]  = trainClassifier(g)
% accepts struct g with fields
%   name - genre
%   files - struct of files with feature data
%           ceps (long x 13)
%           features (1 x 13

ds = prtDataSetClass;
nGenre = length(g);

classNames = cell(1,nGenre);
features = [];
labels = [];

for ii=1:nGenre
    nFiles = length(g(ii).files);
    classNames{ii} = {ii-1,g(ii).name};
    for jj=1:nFiles
        newFeat = g(ii).files(jj).features;
        if ~any(isnan(newFeat) | isinf(newFeat))
            features = [features; newFeat];
            labels = [labels; ii-1];
        end
    end
end

ds = ds.setClassNames(classNames);
ds.data = features;
ds.targets = labels;

% zmuv = prtPreProcZmuv;
% zmuv = zmuv.train(ds);
% ds = zmuv.run(ds);

classifier = prtClassMatlabTreeBagger;
classifier.nTrees = 2000;
% classifier.nTrees = 1000;
% classifier = prtClassBinaryToMaryOneVsAll;

% baseClassifier = prtClassNnet;
% baseClassifier.kernels.kernelCell{2}.sigma = 10;

% classifier.baseClassifier = baseClassifier;
% classifier.baseClassifier = prtClassLibSvm;
classifier.internalDecider = prtDecisionMap;
classifier = classifier.train(ds);

end