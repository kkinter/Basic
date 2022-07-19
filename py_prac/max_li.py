li = [1, 1, 3, 1, 2]
sum_val = 0
max_val = max(li)

print(max(li[4:len(li)]))

# for i in range(len(li)):
#         if li[i] == max_val:
#             max_val = max(li[i+1,len(li)])
#             sum_val += max_val - i
#         else:
#             sum_val += max_val - i