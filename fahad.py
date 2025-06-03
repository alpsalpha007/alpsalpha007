import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation
cpu_data = []
def update(frame):
    cpu_data.append(psutil.cpu_percent())
    if len(cpu_data)>60:
        cpu_data.pop(0)
    plt.cla()
    plt.plot(cpu_data)
    plt.title("Real timw cpu usage")
    plt.ylim(0,100)
fig=plt.figure()
ani=animation.FuncAnimation(fig,update,interval=1000)
plt.show()
                 