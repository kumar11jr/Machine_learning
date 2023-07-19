import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits

digits = load_digits()

# print(dir(digits))

# plt.gray()
# plt.matshow(digits.images[1])
# plt.show()

# spilting datasets
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test =train_test_split(digits.data , digits.target, test_size=0.1)


#model importing
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train,y_train)
# print(model.predict(X_test))
# print(model.score(X_test,y_test))




# testing manually
plt.gray()
plt.matshow(digits.images[60])
# plt.show()
# print(digits.target[60])
print(model.predict([digits.data[60]]))