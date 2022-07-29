def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
  

## def 로 정의한 함수명을 변수로 선언했을 때 오류가 발생했었음
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    gcd_ = gcd(a, b)
    print( (a * b) // gcd_ )