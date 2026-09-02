my_list = [3, 8, 2, 10, 5]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)