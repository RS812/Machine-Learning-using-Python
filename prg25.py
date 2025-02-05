from pandas import *
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.preprocessing import MinMaxScaler
d=read_csv("D:\\rutvi\\data.csv")
d
data=get_dummies(d["STUNAME"])
data
scaler=MinMaxScaler()
scaled_data=scaler.fit_transform(data)
print(scaled_data)
for i in d.select_dtypes(include="number").columns:
    sb.histplot(data=d,x=i)
plt.show()
