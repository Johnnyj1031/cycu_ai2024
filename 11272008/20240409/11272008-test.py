import pandas as pd
import folium
from folium.plugins import TimestampedGeoJson

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

# 創建地圖對象，這裡以台灣為中心
m = folium.Map(location=[23.6978, 120.9605], zoom_start=7)

# 將目前第一欄的資料轉換成日期時間格式並轉換為 ISO 8601 格式
df[df.columns[0]] = pd.to_datetime(df[df.columns[0]]).apply(lambda x: x.isoformat())

# 將經度和緯度數據轉換為數字
df['經度'] = pd.to_numeric(df['經度'])
df['緯度'] = pd.to_numeric(df['緯度'])

# 創建一個包含地震點的 GeoJSON 對象
data = {
    'type': 'FeatureCollection',
    'features': [
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [df.iloc[i, 1], df.iloc[i, 2]],
            },
            'properties': {
                'time': df.iloc[i, 0],
                'style': {'color' : 'blue'},
                'icon': 'arrow',
                'iconstyle':{
                    'fillColor': 'blue',
                    'fillOpacity': 0.6,
                    'stroke': 'false',
                },
                'popup': f"Time: {df.iloc[i, 0]}<br>Latitude: {df.iloc[i, 2]}<br>Longitude: {df.iloc[i, 1]}<br>Magnitude: {df.iloc[i, 3]}<br>Depth: {df.iloc[i, 4]}<br>Location: {df.iloc[i, 5]}",
            }
        } for i in range(len(df))
    ]
}

# 將 GeoJSON 對象添加到地圖上，並創建時間軸
TimestampedGeoJson(
    data,
    period='PT1H',
    add_last_point=True,
    auto_play=False,
    loop=False,
    max_speed=1,
    loop_button=True,
    date_options='YYYY/MM/DD HH:mm:ss',
    time_slider_drag_update=True
).add_to(m)

# 保存地圖
m.save('earthquake_map.html')