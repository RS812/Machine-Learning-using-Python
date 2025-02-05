from sklearn.linear_model import LinearRegression 
import numpy as np 
X = np.array([[1], [2], [3], [4], [5]]) 
y = np.array([2, 4, 5, 4, 5])  
model = LinearRegression() 
model.fit(X, y) 
print("Slope (m):", model.coef_[0]) 
print("Intercept (c):", model.intercept_) 
predictions = model.predict(X) 
print("Predictions:", predictions)