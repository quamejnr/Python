"""
This program retrieves download links of the episodes of a tv series from a website.
Checks if episode on your pc and downloads if it is not
"""
from bs4 import BeautifulSoup
import requests
from idm import IDMan
import os
import re


url = 'https://www.lightdl.xyz/2019/02/su.html'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')
link = soup.find('span', class_='notranslate')
dl_link = link.a['href']
series_name = re.split(r'[\s|_]', link.text.lstrip())[0]
path = r'D:\VIDEOS\CINEMA\TV SHOWS'
save_path = os.path.join(path, series_name)
ep_list = os.listdir(save_path)


try:
    os.mkdir(save_path)                                         # creates directory if none exists
    print(f'Creating {series_name} Folder...')
except FileExistsError:
    print(f'{series_name} Folder already exists')

for episode in soup.find_all('span', class_='notranslate')[:25]:

    try:
        ep_link = episode.a['href']                             # retrieves download link
        ep_name = ep_link.split('/')[-1]
    except TypeError:
        print('Download link unavailable....')
        continue
    else:
        if ep_name in ep_list:                                  # checks if file already exists
            print(f"{ep_name} already exists")
        else:
            downloader = IDMan()
            downloader.download(ep_link, save_path)           # downloads file
            print(f'{ep_name} downloading...')
