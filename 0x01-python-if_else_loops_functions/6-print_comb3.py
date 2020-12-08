#!/usr/bin/python3
for number in range(10):
    for num in range(number + 1, 10):
        print("{}".format(str(number) + str(num)), end="")
        if int(str(number) + str(num)) < 89:
            print(", ", end="")
print("")
