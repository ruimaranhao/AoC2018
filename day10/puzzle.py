import numpy as np
import re
import matplotlib.pyplot as plt

def steps_minimize_variance(p, v):
    px = p[:, 0]
    vx = v[:, 0]

    mu = np.mean(px)
    ev = np.mean(vx)
    t = np.mean((mu - px) / (vx - ev))

    t = int(round(t))

    return t


with open('inp0') as file:
    data = []
    for line in file.readlines():
            match = re.match(r'position=<\s*(?P<px>-?\d+),\s*(?P<py>-?\d+)> velocity=<\s*(?P<vx>-?\d+),\s*(?P<vy>-?\d+)>', line).groupdict()
            data.append([int(match['px']), int(match['py']), int(match['vx']), int(match['vy'])])

data = np.array(data, dtype=np.float32)
p, v = data[:, :2], data[:, 2:]

t = steps_minimize_variance(p, v)

print(t)

plt.plot(*(p + t*v).T, ls='', marker='8', color='k')
plt.gca().invert_yaxis()
plt.axis('equal')
plt.show()
