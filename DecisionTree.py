import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("DecisionTree.csv")
# print(df.head(5))


inputs = df.drop('salary_more_then_100k',axis='columns')
target = df['salary_more_then_100k']


from sklearn.preprocessing import LabelEncoder
le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()

inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['job_n'] = le_job.fit_transform(inputs['job'])
inputs['degree_n'] = le_degree.fit_transform(inputs['degree'])

# print(inputs.head(5))

inputs_n = inputs.drop(['company','job','degree'],axis='columns')
# print(inputs_n)


from sklearn import tree
model = tree.DecisionTreeClassifier()
model.fit(inputs_n,target)
print(model.predict([[2,0,1]]))
