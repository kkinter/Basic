t = int(input())
for i in range(t):
    P, Q, R, S, W = map(int,input().split())
    a_price = 0
    b_price = 0
    if W > R:
        a_price = P*W
        b_price = Q + S*(W-R)
        print(f"#{i+1} {min(a_price,b_price)}")
    else:
        a_price = P*W
        b_price = Q
        print(f"#{i+1} {min(a_price,b_price)}")

