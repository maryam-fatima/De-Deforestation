import os
os.chdir("/content/gdrive/MyDrive/project_folder/")
dirs = ["Cutting/Cutting", "NonCutting/NonCutting"]

from sklearn.datasets import load_iris
#Iris is available from the sklearn package
iris = load_iris(dirs)
X, y = iris.data, iris.target
