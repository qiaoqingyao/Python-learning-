#. 读取的过程 1 打开文件， 2 读取文件  3 关闭文件

#  r: read
#. w: write
#. A : 可读写

==================================
File = open('文件路径', ‘r’)  'r' 只可读， ‘w’，只可写， ‘a+’ 可读写

data = file.read().  一次性全部读出来
data = file.read(5). 读前5个字符


file.seek(n). 跳过前n个字符

data = file.readline() # only read one line a time

While data:
	 print（data, end = ''）
         Data = file.readline()

Dates =file.readlines(). # read all lines one time
print(type(dates))   #。data 属性为 list
for line in dates:
	print(line, end='')
file.close()

===================================
# code file.close() is no need anymore
With open('file position','r') as file:
	datas = file.readlines()
	for line in datas:
		print(line)

===================================

This is database config file

da_url=31.23.45.11
db_port =1521
db_user =user
db_pass =password
====================

configData ={}
With open('file position','r') as file:
	datas = file.readlines()
	for line in datas:
		if line.startswith('#')
			continue
		key = line.split('=')[0]
		value = line.split('=')[1].replace('\n',' ')
		configData[key]=value
		print(line)
If __name__ =='__main__'
	print(configData)
==================================================
 # file writing

With open('data position','w') as file:
	data = 'hello python'
	file.write(data)
Data =[1,2,3]
For data in Data:
	file.write(data)

Or 
File.writelines([data+'\n'] for data in Data]). # there will have a extra blank line

Or
File.writelines('\n'.join(Data))	 # join   make the list into string

'w'.    Cleaning all content before writing stuff
'a'.    Adding new content
