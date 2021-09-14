import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    a_tag = tr.select_one('td.title > div > a')
    img_tag = tr.select_one('td > img')
    point_class = tr.select_one('td.point')
    if a_tag is not None:
        title = a_tag.text
        rank = img_tag['alt']
        rating = point_class.text
        doc = {
            'rank': rank,
            'title': title,
            'rating': rating,
        }
        db.movies.insert_one(doc)