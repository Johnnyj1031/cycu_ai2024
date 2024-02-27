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
    
