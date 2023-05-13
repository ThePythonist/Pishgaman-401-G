import sqlite3

con = sqlite3.connect('test2.db')
cur = con.cursor()

# cur.execute("""
# CREATE TABLE employees (
# id INTEGER PRIMARY KEY,
# fname VARCHAR(50),
# lname VARCHAR(50),
# age INT,
# job VARCHAR(50)
# );
# """)

# people = [
#     {"Fname": "Arshia", "Lname": "Yarmohammadi", "Age": 18, "Job": "Front-End Dev"},
#     {"Fname": "Arad", "Lname": "Moradi", "Age": 16, "Job": "Front-End Dev"},
#     {"Fname": "Ahmad", "Lname": "Movahed", "Age": 13, "Job": "DB Admin"},
#     {"Fname": "Mohammad", "Lname": "Rostami", "Age": 13, "Job": "Project Manager"},
#     {"Fname": "Ali", "Lname": "Mohammadi", "Age": 6, "Job": "Security Engineer"},
# ]
#
# for person in people:
#     cur.execute(f"INSERT INTO employees (fname,lname,age,job) VALUES (?,?,?,?)",
#                 (person['Fname'], person['Lname'], person['Age'], person['Job']))

# cur.execute("DROP TABLE employees;")
cur.execute("SELECT * FROM employees;")
records = cur.fetchall()
for i in records:
    print(i)

con.commit()
con.close()
print('Done')
