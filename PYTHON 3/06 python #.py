def main():
    h = height()
    for i in range(h):
        print("#", end =" ")

def height():
    while True:
        try:
            n = (int(input("Enter height: ")))
            if n > 0:
                break
        except:
            print("Value Error: enter a integer")
    return n
main()
