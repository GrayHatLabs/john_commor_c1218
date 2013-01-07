import sqlite3 as lite
import sys

def checkdb(frame):
	con = lite.connect('powermeter.db')

	with con:
		cur = con.cursor()
		cur.execute("select response,payload,chksum from request join response on request.response_id = response.id where request.write = ? limit 1",("ee0000000001201310123213",))
		rows = cur.fetchall()
		print len(rows)
		for row in rows:
			print row


checkdb('ee00000000012013101231231')
