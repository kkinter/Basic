number_list = [1, 23, 9, 6, 91, 59, 29]
max_num = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max_num2 = max(number_list2)

if max_num > max_num2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max_num < max_num2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")