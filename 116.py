import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

cur.execute("CREATE TABLE students (name, codemelli, grade, score);")

con.commit()
con.close()
print('Done')
