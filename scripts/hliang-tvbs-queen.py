import requests
from bs4 import BeautifulSoup
import re
from qbittorrent import Client

# Get all tvbs-queen links from first search page, then save as episode:url dict
home_url = "http://bt.hliang.com/"
main_url = "http://bt.hliang.com/search.php?keyword=%E5%A5%B3%E4%BA%BA%E6%88%91%E6%9C%80%E5%A4%A7"

r = requests.get(main_url)
soup = BeautifulSoup(r.text, 'html.parser')

items = {}
for element in soup.find_all('a', attrs={'target':'_blank'}):
    episode = re.findall(r'\d+', element.text)
    if not episode:
        continue
    url = element['href']
    url = home_url + url
    items[episode[0]] = url

# Sort episodes by date
sorted_episodes = sorted(items)

# Check episodes to see whether they have already been added previously
with open('hliang_tvbs_queen_episode_list.txt', 'r') as filehandle:
    episodes = [episode.rstrip() for episode in filehandle.readlines()]

# Find difference between scraped episodes and already downloaded episodes
to_download = set(sorted_episodes) - set(episodes)
to_download = list(to_download)

# If there aren't any items, exit
if not to_download:
    print('All links already available, no magnets added')
    exit()

# Save new episodes to file
with open('hliang_tvbs_queen_episode_list.txt', 'a+') as filehandle:
    filehandle.writelines("%s\n" % episode for episode in sorted(to_download))

# Run through every url, extracting the magnet links
magnets = []
#for _, url in items.items():
for episode in to_download:
    url = items[episode]
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    magnets.append(soup.find_all('a', attrs={'id':'magnet'})[0]['href'])

# Add to torrent client
qb = Client('http://127.0.0.1:8080/')
qb.login('admin', 'password') # Password omitted
dl_path = '/location'

for magnet in magnets:
    qb.download_from_link(magnet, savepath=dl_path)

amount = len(magnets)

print(f'{amount} magnets added!')