
import sqlite3

try:
    db = sqlite3.connect("100 python db.db")
    cursor=db.cursor()
    a= int(input("Enter Emp Id\n"))

    sql="delete from emp(where empid = %d %(y[0]))"
    

    cursor.execute(sql)
   
    print("Deleted successfully")
    db.close()

except Exception as e:
    print("Check connection",e)





