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
scores = []

for i in records:
    scores.append(float(i[-1]))

scores.sort(reverse=True)

for i in scores[:3]:
    print(i)

con.commit()
con.close()
