import sqlite3
# make a connection
connection = sqlite3.connect("student.db")
cursor = connection.cursor()


# create table

table_info = """
Create table STUDENT(NAME VARCHAR(25) , CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);

"""

cursor.execute(table_info)


## insert some more records

cursor.execute('''Insert Into STUDENT values('Emad' , 'Data Science' , 'A' , 90)''')
cursor.execute('''Insert Into STUDENT values('Milad' , 'Machine Learning' , 'B' , 100)''')
cursor.execute('''Insert Into STUDENT values('Mariam' , 'Data Science' , 'A' , 85)''')
cursor.execute('''Insert Into STUDENT values('Mohammed' , 'DEVOPS' , 'A' ,50)''')
cursor.execute('''Insert Into STUDENT values('Mohra' , 'DEVOPS' , 'A' , 35)''')
## Display inserted records
print("The inserted records are")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()