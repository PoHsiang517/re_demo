
import re

text = input("請輸入文字: ")
link = dict({"烘蛋" : "https://i.imgur.com/9pmCKaZ.jpg",
	         "回鍋肉" : "https://i.imgur.com/B0SBwag.jpg",
	         "雞翅" : "https://i.imgur.com/tgFj3mE.jpg",
	         "蚵仔" : "https://i.imgur.com/QNzRVJ4.jpg",
	         "蝦" : "https://i.imgur.com/tgxeGNg.jpg",
	         "肋排" : "https://i.imgur.com/fbN9uZP.jpg",
	         "天氣" : "查詢氣象功能",
	         "氣象" : "查詢氣象功能"
	        })

re_comp = re.compile(r"(烘蛋|回鍋肉|雞翅|蚵仔|蝦|肋排|天氣|氣象)")
re_list = re_comp.findall(text)

for k, v in link.items():
	for i in range(len(re_list)):
		if k == re_list[i]:
			print(v)
'''
for i in range(len(re_list)):

    print(re_list[i])
    i += 1
'''