# def printlog(func):
  #  def wrapper(*args, **kwargs):
   #     print("calling:"+func.__name__)
    #    return func(*args,**kwargs)
    # return wrapper

# def runlng_average(func):
#    data = {"total":0,"count":0}
#    def wrapper(*args,**kwargs):
#        val = func(*args,**kwargs)
#        data["total"]+=val
#        data["count"]+=1
#        print(f"Average of {func.__name__}so for:{data["total"]/data["counnt"]}")
#        return val
#    return wrapper
#@runlng_average
#def foo(x):
#    return x+2

#foo(x)

#def running_average(func):
#    data = {"total": 0, "count": 0}

#    def wrapper(*args, **kwargs):
#        val = func(*args, **kwargs)
#        data["total"] += val
#        data["count"] += 1
#        print(f"Average of {func.__name__} so far: {data['total'] / data['count']}")
#        return val

#    return wrapper

#@running_average
#def foo(x):
#    return x + 2

# Define x before using it
# you must later ask chat gpt to explain it to you

#foo(3)


#foo(5)

#calculate a sine wave and returns it back to you analogue data: continuous, digital data discrete
#this is supposed to calculate the data points and send them back to you 
#also add a damping factor to it to make it get little 

import math
import matplotlib.pyplot as plt

def calculate_and_plot_sine_wave(start, end, step):
    """
    Calculates the sine wave points from 'start' to 'end' with the given 'step',
    and then plots the wave.

    Args:
        start (float): Starting x-value (in radians)
        end (float): Ending x-value (in radians)
        step (float): Step size between x-values

    Returns:
        List[Tuple[float, float]]: List of (x, sin(x)) graphing points
    """
    x_values = []
    y_values = []

    x = start
    while x <= end:
        x_values.append(x)
        y_values.append(math.sin(x))
        x += step

    # Plotting
    plt.plot(x_values, y_values, label="sin(x)")
    plt.title("Sine Wave")
    plt.xlabel("x (radians)")
    plt.ylabel("sin(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

    return list(zip(x_values, y_values))

def add_plot(func):
    wrapper

#plot as a decoratorusing math 
#writting into a disk 
#@add_plot
#def sin(f=1,points=1000):
#    return np.sin(2*np.pi*f*(np.linspace(0,10,points)))
#using yield







