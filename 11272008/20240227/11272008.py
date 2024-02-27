import requests
import feedparser

# RSS Feed URL
url = "https://news.pts.org.tw/xml/newsfeed.xml"

# Get RSS Feed
response = requests.get(url)

# 解析 RSS Feed
feed = feedparser.parse(response.content)

#提取 Feed 內容
for entry in feed.entries:
    print(entry.title)
    #印出 summary
    print(entry.summary)

    # 印出區隔線
    print("="*50)
    
    import requests
import feedparser
import csv

# RSS Feed URL
url = "https://news.pts.org.tw/xml/newsfeed.xml"

# Get RSS Feed
response = requests.get(url)

# 解析 RSS Feed
feed = feedparser.parse(response.content)

# 檔案位置
file_path = r"C:\Users\Johnny\Desktop\cycu_ai2024\11272008.csv"

# 開啟檔案，並寫入含有 "巴黎" 的標題
with open(file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])  # 寫入標題
    for entry in feed.entries:
        if '巴黎' in entry.title:
            print(entry.title)
            writer.writerow([entry.title])  # 寫入含有 "巴黎" 的標題


