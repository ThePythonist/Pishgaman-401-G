entry1 = input("Type Header : ")
entry2 = input("Type a Sentence : ")

output = f"""
<h1> {entry1} </h1>
<p> {entry2} </p>
"""

open("Home.html", "w").write(output)
print('Done')