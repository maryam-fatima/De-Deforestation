# Example6: use pyAudioAnalysis wrapper 
# to extract feature and train SVM classifier 
# for 20 music (10 classical/10 metal) song samples
from pyAudioAnalysis.audioTrainTest import extract_features_and_train
chdir("/content/gdrive/MyDrive/project_folder/Wood cutting sound")

mt, st = 1.0, 0.05
#dirs = ["data/chainsaw", "data/axe", "data/random"]
dirs = ["Training_data\ambiguous sound", "Training_data\axe cutting sound", "Training_data\back_ground noise", "Training_data\chainsaw cutting sound", "Training_data\manual saw cutting sound", "Training_data\tree breaking sound"] 
extract_features_and_train(dirs, mt, mt, st, st, "svm", "svm_deforest")
