import feedparser as fp
from gtts import gTTS as gT
import shutil
import time

old_path = '/Users/macowner/news_feed/news.mp3'
file_path = '/Users/macowner/Library/Mobile Documents/com~apple~CloudDocs/News/news.mp3'

feeds = {'wsj_world': r'http://www.wsj.com/xml/rss/3_7085.xml',
        'wsj_markets': r'http://www.wsj.com/xml/rss/3_7031.xml', # The WSJ Markets feed is empty. Leaving it in
        'wsj_usb': r'http://www.wsj.com/xml/rss/3_7014.xml',
        'wsj_tech': r'http://www.wsj.com/xml/rss/3_7455.xml'}


def news_creator():
    for feed, url in feeds.items():
        parsed = fp.parse(url)
        news = parsed['entries']

        news_sums = []
        for news in news:
            news = news.summary
            news_sums.append(news)

    # print(news_sums)
    news_string = ' NEXT STORY. '.join(news_sums)
    print(news_string)

    tts = gT(news_string).save('news.mp3')
    shutil.move(old_path, file_path)


while True:
    news_creator()
    print('Created news file.')
    time.sleep(3600)
