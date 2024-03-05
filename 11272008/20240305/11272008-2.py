import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# 抓取網頁內容
url1 = "https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx"
url2 = "https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil2019.aspx"

response1 = requests.get(url1)
response2 = requests.get(url2)

# 解析網頁內容
soup1 = BeautifulSoup(response1.text, 'html.parser')
soup2 = BeautifulSoup(response2.text, 'html.parser')

# 找到所有的表格
tables1 = soup1.find_all('table')
tables2 = soup2.find_all('table')

# 將 HTML 表格轉換為 DataFrame
df1_1 = pd.read_html(str(tables1[0]))[0]
df1_2 = pd.read_html(str(tables1[1]))[0]

df2_1 = pd.read_html(str(tables2[0]))[0]
df2_2 = pd.read_html(str(tables2[1]))[0]

# 合併 DataFrame
df1 = pd.concat([df1_1, df2_1])
df2 = pd.concat([df1_2, df2_2])

# 印出 DataFrame
print(df1)
print(df2)

#將 DataFrame 寫入 CSV 檔案
df2.to_csv("C:/Users/USER/Desktop/oil.csv", index=False)

# df2 只保留前5個欄位的資料
df2 = df2.iloc[:, :5]

# 去除第二欄值到第五欄值為 NaN 的列
df2 = df2.dropna(subset=df2.columns[1:5], how='all')

# 把第一欄的資料型態 轉成 datetime
df2[df2.columns[0]] = df2[df2.columns[0]].str.split(" ", expand=True)[0]
df2[df2.columns[0]] = pd.to_datetime(df2[df2.columns[0]], format='%Y/%m/%d')

print (df2)

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# 使用前一個非 NaN 值來填充 NaN 值
df2 = df2.fillna(method='ffill')

# 使用 matplotlib 繪製折線圖 , x 軸是日期 , y 軸是油價
plt.figure(figsize=(10, 6))
for i in range(1, 5):
    plt.plot(df2[df2.columns[0]], df2[df2.columns[i]], label=df2.columns[i])

plt.xlabel('日期')  # X-axis label
plt.ylabel('油價')  # Y-axis label
plt.title('油價趨勢')  # Title
plt.legend()  # Legend
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # Set font to support Chinese characters
plt.show()