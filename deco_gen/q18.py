import random

def asg(a):
    for i in range(0,a+1):
        yield random.randint(1,3)
for j in asg(4):
    print(j)