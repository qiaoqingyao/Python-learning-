import re
a ='123456'
b ='111222'
re.match(r'\d{6}',a) # a是否为6位数
>>> <re.match object : span =(0,6),match='123456'>.  # a 是6位数
c = '123456789'
re.match(r'^\{6}$',c) # 从头到尾都计算
>>>结果为空
d=‘800455’
re.match(r'^8\d{5}$',d) # 匹配8且后面为5位数
>>> <re.Match object : span=(0,6),match='800455'>
查找手机号，第一位为1， 第二位可能是3456789
f =’13000000000‘
re.match(r'^1[3456789]\d{9}$', f)
re.match(r'^1[^012]\d{9}$', f)  #不包括012
