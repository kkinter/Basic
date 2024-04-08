def foo(word):
    for i in range(len(word)-1,-1,-1):
        print(word[i], end='')

foo('apple')
