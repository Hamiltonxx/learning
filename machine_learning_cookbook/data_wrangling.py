import pandas as pd 
import httpx
import io

url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/titanic.csv'
resp = httpx.get(url)
dataframe = pd.read_csv(io.StringIO(resp.text))
print(dataframe.head(5))
print(dataframe.shape)
# print(dataframe.describe())
# print(dataframe.info())
print(dataframe.iloc[0])
print(dataframe.iloc[100:104])
# query
print(dataframe[dataframe['Sex']=='female'].head(3))
# sort
print(dataframe.sort_values(by=["Age"]).head(2))
# update
print(dataframe['Sex'].replace("female","woman").head(4))
print(dataframe['Sex'].replace(["female","male"],["woman","man"]).head(4))
print(dataframe.replace(1,"One").head(4))

print(dataframe['Age'].max(), dataframe['Age'].min(), dataframe['Age'].mean(), dataframe['Age'].count())
print(dataframe['Sex'].unique())
print(dataframe[dataframe['Age'].isnull()].head(4))

# drop
print(dataframe.drop('Age', axis=1).head(3))

# dictionary = {
#     "Name": ["Jacky Jackson","Steven Stevenson"],
#     "Age": [38,25],
#     "Driver": [True,False]
# }
# dataframe = pd.DataFrame(dictionary)
# print(dataframe)
# dataframe["Eyes"] = ["Brown","Blue"]
# print(dataframe)
