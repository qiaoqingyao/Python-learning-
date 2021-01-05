Sqlite

# 1 connect to database. 2 拿到游标， 3 执行sql， 4 关闭游标， 5 关闭数据库链接

import sqlite3

# connect

conn= sqlite3.connect('test.db')

# get cursor. 
cursor= conn.cursor()

# execute cursor

sql='create table user(id, int(11) primary key, name varchar(50))'
cursor.execute(sql)

# close cursor and connection
cursor.close()
Conn.close()
=======================

import sqlite3

# connect

conn= sqlite3.connect('test.db')

# get cursor. 
cursor= conn.cursor()

# execute cursor
# adding data into created table

sql='insert into user (id, name) values ('1','Peter')'
cursor.execute(sql)

# close cursor and connection
cursor.close()
Conn.commit()
Conn.close()
=========================
# query data

import sqlite3

# connect

conn= sqlite3.connect('test.db')

# get cursor. 
cursor= conn.cursor()

# execute cursor
# query data



sql='select * from user'
Sql = 'update user set name='AKi' where id =4'. # replace data
Sql= 'delete from user where id=1' # delete data
cursor.execute(sql)
results= cursor.fetchall()

# close cursor and connection
cursor.close()

Conn.close()

   
Try:
   sql='select * from user'
   Sql = 'update user set name='AKi' where id =4'. # replace data
   Sql= 'delete from user where id=1' # delete data
   cursor.execute(sql)
   results= cursor.fetchall()	
   Conn.commit()


Except Exception as e:
	conn.rollback()
Finally:
	cursor.close()
	conn.close()
==========================================
Mysql


Import pymysql

conn= pymysql.connect('localhost','root','root','testdb')

