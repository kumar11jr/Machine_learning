import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
# print(dir(iris))
# print(iris.feature_names)

df = pd.DataFrame(iris.data,columns=iris.feature_names)
# print(df.head(5))
df['target'] = iris.target
# print(df.head(5))

from sklearn.model_selection import train_test_split
X = df.drop('target',axis='columns')
y = df.target

X_train,X_test,y_train,y_test =train_test_split(X,y, test_size=0.3)

from sklearn.svm import SVC
model = SVC()
print(model.fit(X_train,y_train))
print(model.score(X_test,y_test))  # 96.67%


# by tunning parameters
model_c = SVC(C=10)
print(model_c.fit(X_train,y_train))
print(model_c.score(X_test,y_test))  # 100%



