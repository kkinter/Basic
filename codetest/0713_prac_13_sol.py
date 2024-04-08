
def foo(word):
    result = ''
    for i in range(len(word)-1,-1,-1):
        result += word[i]
    return result
print(foo('applaaaaaaaaaaae'))
word = 'apple'
print(word[::-1])
print(reversed(word))
print(''.join(reversed(word)))

# index로 접근하는게 알고리즘 풀기 좋음
for i in range(len(word)):
    print(word[len(word)-i-1])