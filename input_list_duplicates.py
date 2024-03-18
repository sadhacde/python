#collects user inputted list and removes duplicates

my_list = []
num = int(input("How many items do you want in the list: "))

for n in range(num):
    item = int(input("Enter a number: "))
    if item not in my_list:
        my_list.append(item)

print("The list with unique elements only:")
print(my_list)

