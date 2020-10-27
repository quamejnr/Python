from bs4 import BeautifulSoup
import requests

url = "http://coreyms.com"

source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    content = article.find('div', class_='entry-content')
    summary = content.p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4].split('?')[0]
        yt_link = f"https://youtube.com/watch?v={vid_id}"
    except TypeError as e:
        yt_link = None

    print(yt_link)
    print('')





