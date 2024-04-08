def foo(word):
    length = len(word) -1
    while length >= 0:
        print(word[length],end='')
        length -= 1

foo('apple')