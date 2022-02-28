import sqlite3
from person import Person

con = sqlite3.connect('people.db')

cur = con.cursor()

p1 = Person("Steven Smith", 211, 80)
p2 = Person("Jian Wong", 122, 92)
p3 = Person("Chris Peterson", 213, 91)
p4 = Person("Sai Patel", 524, 94)
p5 = Person("Andrew Whitehead", 425, 99)
p6 = Person("Lynn Roberts", 626, 90)
p7 = Person("Robert Sanders", 287, 75)

cur.execute("""CREATE TABLE people (
                name text,
                id integer,
                points integer
                )""")
con.commit()

cur.execute("INSERT INTO people VALUES (:name, :id, :points)",
{'name':p1.name, 'id':p1.id, 'points':p1.points})

cur.execute("INSERT INTO people VALUES (:name, :id, :points)",
{'name':p2.name, 'id':p2.id, 'points':p2.points})

cur.execute("INSERT INTO people VALUES (:name, :id, :points)",
{'name':p3.name, 'id':p3.id, 'points':p3.points})

cur.execute("INSERT INTO people VALUES (:name, :id, :points)",
{'name':p4.name, 'id':p4.id, 'points':p4.points})

cur.execute("INSERT INTO people VALUES (:name, :id, :points)",
{'name':p5.name, 'id':p5.id, 'points':p5.points})

cur.execute("INSERT INTO people VALUES (:name, :id, :points)",
{'name':p6.name, 'id':p6.id, 'points':p6.points})

cur.execute("INSERT INTO people VALUES (:name, :id, :points)",
{'name':p7.name, 'id':p7.id, 'points':p7.points})