import os
from pyAudioAnalysis import audioTrainTest as aT
os.chdir("/content/gdrive/MyDrive/project_folder/")
dirs = ["UpdatedTest/Cutting", "UpdatedTest/NonCutting"]
aT.evaluate_model_for_folders(dirs,
                              "svm_CuttingNonCutting", 
                              "svm", 
                              "Cutting")
