
n = int(input("Please enter array lenght: "))
num_list = []

for i in range (n):
    num = int(input("Please enter numbers: "))
    num_list.append(num)

print("This is your entry list:\n", num_list)

final_list = []

for num in num_list:
    if num not in final_list:
        final_list.append(num)
    
print("This is your list without dupplication:\n",  final_list)
