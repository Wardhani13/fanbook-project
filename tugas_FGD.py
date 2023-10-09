import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.bilibili.tv/id/anime', headers=headers)

client = MongoClient('mongodb://wardhani1:sparta@ac-6ez4vhl-shard-00-00.uxvodvx.mongodb.net:27017,ac-6ez4vhl-shard-00-01.uxvodvx.mongodb.net:27017,ac-6ez4vhl-shard-00-02.uxvodvx.mongodb.net:27017/?ssl=true&replicaSet=atlas-fr57e5-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.dbsparta

soup = BeautifulSoup(data.text, 'html.parser')

animes = soup.select('.section__list__item')

for anime in animes:
    anime_title = anime.select_one('.bstar-video-card__title-text').text
    genre = anime.select_one('.bstar-video-card__desc.bstar-video-card__desc--normal').text.strip().split('.')[1]
    img_tag = soup.select_one('.bstar-image__img')
    # print(anime_title,'/', genre,'/', img_tag["src"])

    db.anime.insert_one({'title': anime_title, 'genre': genre, 'link img': img_tag["src"]})