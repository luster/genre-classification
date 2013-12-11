function plotConf(confmat)

numClasses = size(confmat,1);
numTrue = sum(confmat);

truth = zeros(sum(numTrue),1);
for ii=0:numClasses-1
    truth(ii*numTrue(ii+1)+1:(ii+1)*numTrue(ii+1)) = ii*ones(numTrue(ii+1), 1);
end

guess = [];
for ii=1:numClasses
    for jj=1:numClasses
        guess = [guess; (jj-1)*ones(confmat(ii,jj), 1)];
    end
end

prtScoreConfusionMatrix(guess,truth);
end