import re

text = input("請輸入字串: ")
pattern = (r"(蛋|肉|雞|蚵|蝦|肋排|吐司"
	       r"|地瓜|蔬菜|花枝|薯|海鮮|煎餅"
	       r"|饅頭|布丁)")
re_comp2 = re.match(pattern, text)
output = re_comp2
print(output)