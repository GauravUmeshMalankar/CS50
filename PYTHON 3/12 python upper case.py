
# first method
before=input("Before: ")
print("After: ", end="")
for c in before:
    print(c.upper(),end="")
print()

# second method
before=input("Before: ")
# variable declared
after = before.upper()
print(f"After: {after}")

# third method
before=input("Before: ")
# variable not declared tighten up
print(f"After: {before.upper()}")
