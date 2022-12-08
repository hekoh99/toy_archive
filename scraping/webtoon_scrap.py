from urllib.request import urlopen
from bs4 import BeautifulSoup
import dload

response = urlopen('https://comic.naver.com/webtoon/weekday')
b_html = response.read()
s_html = b_html.decode()
bs = BeautifulSoup(s_html, "html.parser")

webtoon_list = []

for i in bs.findAll('div', {"class":'col_inner'}):
    webtoon_list_day = [i.find('h4').text] + [j.text for j in i.findAll('a', {"class":"title"})]
    webtoon_list.append(webtoon_list_day)

print(webtoon_list)