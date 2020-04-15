import requests
from bs4 import BeautifulSoup

url='https://finance.naver.com/sise/'

html=requests.get(url).text
soup=BeautifulSoup(html, 'html.parser')
names=soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div')

for i, name in enumerate(names):
    print("{}위: {}".format(i+1, name.text))         