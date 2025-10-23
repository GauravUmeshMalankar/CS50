"""
size =  int(input("Enter size of rangoli = "))

def rangoli(size):
    n = 0
    for i in range(1, size +1):
        for j in range(1,(size - i) +1):
            print(end = " ")
            while n!=( 2 * i - 1):
                print("*", end = "")
                n = n +1
                n=0
            print()
    k = 1
    n = 1
    for i in range(1, size):
        for j in range(1,k +1):
            print(end = " ")
            k = k+1
            while n<=( 2 * (size-i) - 1):
                print("*", end = "" )
                n = n +1

            n=1
            print()

#size= 5
print(rangoli(size))
"""

size =  eval(input("Enter size of rangoli = "))

def abc(size):
        for i in range(65,70):
            for j in range(i,64,-1):
                print(chr(j),end=" ")
            for n in range(66,i+1):
                print(chr(n),end=" ")
            

def rangoli(size):
    for x in range(size):
        print("-" * (size - x),abc(size ),"-" * (size - x))
      
   
    for x in range(size - 2, -1, -1):
        print("-" * (size - x), " " * (2*x + 1),"-" * (size - x))

rangoli(size)
