import requests
import feedparser
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# 基礎的網址
base_url = 'https://www.cwa.gov.tw/rss/forecast/36_05.xml'

# 創建一個 DataFrame 來儲存氣象資料
weather_data = pd.DataFrame(columns=['County', 'Temperature'])

# 抓取所有的網址
for i in range(1, 24):
    # 產生新的網址
    url = base_url[:-6] + str(i).zfill(2) + '.xml'

    # 下載 RSS feed
    response = requests.get(url)

    # 確認請求成功
    if response.status_code == 200:
        # 解析 RSS feed
        feed = feedparser.parse(response.content)

        # 讀取每一個項目
        for entry in feed.entries:
            # 如果項目的標題包含 "今晚明晨"，則提取縣市名稱和溫度
            if '今晚明晨' in entry.title:
                county = entry.title.split(' ')[0]
                temperature = float(entry.title.split(' ')[-3])
                weather_data = weather_data.append({'County': county, 'Temperature': temperature}, ignore_index=True)

# 讀取台灣的區界地圖
taiwan = gpd.read_file('C:\\Users\\User\\Desktop\\cycu_ai2024\\11272008\\20240402\\county\\COUNTY_MOI_1090820.shp')

# 將氣象資料與地理資訊結合
taiwan = taiwan.merge(weather_data, left_on='COUNTYNAME', right_on='County')

# 畫出地圖
fig, ax = plt.subplots(1, 1)
taiwan.plot(column='Temperature', ax=ax, legend=True)

# 在每個縣市的中心點標示溫度
for x, y, label in zip(taiwan.geometry.centroid.x, taiwan.geometry.centroid.y, taiwan['Temperature']):
    ax.text(x, y, str(label), fontsize=12)

# 設定經緯度範圍
plt.xlim(119,122)
plt.ylim(21.5,25.5)

# 顯示地圖
plt.show()

# 儲存地圖
plt.savefig('C:\\Users\\User\\Desktop\\cycu_ai2024\\11272008\\20240402\\taiwan_map.png')