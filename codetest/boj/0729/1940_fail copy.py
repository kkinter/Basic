import sys
from turtle import st
input = sys.stdin.readline

n = int(input())    
m = int(input())
numbers = list(map(int, input().split()))
cnt = 0
numbers = sorted(numbers, reverse= True)

st = 0
en = 2
sum_val = 0
while en < n:
    if numbers[st] + numbers[en] < m:
        


print(cnt)