# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
#soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup)

res = requests.get("http://www.doubleround.com.tw/v2/official")
soup2 = BeautifulSoup(res.text, "html.parser")

h3_tag = soup2.select("div.cabinet-middle > h3.cabinet-instruction")
for i in h3_tag:
	print(i.text)


'''
print(soup.prettify()) #重新依標準縮進格式編排HTML語法
print(soup.get_text()) #列印出所有文字

for link in soup.find_all('a'): #列印出所有連結
	#print(link)
	print(link.get("href"))

print(soup.title) #列印出title(含標籤)
print(soup.title.string) #列印出title標籤中的文字
'''

