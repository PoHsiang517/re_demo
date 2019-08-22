import re

'''
正規表示式特殊序列
\A	只在字串開頭進行匹配。
\b	匹配位於開頭或者結尾的空字串
\B	匹配不位於開頭或者結尾的空字串
\d	匹配任意十進位制數，相當於 [0-9]
\D	匹配任意非數字字元，相當於 [^0-9]
\s	匹配任意空白字元，相當於 [ \t\n\r\f\v]
\S	匹配任意非空白字元，相當於 [^ \t\n\r\f\v]
\w	匹配任意數字和字母，相當於 [a-zA-Z0-9_]
\W	匹配任意非數字和字母的字元，相當於 [^a-zA-Z0-9_]
\Z	只在字串結尾進行匹配
'''
a = '一1二2三3四4五5六七八678九9'
b = "one1 two2 three3 four4 five5 six6 seven7 eight8 nine9 ten10"

re_findall_1 = re.findall(r"(\d)", a)
print(re_findall_1)
# result = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

ret = re.findall(r'(\D)', a)
print(ret)
# result = ['一', '二', '三', '四', '五', '六', '七', '八', '九']

re_split = re.split("\d", a)
print(re_split)
# Result = ['一', '二', '三', '四', '五', '六七八', '', '', '九', '']

re_split_1 = re.findall("1.*x", b)
print(re_split_1)
# result = ['1 two2 three3 four4 five5 six']

re_compile = re.compile(r"\w*ne\w*")
print(re_compile.findall(b))
#result = ['one1', 'nine9']
