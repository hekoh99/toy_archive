from urllib.request import urlopen
from bs4 import BeautifulSoup
import dload

base_url = 'https://comic.naver.com'
response = urlopen(base_url + '/webtoon/weekday')
b_html = response.read()
s_html = b_html.decode()
bs = BeautifulSoup(s_html, "html.parser")

webtoon_list = []
link_dic = {}

for i in bs.findAll('div', {"class":'col_inner'}):
    webtoon_list_day = [i.find('h4').text]
    for j in i.findAll('a', {'class' : 'title'}):
        webtoon_list_day.append(j.text)
        link_dic[j.text] = j['href']
    webtoon_list.append(webtoon_list_day)

print(link_dic['윌유메리미'])