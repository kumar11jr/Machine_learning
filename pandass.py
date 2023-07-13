import pandas as pd

# weather_data = {
#     'day':['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
#     'temperature':[32,35,28,24,32,31],
#     'windspeed':[6,7,2,7,4,2],
#     'event':['rain','sunny','snow','snow','rain','sunny']
# }
# df = pd.DataFrame(weather_data)
df = pd.read_csv('data.csv')
print(df)

rows , columns = df.shape
print(columns)


print(df.head())
print(df.head(2))
print(df.tail())
print(df.tail(1))
print(df[2:4])

print(df.columns)
print(df['day'])
print(df['windspeed'].mean())
print(df['windspeed'].max())
print(df.describe())    #print statics of dataset



print(df[df.temperature>=32])

print(df[['day','temperature']][df.temperature==df['temperature'].mean()])

# # print(df.index)
# df.set_index('day', inplace=True)


# print(df.loc['1/3/2017'])


# df.reset_index(inplace=True)


 
# ways of creating data frame

# df = pd.read_csv("file.csv")

# df = pd.read_excel("file.xlsx","Sheet1")

#  weather_data = {
#     'day':['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
#     'temperature':[32,35,28,24,32,31],
#     'windspeed':[6,7,2,7,4,2],
#     'event':['rain','sunny','snow','snow','rain','sunny']
# }
# df = pd.DataFrame(weather_data) 


# new_df = df.fillna(0)
# print(new_df)


# new_df = df.fillna({
#     'temperature':0,
#     'windspeed':1000,
#     'event':'shahil'
# })
# print(new_df)


new_df = df.fillna(method='ffill')
print(new_df)
