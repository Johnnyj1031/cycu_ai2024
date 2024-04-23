import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
import re
import urllib.parse

# 迴圈從00到23
for i in range(24):
    hour = str(i).zfill(2)  # 將數字轉換為兩位數的字串，例如：'01', '02', ..., '23'
    base_url = f"https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240423/{hour}/"
    response = requests.get(base_url)

    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有CSV檔案的連結
    csv_links = soup.find_all('a', href=re.compile(r'.csv'))

    for csv_link in csv_links:
        # 結合基礎URL與相對URL以獲得完整的CSV檔案URL
        csv_url = urllib.parse.urljoin(base_url, csv_link['href'])

        # 讀取CSV檔案
        csv_response = requests.get(csv_url)
        data = StringIO(csv_response.text)
        df = pd.read_csv(data)

        print(df)