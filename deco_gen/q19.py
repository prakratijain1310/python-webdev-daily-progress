'''def dec(func):
    def wrapper():
        return 3+2
    return wrapper()
@dec 
def asdf():
    return 9'''

'''def decorator(func):
    def wrap(*a, **b):
        print(f"Calling with a: {a}, b: {b}")
        result = func(*a,**b)
        print(f"returned: {result}")
        
        return result
    return wrap
@decorator
def multiply_numbers(x, y):
    return x * y

result = multiply_numbers(10, 20)
print("Result:", result)'''


def decorator(func):
    def wrap(a, b):
        print(f"a: {type(a)}, b: {type(b)}")
        result = func(a,b)
        print(f"returned: {result}")
        
        return result
    return wrap
@decorator
def typecheck(x, y):
    return type(x)==type(y)

result = typecheck(10, 20)
print("Result:", result)
