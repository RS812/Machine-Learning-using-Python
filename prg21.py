import pandas as pd
from sklearn import preprocessing
d=pd.read_csv("D:\\rutvi\\data.csv")
d
ohe=pd.get_dummies(d["STUNAME"])
ohe
stdscale=preprocessing.scale(ohe)
print("Mean Data: ",stdscale.mean(axis=0))
print("Standard Mean Data: ",stdscale.std(axis=0))
