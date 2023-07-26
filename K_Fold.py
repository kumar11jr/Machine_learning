import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits

df = load_digits()


from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier


# spilting datasets
from sklearn.model_selection import train_test_split
# X_train,X_test,y_train,y_test =train_test_split(df.data , df.target, test_size=0.1)



# lr = LogisticRegression()
# lr.fit(X_train,y_train)
# print(lr.score(X_test,y_test))


# svm = SVC()
# svm.fit(X_train,y_train)
# print(svm.score(X_test,y_test))


# rn = RandomForestClassifier()
# rn.fit(X_train,y_train)
# print(rn.score(X_test,y_test))


from sklearn.model_selection import KFold
kf = KFold(n_splits=4)

for train ,test in kf.split([1,2,3,4,5,6,7]):
    print(train,test)



def get_score(model,X_train,X_test,y_train,y_test):
    model.fit(X_train,y_train)
    return model.score(X_test,y_test)


from sklearn.model_selection import StratifiedKFold
folds = StratifiedKFold(n_splits=10,shuffle=True,random_state=42)


score_lf = []
score_sv = []
score_rf = []
for train,test in folds.split(df.data,df.target):
    X_train ,X_test,y_train,y_test = df.data[train],df.data[test],df.target[train],df.target[test]
    score_lf.append(get_score(LogisticRegression(), X_train ,X_test,y_train,y_test))
    score_sv.append(get_score(SVC(), X_train ,X_test,y_train,y_test))
    score_rf.append(get_score(RandomForestClassifier(), X_train ,X_test,y_train,y_test))


print(score_lf)
print(score_sv)
print(score_rf)


from sklearn.model_selection import cross_val_score
print(cross_val_score(LogisticRegression(),df.data,df.target))
print(cross_val_score(SVC(),df.data,df.target))
print(cross_val_score(RandomForestClassifier(),df.data,df.target))