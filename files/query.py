import mysql.connector as conn
import random

output = []
x = [random.randint(1,20)]

my_db = conn.connect(host='localhost', user='jeff', password='jeff', database='employees')

cursor = my_db.cursor()
cursor.execute('SELECT * FROM employees LIMIT %s', x)

result = cursor.fetchall()

#for a in result:
output = [a for a in result]

f = open('index.html', 'w')

# the html code which will go into index.html
htmlcode = f"""<html>
<head>
<title>Title</title>
</head>
<body>
<h2>Fake Data</h2>

<p> {output} </p>

</body>
</html>
"""

# writing the code into the file
f.write(htmlcode)

# close the file
f.close()

