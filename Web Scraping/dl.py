from bs4 import BeautifulSoup
import requests
from idm import IDMan
import os
import re

url = ''
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')
link = soup.find('span', class_='notranslate')
dl_link = link.a['href']
series_name = re.split(r'[\s|_]', link.text.lstrip())[0]
path = r''
save_path = os.path.join(path, series_name)
ep_list = os.listdir(save_path)


try:
    # creates directory if none exists
    os.mkdir(save_path)
    print(f'Creating {series_name} Folder...')
except FileExistsError:
    print(f'{series_name} Folder already exists')

for episode in soup.find_all('span', class_='notranslate')[:25]:

    try:
        # retrieves download link
        ep_link = episode.a['href']
        ep_name = ep_link.split('/')[-1]
    except TypeError:
        print('Download link unavailable...')
        continue
    else:
        # checks if file already exists,
        # ignores if it exits and downloads if it doesn't.
        if ep_name in ep_list:
            print(f"{ep_name} already exists")
        else:
            # The file is downloaded with IDM
            downloader = IDMan()
            downloader.download(ep_link, save_path)
            print(f'{ep_name} downloading...')


