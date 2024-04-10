import pandas as pd
import folium

# 讀取CSV文件，使用'cp950'編碼
df = pd.read_csv(r'C:\\Users\\Johnny\\Desktop\\cycu_ai2024\\11272008\\20240409\\地震活動彙整.csv', encoding='cp950')

# 刪除第一欄和第一列的資料
df = df.drop(df.columns[0], axis=1)
df = df.drop(df.index[0], axis=0)

# 將目前第一欄的資料轉換成日期時間格式
df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])

# 將目前第一欄的資料只取2024-04-03 07:58:00 之後的資料
df = df[df[df.columns[0]] >= '2024-04-03 07:58:00']


# 將第一欄的名稱改為時間，第二欄的名稱改為經度，第三欄的名稱改為緯度，第四欄的名稱改為規模，第五欄的名稱改為深度，第六欄的名稱改為地點
df.columns = ['時間', '經度', '緯度', '規模', '深度', '地點']


# 印出資料
print(df)

# 創建地圖對象，這裡以台灣為中心
m = folium.Map(location=[23.6978, 120.9605], zoom_start=7)

# 繪製地震點並在點上顯示地震資訊
for i in range(len(df)):
    # 取得緯度和經度資訊
    latitude = df.iloc[i, 2]
    longitude = df.iloc[i, 1]
    
    # 取得地震資訊
    time = df.iloc[i, 0]
    magnitude = df.iloc[i, 3]
    depth = df.iloc[i, 4]
    location = df.iloc[i, 5]
    
    # 在地圖上標記地震點並顯示地震資訊
    popup_info = f"Time: {time}<br>Latitude: {latitude}<br>Longitude: {longitude}<br>Magnitude: {magnitude}<br>Depth: {depth}<br>Location: {location}"
    folium.Marker([latitude, longitude], popup=folium.Popup(popup_info, max_width=250)).add_to(m)

# 保存地圖
m.save('earthquake_map.html')





