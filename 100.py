students = [
    {"name": "Arshia", "age": 18, "job": "Backend Developer"},
    {"name": "Ahmad", "age": 13, "job": "Frontend Developer"},
    {"name": "Ali", "age": 14, "job": "Security Engineer"},
    {"name": "Arad", "age": 16, "job": "Data Engineer"},
]

output = """
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>

<h1>Pishgaman G</h1>

<table id="customers">
  <tr>
    <th>Student Name</th>
    <th>Student Age</th>
    <th>Student Job</th>
  </tr>
"""

for student in students:
    output += f"""
  <tr>
    <td>{student['name']}</td>
    <td>{student['age']}</td>
    <td>{student['job']}</td>
  </tr>
    """

output += """
</table>
</body>
</html>
"""

open("Table.html", "w").write(output)
print("Done")