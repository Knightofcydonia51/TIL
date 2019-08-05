import requests
from bs4 import BeautifulSoup

url='https://finance.naver.com/sise/'

html=requests.get(url).text
soup=BeautifulSoup(html, 'html.parser')
kospi=soup.select_one('#KOSPI_now')
print(kospi)
