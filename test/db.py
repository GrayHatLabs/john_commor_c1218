import sqlite3 as lite
import sys


con = lite.connect('password.db')
cur = con.cursor()    
#cur.execute("create TABLE response ( id INTEGER PRIMARY KEY AUTOINCREMENT, response TEXT,payload TEXT,chksum TEXT)")
#cur.execute("create TABLE request  ( id INTEGER PRIMARY KEY AUTOINCREMENT, write TEXT,response_id INT,FOREIGN KEY(response_id) REFERENCES response(id)) ")
#cur.execute("INSERT INTO response(response,payload,chksum) values (?,?,?)",('test','test','test'))
#lid = cur.lastrowid
#cur.execute("INSERT INTO request(write,response_id) values (?,?)",('test',str(lid)))
#print lid

cur = con.cursor()
cur.execute("select * from response");

rows = cur.fetchall()

for row in rows:
	print row

cur = con.cursor()
cur.execute("select * from request");

rows = cur.fetchall()

for row in rows:
	print row
