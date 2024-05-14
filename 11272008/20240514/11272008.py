import requests
from bs4 import BeautifulSoup
import pandas as pd
import ssl

# 建立一個未經驗證的 SSL context
ssl._create_default_https_context = ssl._create_unverified_context

# 獲取網頁內容
base_url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240429/"

# 遍歷所有的小時
for hour in range(24):
    hour_str = str(hour).zfill(2)  # 將小時轉換為兩位數的字串
    url = base_url + hour_str + "/"
    
    response = requests.get(url)

    # 解析網頁內容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有的 csv 檔案連結
    csv_links = [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith('.csv')]

    # 讀取並印出每個 csv 檔案的內容
    for csv_link in csv_links:
        df = pd.read_csv(csv_link)
        print(df)