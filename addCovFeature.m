function gout = addCovFeature(g)

for ii=1:length(g)
    nFiles = length(g(ii).files);
    for jj=1:nFiles
        datMat = cov(g(ii).files(jj).ceps);
        newFeat = [g(ii).files(jj).features, datMat(:)'];
        g(ii).files(jj).features = newFeat;
    end
end

gout = g;

end