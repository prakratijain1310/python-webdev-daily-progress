#l=[1,2,3,4,5]
#print(max(l))

l = [1, 2, 3, 4, 5]
smallest = l[0]
for i in l:
    if i < smallest:
        smallest = i
print(smallest)
