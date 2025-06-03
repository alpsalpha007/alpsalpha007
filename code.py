import datetime

def log_time(func):
    def day_time(arg):
        print(f'{func.__name__} is{datetime.datetime.now()}')
        return func(arg)
    return day_time

@log_time
def foo(x):
    print(x + 2)

foo(3)

#def my_pow():
 #   x = int(input("enter a number: "))
  #  print(x ** 3)

#my_pow()

def power(x,y):
    return x**y

input(power (x,y))
