import feedparser

rss_url = "http://www.spiegel.de/schlagzeilen/index.rss"
feed = feedparser.parse(rss_url)
item_list = []

for item in feed['items']:
    item_list.append(item['title'])

with open('./output.txt', mode = 'wt', encoding = 'utf-8') as file:
    for title in item_list:
        file.write(title + '\n')
