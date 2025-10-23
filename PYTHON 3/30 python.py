
import sqlite3

try:
    db = sqlite3.connect("100 python db.db")
    cursor=db.cursor()
    while(True):
        a= int(input("Enter Emp Id\n"))
        b= input("Enter Employee name\n")
        c= int(input("Enter salary number\n"))
        sql= "update emp set('empname=' "+b+" salary= "+c+" where empid='"+a+"' )"

        cursor.execute(sql)
        db.commit()
        x = input("Do you want to continue? Press y or n\n")
        if(x=="N" or x =="n"):
            break

        db.close()

except Exception as e:
    print("Check connection",e)










