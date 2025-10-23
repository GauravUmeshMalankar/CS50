
# first method
a = []

for i in range(0,5):
    x = (int)(input("Enter a number: "))
    a.append(x)

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
           temp = a[i]
           a[i]=a[j]
           a[j]=temp
print("Sorted list",a)


# second method
a = []

for i in range(0,5):
    x = (int)(input("Enter a number: "))
    a.append(x)

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
            a[i],a[j]=a[j],a[i]
    print(a)
          
print("Sorted list",a)
