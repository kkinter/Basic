s = input()
my_dict = {}
for i in s:
    my_dict.setdefault(i , 0)
    if i in my_dict:
        my_dict[i] += 1

print(my_dict)