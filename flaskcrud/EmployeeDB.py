import sqlite3

conn= sqlite3.connect('EMPLOYEE.db')
print("Database opened successfully")
s='''CREATE TABLE EMPLOYEE(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,salary DECIMAL(10,2) NOT NULL)'''
print("Table created successfully")
conn.execute(s)
conn.close()