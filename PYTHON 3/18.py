"""
def is_prime(n):
    if n < 2:
        return n, "is not prime"

    for i in range(2, n):
        if n % i == 0:
            return n, "is not prime"

    return n," is prime"


n =(int)(input("enter a number: "))
print(is_prime(n))




def student_info(name,s_id,s_gpa,student_dic ):
   student_dic[student_name] = [s_id,student_gpa]
   return student_dic
sd = dict()

n = input("Enter student name: ")
a = (int)(input("Enter student roll no: "))
b = input("Enter student class: ")

print(student_info(n,a,b,sd))

def display(**kwargs):
    for x in kwargs.itens():
        print(x.key,"=",x.value)

#print(display(sd))
"""
s=(2,5,8)
s_append = s + (8, 16, 67)
print(s_append)
print(s)
