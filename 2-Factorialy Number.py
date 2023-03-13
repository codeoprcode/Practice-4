import math

num = int(input("Please enter your number= "))
i = 0

while 8 == 8:
    i = i + 1
    a = math.factorial(i)
    
    if a == num:
        print("Yessssss")
        print("This is your factorial number= ", i)
        break

    if a > num:
        print("Noooooooo")
        break

