import sqlite3
from person import Person

con = sqlite3.connect('people.db')

cur = con.cursor()

def insert_person(pers):
    with con:
        cur.execute("INSERT INTO people VALUES (:name, :id, :points)",
                    {'name':pers.name, 'id':pers.id, 'points':pers.points})

def search_by_id(id):
    cur.execute("SELECT * FROM people WHERE id=:id", {'id': id})
    return cur.fetchall()

def update_points(pers, points):
    with con:
        cur.execute("UPDATE people SET points = :points WHERE id = :id",
                    {'points':points, 'id':pers.id})

def remove_person(pers):
    with con:
        cur.execute("DELETE from people  WHERE id  = :id", {'id':pers.id})

#make all the people
p1 = Person("Steven Smith", 211, 80)
p2 = Person("Jian Wong", 122, 92)
p3 = Person("Chris Peterson", 213, 91)
p4 = Person("Sai Patel", 524, 94)
p5 = Person("Andrew Whitehead", 425, 99)
p6 = Person("Lynn Roberts", 626, 90)
p7 = Person("Robert Sanders", 287, 75)

"""
#create a table to hold all the people with 3 columns
#table name is people
cur.execute(CREATE TABLE people (
                name text,
                id integer,
                points integer
                ))
con.commit()

#insert all the people one by one into the list
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

con.commit()
"""

#this returns the list
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cur.fetchall())

con.close()


