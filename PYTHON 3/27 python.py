
import sqlite3

try:
    db = sqlite3.connect("100 python db.db")
    cursor=db.cursor()
    a= int(input("Enter Emp Id\n"))
    b= input("Enter Employee name\n")
    c= int(input("Enter salary number\n"))
    #sql="create table emp(empid int, empname varchar(50), salary number(10,2))"
    #sql="insert into emp values(%d %s %f%(a,b,c))"
    sql= "insert into emp values('"+str(a)+"','"+b+"','"+str(c)+"')"


    #sql ="""insert into emp (empid, empname, salary number)values('{}', '{}' , '{}');""".format(a,b,c)

    cursor.execute(sql)
    db.commit()
    print("Record inserted successfully")
    db.close()

except Exception as e:
    print("Check connection",e)





