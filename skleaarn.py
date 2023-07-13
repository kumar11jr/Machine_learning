import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

area = [2600, 3000, 3200, 3600, 4000]
prices = [550000, 565000, 610000, 680000, 725000]

data = {'area': area, 'prices': prices}

df = pd.DataFrame(data)

plt.scatter(df.area, df.prices, color='red', marker='+')
# plt.xlabel('Area')
# plt.ylabel('Price')
# plt.title('Price vs. Area')
# plt.show()

reg = linear_model.LinearRegression()
reg.fit(df[['area']], df.prices)

area_to_predict = np.array([[2020]])
predicted_price = reg.predict(area_to_predict)

print('Predicted price for an area of 2020 sqft:', predicted_price)
# print(reg.score())