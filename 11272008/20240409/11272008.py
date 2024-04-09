import pandas as pd
import folium

# 讀取CSV文件，使用'cp950'編碼
df = pd.read_csv(r'C:\\Users\\User\Desktop\\cycu_ai2024\\11272008\\20240409\\地震活動彙整.csv', encoding='cp950')

# 刪除第一欄和第一列的資料
df = df.drop(df.columns[0], axis=1)
df = df.drop(df.index[0], axis=0)

# 將目前第一欄的資料轉換成日期時間格式
df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])

# 將目前第一欄的資料只取2024-04-03 07:58:00 之後的資料
df = df[df[df.columns[0]] >= '2024-04-03 07:58:00']

# 目前第二欄的資料為經度，將其轉換成浮點數
df[df.columns[1]] = df[df.columns[1]].astype(float)

# 目前第三欄的資料為緯度，將其轉換成浮點數
df[df.columns[2]] = df[df.columns[2]].astype(float)

# 創建地圖對象，這裡以台灣為中心
m = folium.Map(location=[23.6978, 120.9605], zoom_start=7)

# 繪製地震點
for i in range(len(df)):
    folium.CircleMarker([df.iloc[i, 2], df.iloc[i, 1]], radius=5, color='red', fill=True, fill_color='red', fill_opacity=0.7).add_to(m)

# 保存地圖
m.save('earthquake_map.html')





