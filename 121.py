import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

# cur.execute("DELETE FROM students;")
#
# cur.execute("INSERT INTO students VALUES ('Taha','2021153884','haftom','19.83');")
# cur.execute("INSERT INTO students VALUES ('Mohammad','1504794207','nohom','16.53');")
# cur.execute("INSERT INTO students VALUES ('Reza','7394467645','haftom','15.90');")
# cur.execute("INSERT INTO students VALUES ('Arian','6583333934','hashtom','17.21');")

cur.execute("SELECT * FROM students;")
records = cur.fetchall()
natl_codes = [i[1] for i in records]
evens = []

for i in natl_codes:
    if int(i) % 2 == 0:
        evens.append(i)

for i in records:
    if i[1] in evens:
        print(i[0])

con.commit()
con.close()
