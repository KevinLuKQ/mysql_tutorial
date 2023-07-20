def cube(func):
    def wrapper():
        x = func()
        return x * x * x
    return wrapper
    
def square(func):
    def wrapper():
        x = func()
        return x * x
    
@square
@cube
def test():
    return 2


print(test())