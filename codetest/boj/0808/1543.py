docu = input()
word = input()
new_docu = docu
cnt = 0
while True:
    if word in new_docu:
        new_docu = new_docu.replace(word ,' ', 1)
        cnt += 1
    if word not in new_docu:
        break
print(cnt)