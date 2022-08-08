docu = input()
word = input()

cnt = 0
while True:
    if word in docu:
        docu = docu.replace(word ,' ', 1)
        cnt += 1
    if word not in docu:
        break
print(cnt)