import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from random import randrange

data_1 = [randrange(0, 10) for _ in range(0, 10)]
data_2 = [randrange(0, 10) for _ in range(0, 10)]

fig, ax = plt.subplots()
p, = ax.plot(data_1)

plt.subplots_adjust(left=0.1, bottom=0.25)

axfreq = plt.axes([0.1, 0.1, 0.8, 0.05])
slider = Slider(
    ax=axfreq,
    label='Offset',
    valmin=-5,
    valmax=5,
    valinit=0,
)


def update(val):
    data_2 = [x+val for x in data_1]
    p.set_ydata(data_2)


slider.on_changed(update)
plt.show()
