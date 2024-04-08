''' 
동적계획법 (DP)
- 작은 부분의 문제들을 해결한 후, 해당 부분의 문제의 해를 활용해서, 보다 큰 크기의 부분 문제를 해결
- 상향식 접근법으로, 가장 최하위 해답을 구한 후, 이를 저장하고, 해당 결과값을 이용해서 상위 문제를 풀어가는 방식
- 메모이제이션 기법을 사용함 > 이전에 계산한 값을 저장하여, 다시 계산하지 않도록 하여 실행 속도를 빠르게 하는 기법
- 부분 문제는 중복되어 재활용 됨. > 피보나치 수열
분할 정복
- 문제를 나눌 수 없을 때까지 나누어서 각각을 풀면서 다시 합병하여 문제의 답을 얻는 알고리즘
- 하양식 접근 > 일반적으로 재귀함수로 구현
- 문제를 잘게 쪼갤 때, 부분 문제는 서로 중복되지 않음 > 병합 정렬, 퀵 정렬
'''

def fibo(num):
    if num <= 1:
        return num
    return fibo(num-1) + fibo(num-2)

def fibo_dp(num):
    cache = [0 for i in range(num + 1)]
    cache[0] = 0
    cache[1] = 1

    for index in range(2, num + 1):
        cache[index] = cache[index - 1] + cache[index - 2]
    return cache[num]