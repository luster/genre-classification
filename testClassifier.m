function [classified,ds] = testClassifier(g, classifier)
% g is a struct with name and files fields
% classifier is a trained classifier

ds = prtDataSetClass;
nGenre = length(g);

classNames = cell(1,nGenre);
features = [];
labels = [];

for ii=1:nGenre
    nFiles = length(g(ii).files);
    classNames{ii} = {ii-1,g(ii).name};
    for jj=1:nFiles
        features = [features; g(ii).files(jj).features];
        labels = [labels; ii-1];
    end
end

ds = ds.setClassNames(classNames);
ds.data = features;
ds.targets = labels;

zmuv = prtPreProcZmuv;
zmuv = zmuv.train(ds);
ds = zmuv.run(ds);

classified = run(classifier,ds);

end