# Problem set 1

"""
2. Sort a list
Create a function in Python that accepts numbers. The first
will be a list of numbers. The second parameter will be a string that
can be one of the following values: asc, desc, and none.

If the second parameter is “asc,” then the function should return a list
with the numbers in ascending order. If it’s “desc,” then the list should
be in descending order, and if it’s “none,” it should return the original
list unaltered.
"""

# creating a empty list and accepting number from user
l = []
print("Enter any five numbers \n")

for i in range(5):
    n  = int(input("Enter a number: "))
    l.append(n)

# Displaying Original list
print(f"Your number list = {l} \n")

# Copying original list for none function
copy = list(l)

num = l

class order:
    def asec(self ,num):
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                if(num[i]>num[j]):
                   temp = num[i]
                   num[i]=num[j]
                   num[j]=temp
        print("Sorted list",num,"\n")

    def dsec(self ,num):
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                if(num[i]<num[j]):
                   temp = num[i]
                   num[i]=num[j]
                   num[j]=temp
        print("Sorted list",num,"\n")

    def none(self,copy):
        print("Your list",copy,"\n")
       
arrange = order()

while True:
    print("Choose order format: \n asec\t  desc\t  none\t")
    print("Enter order format for your list: ")
    f = input()

    if (f == "asec"):
        arrange.asec(num)

    elif (f == "desc"):
        arrange.dsec(num)


    elif (f == "none"):
        arrange.none(copy)

    else:
        print("Invalid Input")
        break;

        
        
    


    
     
