# Accept 5 integers from the user
numbers = []
for i in range(5):
    numbers.append(int(input("Enter an integer: ")))

# Print even and odd numbers
even_numbers = []
odd_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
