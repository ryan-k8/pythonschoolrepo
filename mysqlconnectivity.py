import sqlite3  #/ mysql-connector

conn = sqlite3.connect('example.db') # mysql-connector

cursor = conn.cursor()

ct = '''CREATE TABLE sample(sno int(1),name varchar(20))'''
cursor.execute(ct)

cursor.execute("INSERT INTO sample VALUES(1,'ryan')")
cursor.execute("INSERT INTO sample VALUES(2,'ankur')")
cursor.execute("INSERT INTO sample VALUES(3,'advik')")

cursor.execute("SELECT * FROM sample")
result = cursor.fetchall()
print(type(result))
print(result)


conn.commit()
conn.close()