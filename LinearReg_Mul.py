import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import math

area = [2600, 3000, 3200, 3600, 4000]
bedroom = [3,4,3,3,5]
age = [20,15,18,30,8]
prices = [550000, 565000, 610000, 680000, 725000]

data = {'area': area, 'bedroom':bedroom,'age':age, 'prices': prices}


df = pd.DataFrame(data)
# print(df)


median_bedroom = math.floor(df.bedroom.median())
df.bedroom = df.bedroom.fillna(median_bedroom)

# print(df)

reg = linear_model.LinearRegression()
reg.fit(df[['area','bedroom','age']],df.prices)

to_predict = np.array([[2500,4,5]])
predicted_price = reg.predict(to_predict)

print('Predicted price for an area of 2020 sqft:', predicted_price)
print(reg.coef_)




