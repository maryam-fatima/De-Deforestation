# Example6: use pyAudioAnalysis wrapper 
# to extract feature and train SVM classifier 

import os
from pyAudioAnalysis.audioTrainTest import extract_features_and_train
os.chdir("/content/gdrive/MyDrive/project_folder/")

mt, st = 1.0, 0.05
#dirs = ["data/chainsaw", "data/axe", "data/random"]
#dirs = ["Training_data/ambiguous sound", "Training_data/axe cutting sound", "Training_data/back_ground noise", "Training_data/chainsaw cutting sound", "Training_data/manual saw cutting sound", "Training_data/tree breaking sound"] 
#dirs = ["Cutting/Cutting", "NonCutting/NonCutting"]
extract_features_and_train(dirs, mt, mt, st, st, "svm", "svm_trainedModel")
