import pandas as pd
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv("D:\\2260\\DATA.csv")
data
lbl=LabelEncoder()
data["NAME"]=lbl.fit_transform(data["STUNAME"])
data
