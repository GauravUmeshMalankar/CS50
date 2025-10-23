
import sqlite3

try:
    db = sqlite3.connect("100 python db.db")
    cursor=db.cursor()
    sql =  "select * from emp"
    cursor.execute(sql)

    z=cursor.fetchone()
    print(z)

    x=cursor.fetchall()
    for y in x:
        print("\n %d \t %s \t %f"%(y[0],y[1],y[2]))

    db.close()
except Exception as e:
    print("Check connection",e)










