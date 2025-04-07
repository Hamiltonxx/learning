import pandas as pd
import httpx
import io

url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/data.csv'

# dataframe = pd.read_csv(url)
resp = httpx.get(url)
dataframe = pd.read_csv(io.StringIO(resp.text))
print(dataframe.head(2))

# url = 'https://raw.githubusercontent.com/chrisalbon/sim_data/master/data.xlsx'

# dataframe = pd.read_excel(url, sheet_name=0, header=0)
# resp = httpx.get(url)
# dataframe = pd.read_excel(io.BytesIO(resp.content), sheet_name=0, header=0)
# print(dataframe.head(2))
