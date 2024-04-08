# Join a list of integers into a string in Python

my_list = [1, 2, 3, 4, 5]

my_str = ', '.join(map(str, my_list))

print(my_str)  # 👉️ "1, 2, 3, 4, 5"