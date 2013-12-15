function [classified] = testFile(filename, trained_classifier)
% given a filename and a trained classifier, returnes classified object

addpath('rastamat/');

[x,fs] = audioread(filename);
x = (x(:,1)+x(:,2))/2;

[ceps,~,~]=melfcc(x,fs);%,'numcep',20,'minfreq',0,'maxfreq',2000);
ceps = ceps';

cep_feat = mean(ceps);
covMat = cov(ceps);
features = [cep_feat, covMat(:)'];

ds = prtDataSetClass;
ds.data = features;

% zmuv = prtPreProcZmuv;
% zmuv = zmuv.train(ds);
% ds = zmuv.run(ds);

classified = run(trained_classifier,ds);

end