import csv

with open("phonebook","a") as f:
    name=(input("Enter a name: "))
    number=(input("Enter a number: "))
    writer = csv.writer(f)
    writer.writerow([name,number])
