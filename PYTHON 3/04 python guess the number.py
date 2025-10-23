from cs50 import get_int

n = get_int("Guess the number: ")

if n < 2:
    print(f"You guess lower than me,{n}")
elif n > 2:
    print(f"You guess higher than me,{n}")
else:
    print(f"You guess correctly,{n} the number")

from cs50 import get_string
answer = get_string("Enter your name: ")
print(f"Hello, {answer}")
