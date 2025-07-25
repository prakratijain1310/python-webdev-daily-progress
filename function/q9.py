'''
def fact(a):
    fact=1
    for i in range(1,a+1):
        fact*=i
    return fact
print(fact(4))
'''
def fact(a):
    if a==0 or a==1:
        return 1
    return a*fact(a-1)
print(fact(8))
