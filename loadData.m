function g = loadData(train_or_test)
%loadTrainData loads training data into prt Dataset

addpath('rastamat/');
path_to_train_data = dir(train_or_test);
numGenres = 4;
g = struct;

for ii=1:numGenres
    g(ii).name = path_to_train_data(ii+2).name;
    str = sprintf('%s/%s',train_or_test,g(ii).name);
    d = dir(str);
    g(ii).files = d(3:end);
    for jj=3:length(d)
        sstr = sprintf('%s/%s',str,d(jj).name);
        try
            [x,fs]=audioread(sstr);
            x = (x(:,1)+x(:,2))/2;

            [ceps,~,~]=melfcc(x,fs,'numcep',20,'minfreq',0,'maxfreq',2000);
            ceps = ceps';
            ceps(:,1:13);

            cep_feat = mean(ceps);
            g(ii).files(jj-2).ceps = ceps;
            g(ii).files(jj-2).features = cep_feat;
        catch
            fprintf('Likely Corrupted File found at %s. Please delete it.', sstr);
        end
    end
end
end