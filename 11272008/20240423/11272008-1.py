import os
import requests
from bs4 import BeautifulSoup

# 基本網頁 URL
base_url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240423/"

# 目標目錄
target_dir = "C:\\Users\\Johnny\\Desktop\\cycu_ai2024\\11272008\\20240423"

# 遍歷 00 到 23
for i in range(24):
    # 建立完整的網頁 URL
    url = base_url + f"{i:02d}/"

    # 發送 GET 請求
    response = requests.get(url)

    # 解析 HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有的 a 標籤
    links = soup.find_all('a')

    # 遍歷所有的鏈接
    for link in links:
        # 獲取 href 屬性
        href = link.get('href')
        
        # 檢查是否為 CSV 文件
        if href.endswith('.csv'):
            # 建立完整的文件 URL
            file_url = url + href
            
            # 下載文件
            file_response = requests.get(file_url)
            
            # 確保目錄存在
            os.makedirs(target_dir, exist_ok=True)
            
            # 寫入文件
            with open(os.path.join(target_dir, os.path.basename(href)), 'wb') as f:
                f.write(file_response.content)