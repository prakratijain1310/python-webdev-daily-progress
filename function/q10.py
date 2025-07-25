def ispal(*str):
    for i in str:
        print(i)
        if i==i[::-1]:
            return True

print(ispal("nitin","jahaj"))