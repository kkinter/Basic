t = int(input())

for i in range(t):
    arr = list(map(int,input().split()))
    st_arr = sorted(arr)
    st_arr.remove(min(st_arr))
    st_arr.remove(max(st_arr))
    print(f"#{i+1} {round(sum(st_arr)/8)}")