from sklearn.linear_model import LinearRegression
hours = [[1], [2], [3], [4], [5]]
marks = [20,30,40,50,60]
model = LinearRegression()
model.fit(hours, marks)
predicted_marks = model.predict([[6]])
print("hours studied:",6)
print("Predicted marks:", predicted_marks [0])