print("welcome to array element reverser")

n = int(input("Please enter your list length: "))
num_list = []

for i in range (n):
    num = int(input("Please enter numbers: "))
    num_list.append(num)


print("This is your list:\n", num_list)

rev_num_list = []

for m in range (n-1,-1,-1):
    rev_num_list.append(num_list[m])
    
print("This is reverse of your list:\n", rev_num_list)

