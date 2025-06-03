def printlog(func):
    def wrapper(arg):
        print("calling:" + func.__name__)
        return func(arg)  # fixed here
    return wrapper

@printlog
def foo(x):
    print(x + 2)

foo(3)
