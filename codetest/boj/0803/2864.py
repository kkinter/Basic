a, b = map(str, input().split())
er_a = a
er_b = b

if '6' in a:
    er_a = a.replace('6','5')
if '6' in b:
    er_b = b.replace('6','5')

if '5' in a:
    a = a.replace('5','6')

if '5' in b:
    b = b.replace('5','6')


print(min(int(a) + int(b), int(er_a) + int(er_b)), max(int(a) + int(b), int(er_a) + int(er_b)))