
"""
def fact(x):
    if x == 0:
        return 1
    else:
        y = x * fact(x - 1)
        return y

a = int(input("Enter a number: "))
print("Factorial of %d = %d" % (a, fact(a)))


class F:
    def fact(self, x):
        if x == 0:
            return 1
        else:
            y = x * self.fact(x - 1)
            return y



a = int(input("Enter a number: "))
calc= F()
result = calc.fact(a)
print("Factorial of %d = %d" % (a, result))
"""

class F:
    def fact(self, x):
        if x == 0:
            return 1
        else:
            y = x * self.fact(x - 1)
            return y



a = int(input("Enter a number: "))
calc= F()
print("Factorial of %d = %d" % (a, calc.fact(a) ))
