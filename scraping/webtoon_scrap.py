from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm

base_url = 'https://comic.naver.com'
response = urlopen(base_url + '/webtoon/weekday')
b_html = response.read()
s_html = b_html.decode()
bs = BeautifulSoup(s_html, "html.parser")

webtoon_list = []
link_dic = {}
result = [["웹툰명", "평점", "날짜"]]

for i in tqdm(bs.findAll('div', {"class":'col_inner'})):
    # webtoon_list_day = [i.find('h4').text]
    for j in i.findAll('a', {'class' : 'title'}):
        try :
            check_duplicate = link_dic[j.text] # 중복 체크
        except KeyError:
            link_dic[j.text] = j['href']
            toon_res = urlopen(base_url + j['href'])
            toon_page = BeautifulSoup(toon_res.read().decode(), "html.parser")
            for cell in toon_page.findAll('tr'):
                rate = cell.find('div', {"class" : "rating_type"})
                date = cell.find('td', {"class" : "num"})
                if rate is not None and date is not None :
                    info = [j.text]
                    info.append(rate.strong.text)
                    info.append(date.text)
                    result.append(info)


with open("result.csv", "w", newline="") as f:
    wr = csv.writer(f)
    for row in result:
        wr.writerow(row)