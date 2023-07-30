import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
 
df = pd.read_csv("K_Cluster.csv")
# print(df.head())


# plt.scatter(
#     df['Age'],
#     df['Income($)']
# )
# plt.show()


kn = KMeans(n_clusters=3)
# print(kn)
y_predict = kn.fit_predict(df[['Age','Income($)']])
# print(y_predict)
df['y_predicted'] = y_predict
# print(df.head())
df1 = df[df.y_predicted==0]
df2 = df[df.y_predicted==1]
df3 = df[df.y_predicted==2]

plt.scatter(df1.Age,df1['Income($)'],color="green")
plt.scatter(df2.Age,df2['Income($)'],color="red")
plt.scatter(df3.Age,df3['Income($)'],color="black")
plt.show()
