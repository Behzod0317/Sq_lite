import sqlite3
from sql_Employee import Employee
import pandas as pd

conn = sqlite3.connect('Employee.db')

c=conn.cursor()
# c.execute(""" CREATE TABLE employees(
#       first text,
#       last text,
#       pay integer
#   )""")

employee_1 = Employee('Shavkat','Xoldorov',12000000)
employee_2 = Employee('Risqinboy','Tojiboyev',1200000)
employee_3 = Employee('Behruz','Nabijonov',12000000)
employee_4 = Employee('Azizxon','Tojixonov',12300000)
employee_5 = Employee('Oybek','Valiyev',12300000)

c.execute("INSERT INTO employees VALUES('Behzod','Hoshimov',13500000)")
c.execute("INSERT INTO employees VALUES('{}','{}',{})".format(employee_1.first,employee_1.last,employee_1.pay))

conn.commit()

c.execute("INSERT INTO employees VALUES(:first, :last, :pay)",(employee_3.first,employee_3.last,employee_3.pay))

conn.commit()
c.execute("SELECT rowid,* FROM employees")
item = c.fetchall()

for el in item:
    print(el)

conn.commit()
conn.close()

columns = ["Id","Name","Lastname","Salary $"]
df = pd.DataFrame(data= item, columns=columns)
df.to_csv("Employees.csv", index = False)