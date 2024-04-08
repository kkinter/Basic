s, k, h = map(int, input().split())
sum_val = s + k + h
if sum_val >= 100:
    print('OK')
else:
    min_val = min(s, k, h)
    if min_val == s:
        print('Soongsil')
    elif min_val == k:
        print('Korea')
    elif min_val == h:
        print('Hanyang')