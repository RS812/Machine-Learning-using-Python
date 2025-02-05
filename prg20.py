from pandas import *
data =read_csv("D:\\rutvi\\data.csv")
data
xdata=get_dummies(data["STUNAME"])
xdata
