'''
#zero division
def zerodiv(x,y):
    try:
        print (x/y)
    except:
        print("ZERO not allowed")
zerodiv(100,0)

#integer validation
try:
    n=int(input("Enter a number"))
    print(n)
except:
    print("Not an Integer")

#file not found
try:
    file_name=input("enter file name")
    with open (file_name,".txt","r") as f:
        lines=f.read()
except:
    print("File not Found")
#permission not given 
try:
    file_name=input("enter file name")
    with open (file_name,".txt","w") as f:
        lines=f.read()
except:
    print("not permitted to open the file")
'''

def zerodiv(x, y):
    try:
        print(x / y)
    except:
        print("Division by zero is not allowed")
    finally:
        print("Calculation attempt complete.")
    
    if y < 0:
        raise ValueError("Negative value not allowed")

zerodiv(100, 0)
