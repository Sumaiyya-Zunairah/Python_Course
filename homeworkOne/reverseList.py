my_list = input("Enter a list ")

new_list = []

for i in my_list:
    new_list = [i] + new_list

print(new_list)