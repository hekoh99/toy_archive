from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

base_url = 'https://comic.naver.com'
response = urlopen(base_url + '/webtoon/weekday')
b_html = response.read()
s_html = b_html.decode()
bs = BeautifulSoup(s_html, "html.parser")

webtoon_list = []
link_dic = {}
result = [["웹툰명", "평점", "날짜"]]
index = 1

# 3중 for문 어떻게 좀 해보기 (o)

for i in bs.findAll('div', {"class":'col_inner'}):
    webtoon_list_day = [i.find('h4').text]
    for j in i.findAll('a', {'class' : 'title'}):
        webtoon_list.append(j.text)
        link_dic[j.text] = j['href']

for toon in webtoon_list:
    if toon not in link_dic:
        continue
    else :
        toon_link = link_dic.pop(toon)
        toon_res = urlopen(base_url + toon_link)
        toon_page = BeautifulSoup(toon_res.read().decode(), "html.parser")
        for cell in toon_page.findAll('tr'):
            rate = cell.find('div', {"class" : "rating_type"})
            date = cell.find('td', {"class" : "num"})
            if rate is not None and date is not None:
                info = [toon]
                info.append(rate.strong.text)
                info.append(date.text)
                result.append(info)

with open("webtoon.csv", "w", newline="") as f:
    wr = csv.writer(f)
    for row in result:
        wr.writerow(row)