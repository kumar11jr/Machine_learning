import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("LogisticReg.csv")

# print(df.head(5))

plt.scatter(df.age,df.bought_insurance,color="red",marker="*")
# plt.show()

# print(df.shape)

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test =train_test_split(df[['age']],df.bought_insurance,test_size=0.1)

# print(X_test)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train,y_train)
print(model.predict(X_test))
print(model.score(X_test,y_test))
