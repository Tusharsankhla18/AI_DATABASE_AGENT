
# Creating a Database
import sqlite3

## Connect to sqlite3
connection=sqlite3.connect("student.db")

# Creating a Cursor object to insert record, create table, retrieve data
cursor=connection.cursor()

## creating the table
table_info =""" 
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);

"""

cursor.execute(table_info)

## Insert some more records

cursor.execute('''Insert into STUDENT values('ALICE','Data Science','A',90)''')
cursor.execute('''Insert into STUDENT values('BOB','Data Science','B',100)''')
cursor.execute('''Insert into STUDENT values('CAREY','Data Science','A',86)''')
cursor.execute('''Insert into STUDENT values('DAISY','Devops','A',50)''')
cursor.execute('''Insert into STUDENT values('ELLY','Devops','A',60)''')

## Displaying all the records.
print("THE INSERTED DATA ARE :")

data = cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
  print(row)

# Closing the connection
connection.commit()
connection.close()

