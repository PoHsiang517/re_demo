
import re

# 判斷輸入字串是否為數字
def is_number(num):
	pattern = re.compile(r"^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$")
	result = pattern.match(num)
	if result:
		return True
	else:
		return False
#====================================================================

link = dict({"烘蛋" : "https://i.imgur.com/9pmCKaZ.jpg",
             "回鍋肉" : "https://i.imgur.com/B0SBwag.jpg",
             "雞翅" : "https://i.imgur.com/tgFj3mE.jpg",
             "蚵仔" : "https://i.imgur.com/QNzRVJ4.jpg",
             "蝦球" : "https://i.imgur.com/tgxeGNg.jpg",
             "蝦子" : "https://i.imgur.com/tgxeGNg.jpg",
             "鹽酥蝦" : "https://i.imgur.com/4IrNtjg.jpg",
             "肋排" : "https://i.imgur.com/fbN9uZP.jpg",
             "法式吐司" : "https://i.imgur.com/fl5K3gR.jpg",
             "地瓜" : "https://i.imgur.com/cG8oeco.jpg",
             "蔬菜" : "https://i.imgur.com/RQrfpxC.jpg",
             "花枝" : "https://i.imgur.com/MmKp3NF.jpg",
             "馬鈴薯" : "https://i.imgur.com/BsOFSW8.jpg",
             "海鮮" : "https://i.imgur.com/XAqjkwH.jpg",
             "煎餅" : "https://i.imgur.com/XAqjkwH.jpg",
             "太陽蛋吐司" : "https://i.imgur.com/2t5EobR.jpg",
             "炸雞" : "https://i.imgur.com/qe7UoMz.jpg",
             "虱目魚肚" : "https://i.imgur.com/mHVa7BV.jpg",
             "吐司磚烘蛋" : "https://i.imgur.com/qY9vx3u.jpg",
             "饅頭" : "https://i.imgur.com/HvypheB.jpg",
             "吐司布丁" : "https://i.imgur.com/2IPr7yh.jpg",
             "披薩" : "https://i.imgur.com/TNChEzR.jpg",
             "PIZZA" : "https://i.imgur.com/TNChEzR.jpg",
             "雞腿" : "https://i.imgur.com/EOreprT.jpg",
             "肉丸" : "https://i.imgur.com/tCmFeA7.jpg",
            })

text = input("請輸入文字: ")
re_comp = re.compile(r"(烘蛋|回鍋肉|雞翅|蚵仔|蝦球|鹽酥蝦|蝦子|肋排|法式吐司|地瓜|蔬菜|花枝|馬鈴薯|海鮮|煎餅|太陽蛋吐司|炸雞|虱目魚肚|吐司磚烘蛋|饅頭|吐司布丁|披薩|PIZZA|雞腿|肉丸)")
re_list = re_comp.findall(text)
output = []
for k, v in link.items():
	if k == re_list[0]:
		print(re_list[0])
		print(v)