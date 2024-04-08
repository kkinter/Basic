
def foo(word):
    result = ''
    length = len(word) - 1
    cnt = 0
    while length >= cnt:
        if word[cnt] != 'a':
            result += word[cnt]
        cnt += 1
    return result
print(foo('apple'))