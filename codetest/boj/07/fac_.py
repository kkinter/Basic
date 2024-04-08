def fac(n):
    if(n > 1):
        return n *fac(n-1)
    else:
        return 1

def home(k,n):
    cnt = 0
    li = [x for x in range(1,15)]
    li2 = []
    if cnt <= k:
        for i in li:
            li2.append(((1+i)*i)/2)
        cnt += 1
