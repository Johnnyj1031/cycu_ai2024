 #crawler from rss of central weather agency
import pandas as pd
import requests
import feedparser

county_list = []
for num in range(1, 23):
    #string format with prefix 0 if num < 10
    url = 'https://www.cwa.gov.tw/rss/forecast/36_' + str(num).zfill(2) + '.xml'
    print(url)
    #get xml from url
    response = requests.get(url)
    #parse rss feed
    feed = feedparser.parse(response.content)

    tempdict = {}

    for entry in feed.entries:
        # entry.title includes '溫度'
        if '溫度' in entry.title:
        # 資料的格式 如下:
        # 金門縣04/02 今晚明晨 晴時多雲 溫度: 22 ~ 24 降雨機率: 10% (04/02 17:00發布)
            print(entry.title)
        #取出縣市名稱(前三個字)
            tempdict['county'] = entry.title[:3]

        #取出溫度的部分 使用空格切割後 取出 -7 與 -5 的部分
            tempdict['min'] = entry.title.split(' ')[-7]
            tempdict['max'] = entry.title.split(' ')[-5]
            print(tempdict['county'], tempdict['min'], tempdict['max'])
    
            county_list.append(tempdict)
        print("=======================================")

df_weather = pd.DataFrame(county_list)

#尋找台灣的區界地圖 shape file/ geojson file
#https://data.gov.tw/dataset/7441

#read 20240402/tract_20140313.json as geopanas
import geopandas as gpd
import pandas as pd

#read shape file
taiwan=gpd.read_file('C:\\Users\\User\\Desktop\\cycu_ai2024\\11272008\\20240402\\county\\COUNTY_MOI_1090820.shp')
import os
#print cwd
print (taiwan)

#plot taiwan using matplotlib
import matplotlib.pyplot as plt


df_taiwan=gpd.read_file('C:\\Users\\User\\Desktop\\cycu_ai2024\\11272008\\20240402\\county\\COUNTY_MOI_1090820.shp')

#plot taiwan using matplotlib
import matplotlib.pyplot as plt

#merge df_taiwan and df_weather on df_taiwan.COUNTYNAME = df_weather.county 
geo_taiwan = pd.merge(df_taiwan, df_weather, left_on='COUNTYNAME', right_on='county')

print (geo_taiwan)
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 設定字體為 SimHei
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

# 繪製台灣地圖
geo_taiwan.plot()
plt.xlim(117.7,122.5)
plt.ylim(21.7,26.5)

# 在每個多邊形的中心點輸出縣市名稱
for x, y, label in zip(geo_taiwan.geometry.centroid.x, geo_taiwan.geometry.centroid.y, geo_taiwan['min']):
    plt.text(x, y, label, fontsize=8, ha='center')

for x, y, label in zip(geo_taiwan.geometry.centroid.x, geo_taiwan.geometry.centroid.y, geo_taiwan['max']):
    plt.text(x+ 0.2 , y, label, fontsize=8, ha='center')

# 加入標題
plt.title('台灣04/02 溫度 11272008 王興集')

# 顯示圖表
plt.show()

#save to png file
plt.savefig('C:\\Users\\User\\Desktop\\cycu_ai2024\\11272008\\20240402\\taiwan_map.png')


