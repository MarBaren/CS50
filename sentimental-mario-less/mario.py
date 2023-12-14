# TODO

while True:
    try:
        size = int(input("Size: "))
        if size > 0 and size < 9:
            break
    except ValueError:
        print("Not a integer")


for j in range(size):
    for i in range(size):
        if j + i < size - 1:
            print(" ", end="")
        elif j + i >= size - 1:
            print("#", end="")
    print()
