import folium

# 創建地圖對象，這裡以台灣為中心
m = folium.Map(location=[40.7128, -74.0060], zoom_start=13)

# 定義線條的坐標點
line_coordinates = [[40.7128, -74.0060], [40.7158, -74.0020], [40.7198, -74.0120]]

# 繪製線條
folium.PolyLine(line_coordinates, color="blue", weight=2.5, opacity=1).add_to(m)

# 保存地圖
m.save('map_with_line.html')