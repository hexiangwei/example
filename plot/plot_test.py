import random
import matplotlib.pyplot as plt
import time

x = []
y = []


fig, ax = plt.subplots()
line, = ax.plot(x, y)

plt.ion()
plt.show(block=False)

for i in range(100):
    x.append(i)
    y.append(random.random())
    line.set_data(x, y)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw()
    time.sleep(1)

# plt.ioff()
plt.show()
