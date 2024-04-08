import sys
sys.stdin = open("11047.txt")

n, m = map(int, (input()).split())
coin_arr = []
for i in range(n):
    coin = int(input())
    coin_arr.append(coin)
cnt = 0

# while m != 0:
#     for j in coin_arr[::-1]:
#         if m <= j:
#             m = m % j
#             cnt += (m // j)
#         print(m)
for coin in coin_arr[::-1]:
    if m >= coin:
        cnt += (m // coin)
        m = m % coin 
print(cnt)