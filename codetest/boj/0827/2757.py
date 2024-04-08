def pivot(n):
    if n == 0 or n == 1:
        return n
    else:
        return pivot(n) + pivot(n - 1)

print(pivot(5))