import mysql.connector

conn = mysql.connector.connect(
	host='sql6.freesqldatabase.com',
	user = 'sql6399658',
	password = 'WBFBbzAubg',
	database='sql6399658'
	)

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS STUDENT2020(sno int(2),name varchar(20),marks int(10),city varchar(9))")

#cursor.execute("INSERT INTO STUDENT2020 VALUES(1,'NANDA',551,'DELHI')")
#cursor.execute("INSERT INTO STUDENT2020 VALUES(2,'SAURABH',462,'DELHI')")
#cursor.execute("INSERT INTO STUDENT2020 VALUES(3,'SANAL',400,'DELHI')")
#cursor.execute("INSERT INTO STUDENT2020 VALUES(4,'TRISHA',450,'MUMBAI')")
# commented out coz i have already commited changes 


cursor.execute('SELECT SUM(marks) FROM STUDENT2020 WHERE city="DELHI"')
result = cursor.fetchall()
for i in result:
	print(i)


#cursor.execute("DELETE FROM STUDENT2020 WHERE sno=1")
#conn.commit()

cursor.execute('SELECT * FROM STUDENT2020')
r = cursor.fetchall()
for i in r:
	print(i)


conn.close()