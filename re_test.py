
import sys
import re
import random
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
             "地瓜" : "https://i.imgur.com/cG8oeco.jpg", #10
             "蔬菜" : "https://i.imgur.com/RQrfpxC.jpg",
             "花枝" : "https://i.imgur.com/MmKp3NF.jpg",
             "馬鈴薯" : "https://i.imgur.com/BsOFSW8.jpg",
             "海鮮" : "https://i.imgur.com/XAqjkwH.jpg",
             "煎餅" : "https://i.imgur.com/XAqjkwH.jpg",
             "太陽蛋吐司" : "https://i.imgur.com/2t5EobR.jpg",
             "炸雞" : "https://i.imgur.com/qe7UoMz.jpg",
             "虱目魚肚" : "https://i.imgur.com/mHVa7BV.jpg",
             "吐司磚烘蛋" : "https://i.imgur.com/qY9vx3u.jpg",
             "饅頭" : "https://i.imgur.com/HvypheB.jpg", #20
             "吐司布丁" : "https://i.imgur.com/2IPr7yh.jpg",
             "披薩" : "https://i.imgur.com/TNChEzR.jpg",
             "PIZZA" : "https://i.imgur.com/TNChEzR.jpg",
             "雞腿" : "https://i.imgur.com/EOreprT.jpg",
             "肉丸" : "https://i.imgur.com/tCmFeA7.jpg",
             "味噌魚" : "https://i.imgur.com/0yZ3AH4.jpg",
             "子排" : "https://i.imgur.com/9zmRv2G.jpg",
             "牛排" : "https://i.imgur.com/M2uvOpJ.jpg",
             "雞米花" : "https://i.imgur.com/jHZ5EQx.jpg",
             "腐乳炸雞" : "https://i.imgur.com/uuNv8NU.jpg", #30
             "蒜香蛤蜊" : "https://i.imgur.com/i0f153K.jpg",
             "炸薯片" : "https://i.imgur.com/Q7lSh9N.jpg",
             "椒麻雞" : "https://i.imgur.com/NRbMoPP.jpg",
             "蘆筍培根捲" : "https://i.imgur.com/bGYh6nr.jpg",
             "鳳梨蝦球" : "https://i.imgur.com/4J4Hj0P.jpg",
             "牛肉捲" : "https://i.imgur.com/AsEDY6l.jpg",
             "地瓜球" : "https://i.imgur.com/FMxgg4j.jpg",
             "馬鈴薯薯條" : "https://i.imgur.com/qnlkhIE.jpg",
             "牛小排" : "https://i.imgur.com/BcBWTge.png",
             "地瓜波波球" : "https://i.imgur.com/21kakk3.jpg", #40
             "烤玉米" : "https://i.imgur.com/K78PB4M.jpg",
             "醬爆豬肉燥" : "https://i.imgur.com/Ax5ifAG.jpg",
             "迷彩蛋糕" : "https://i.imgur.com/X6YOhUy.png",
             "夢幻雲朵蛋" : "https://i.imgur.com/DYpZJiC.jpg",
             "愛爾蘭瘋薯" : "https://i.imgur.com/xTQLnr8.jpg",
             "葡式蛋塔" : "https://i.imgur.com/6HteEpg.jpg",
             "嫩雞炒時蔬" : "https://i.imgur.com/EDdAdSR.png",
             "蔥抓餅" : "https://i.imgur.com/hXsqivX.png",
             "薑絲絲瓜" : "https://i.imgur.com/dSYFLai.jpg",
             "烤香魚" : "https://i.imgur.com/2w68tWS.png",
             "鮭魚飯糰" : "https://i.imgur.com/Hl4FR4o.png"
            })

#完整字組
re_comp = re.compile(r"(烘蛋|回鍋肉|雞翅|蚵仔|蝦球|鹽酥蝦|蝦子|肋排|法式吐司|地瓜\
                       |蔬菜|花枝|馬鈴薯|海鮮|煎餅|太陽蛋吐司|炸雞|虱目魚肚|吐司磚烘蛋|饅頭\
                       |吐司布丁|披薩|PIZZA|雞腿|肉丸|味噌魚|子排|牛排|雞米花|腐乳炸雞\
                       |蒜香蛤蜊|炸薯片|椒麻雞|蘆筍培根捲|鳳梨蝦球|牛肉捲|地瓜球|馬鈴薯薯條|牛小排|地瓜波波球\
                       |烤玉米|醬爆豬肉燥|迷彩蛋糕|夢幻雲朵蛋|愛爾蘭瘋薯|葡式蛋塔|嫩雞炒時蔬|蔥抓餅|薑絲絲瓜|烤香魚\
                       |鮭魚飯糰)")

#精簡字組
re_comp2 = re.compile(r"(蛋|肉|雞|蚵|蝦|肋排|吐司|地瓜|蔬菜|花枝|薯|海鮮|煎餅|饅頭|布丁\
                         |披薩|PIZZA|肉丸|魚|子排|牛|蛤|蘆筍|培根|鳳梨|玉米|豬|糕|蛋塔|蔥\
                         |絲瓜|飯)") #\斷句符號前的字會搜尋不到

def input_string():

    text = input("請輸入文字: ")
    re_list = re_comp.findall(text)
    if not re_list:
    	re_list = re_comp2.findall(text)
    k_result = []
    
    for k, v in link.items():
        for i in range(len(re_list)):
            if k.find(re_list[i]) != -1:
                k_result.append(k)

    try:
        link_value = link.get(random.choice(k_result))
        print(link_value)
    except IndexError:
        if text == "exit":
            sys.exit()
        else:
            print("查無食譜，請重新輸入，或輸入exit離開: ")
        
        return input_string()

input_string()