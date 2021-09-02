# Example6: use pyAudioAnalysis wrapper 
# to extract feature and train SVM classifier 
# for 20 music (10 classical/10 metal) song samples
from pyAudioAnalysis.audioTrainTest import extract_features_and_train
mt, st = 1.0, 0.05
dirs = ["data/chainsaw", "data/axe", "data/random"] 
extract_features_and_train(dirs, mt, mt, st, st, "svm_rbf", "svm_deforest")
