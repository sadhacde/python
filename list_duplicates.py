#removes duplicate numbers from list

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_real_list = []

for l in my_list:
    if l not in my_real_list:
        my_real_list.append(l)

print("The list with unique elements only:")
print(my_real_list)
