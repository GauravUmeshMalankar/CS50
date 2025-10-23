"""
class me:
    def me2(y):

        y ="This code is in a function"
        return y

    x = "This code is in a class"

a1= me()
print(a1.x)
print(a1.me2())

class Person:
  def __init__(self,name, age):
    self.name = name
    self.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
"""
#print("Autopass rejected")
#print("Autopass accept")
def no(n1):
    n5 = n1[0]
    n2 = n1[1]
    n3 = int()
    n3 = n1[2]
    n4 = [n2,n3]
    n6 = ("Accepted")
    n7 = ("Rejected")
    n8 = str()
    for n in n4:
        if(n2== "white" and n2 == "gray"):
            n8 = n8+n7
            return n8
        elif(n3 >=8  and n3 <= 20):
            n8 = n8+n7
            return n8
        elif(n3 >=1  and n3 <= 7):
            n8 = n8+n6
            return n8
        else:
            n8 = n8+n6
            return n8 
    if (n8 == n6):
        print(f"Autopass of your car {n5} is {n6}")
    elif(n8 == n7):
        print(f"Autopass of your car {n5} is {n7}")
        
     
n1 = ["Ford", "white", 9]
no(n1)



"""
def autopass(mycar):
    for i in mycar:
        if (mycar == "white" and i>=9):
            print("mycar not")

mycar = ["Ford","white",11]
print(autopass(mycar))
"""
