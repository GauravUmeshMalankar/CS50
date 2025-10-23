
n=int(input())
if n==0:
    print()
elif n==1:
    print('a')
else:
    s='abcdefghijklmnopqrstuvwxyz'
    a=s[0:n][::-1]
    l=[]
    for i in range(n):
        b=a[0:i+1]
        c=list(b)
        c='-'.join(c)
        l.append(c)
        x=s[1:n][::-1]
        l1=[]
    for i in range(n):
        d=x[0:i][::-1]
        d=list(d)
        t='-'.join(d)
        t='-'+t
        l1.append(t)
    for i in range(n):
        print(l[i].rjust((n*2)-1,'-'),end=" ")
        print(l1[i].ljust((n * 2) -2, '-'))
        l.reverse()
        l.remove(l[0])
        l1.reverse()
        for i in range(n-1):
            print(l[i].rjust((n*2)-1,'-'),end=" ")
            print(l1[i].ljust((n * 2) - 2, '-'))          
    

"""
size =  eval(input("Enter size of rangoli = "))
def rangoli(size):
    for x in range(size):
        print("-" * (size - x))
        for i in range(65,70):
            for j in range(i,64,-1):
                print(chr(j),end=" ")
            for n in range(66,i+1):
                print(chr(n),end=" ")
                for y in range(size):
                    print(i* (2*x + 1),"-" * (size - x))
            #print()
rangoli(size)

"""
