
a = []
t=0
i=0
final_size=(int)(input("Enter list size number: "))

for i in range(final_size):
    x =input("Enter a number: ")
    a.append(x)


def Average():
    return sum[a] / len[a]


average= Average[a]
print("Average: ",round(average,2))
        

# Python program to get average of a list
# Using reduce() and lambda 
  
# importing reduce()
from functools import reduce
  
def Average(lst):
    return reduce(lambda a, b: a + b, lst) / len(lst)
  
# Driver Code
lst = [15, 9, 55, 41, 35, 20, 62, 49]
average = Average(lst)
  
# Printing average of the list
print("Average of the list =", round(average, 2))
