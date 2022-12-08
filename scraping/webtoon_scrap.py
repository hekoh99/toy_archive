from urllib.request import urlopen
from bs4 import BeautifulSoup
import dload
import csv

base_url = 'https://comic.naver.com'
response = urlopen(base_url + '/webtoon/weekday')
b_html = response.read()
s_html = b_html.decode()
bs = BeautifulSoup(s_html, "html.parser")

webtoon_list = [["웹툰명", "평점", "날짜"]]
link_dic = {}
result = []
index = 0

for i in bs.findAll('div', {"class":'col_inner'}):
    webtoon_list_day = [i.find('h4').text]
    for j in i.findAll('a', {'class' : 'title'}):
        info = [j.text]
        link_dic[j.text] = j['href']
        webtoon_res = urlopen(base_url + j['href'])
        webtoon_page = BeautifulSoup(webtoon_res.read().decode(), "html.parser")
        for k in webtoon_page.findAll('div', {"class" : "rating_type"}) :
            result.append(info + [k.strong.text])
        for k in webtoon_page.findAll('td', {"class" : "num"}):
            result[index].append(k.text)
            index += 1
# print(result)

with open("webtoon.csv", "w", newline="") as f:
    wr = csv.writer(f)
    for row in result:
        wr.writerow(row)