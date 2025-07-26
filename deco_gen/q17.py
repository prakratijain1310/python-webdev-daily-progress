
'''def asg(a):
    i=0
    while i<=a:
        yield i
        i+=1

for j in asg(4):
    print(j)
'''

def asg(a):
    for i in range(0,a+1):
        yield i**3
for j in asg(4):
    print(j)
