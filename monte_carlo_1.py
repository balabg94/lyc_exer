from random import random
def pi(n):
    count_in = 0
    for i in range(n):
        x = random()
        y = random()
        if (x**2 + y**2) <= 1:
            count_in +=1
    return count_in/n * 4

def test():
    return pi(10000000)
