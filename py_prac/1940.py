t = int(input()) # 10
for i in range(t):  
    speed = 0
    distance = 0
    n = int(input()) # 2
    for j in range(n):
        li = list(map(int,input().split()))
        if len(li) == 1:
            distance += speed
        elif li[0] == 1:
            speed += li[1]
            distance += speed
        elif li[0] == 2:
            speed -= li[1]
            if speed < 0:
                speed = 0
            distance += speed
    print(f"#{i+1} {distance}")
  