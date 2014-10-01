# genre-classification

Ethan Lusterman & Robert Gruener  
Department of Electrical Engineering, The Cooper Union  
ECE414 Machine Learning, Fall 2013, Advisor: Sam Keene  

This project collects and uses 30-second preview, genre-labeled raw audio data from echonest's API to train a prt (pattern recognition toolbox) classifier in MATLAB and then test it. Feature extraction is accomplished using Mel Frequency Cepstral Coefficients (MFCCs), and the default classifier used is a Treebagger `(prtClassMatlabTreebagger)`. Testing of the classifier in MATLAB outputs a confusion matrix with overall percentage displayed `(prtScoreConfusionMatrix)`. The front-end is written in Flask for uploading and testing of single audio files with visual output. Due to time constraints, the back-end uses a wrapper that allows MATLAB functions to be called from within Python `(mlabwrap)`.

## Dependencies

### Python
```
pydub
pyechonest
numpy
```

### MATLAB
```
newfolder/PRT (https://github.com/newfolder/PRT)
rastamat (http://labrosa.ee.columbia.edu/matlab/rastamat/)
```

## Example Usage

1. Rename `SAMPLE_CONFIG` to `CONFIG.py` and add your echonest API key data.
2. `python echonest.py` to collect training and testing data
3. Open MATLAB and run `butRunThisScriptDoe.m` to load the data into MATLAB and train and test the classifier.
4. Modify the feature collection in `loadData.m` if desired.
5. Test classifier on single files in MATLAB using `testFile.m`.
