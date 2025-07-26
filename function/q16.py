n=int(input("Enter the number"))
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
    continue

if sum(l)==n:
    print("Perfect") 
else:
    print("HAHAH")



