import random

from numpy import number

def lotto(n):
    for i in range(n):
        number = range(1,46)
        res = random.sample(number,6)
        res.sort()
        print(res)

lotto(5)