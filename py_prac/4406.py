t = int(input())
for i in range(t):
    s = input()
    new_word = ''
    for j in s:
        if j not in 'aeiou':
            new_word += j
    print(f"#{i+1} {new_word}")