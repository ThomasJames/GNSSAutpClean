import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statistics import stdev

"""
For some basic example data that reflects the nature of GNSS receiver.
The X, Y and Z coordinates are derived using a random normal function on python. 
generator through the numpy library.
"""

X_raw = [None] * 500
Y_raw = [None] * 500
Z_raw = [None] * 500


def mean(data):
    return sum(data) / len(data)

for i in range(500):
    X_raw[i] = np.random.normal(10)
    Y_raw[i] = np.random.normal(10)
    Z_raw[i] = np.random.normal(10)

# Standard deviation = SD of X x Y x Z (Plotting)
X_sd, Y_sd, Z_sd = stdev(X_raw), stdev(Y_raw), stdev(Z_raw)
sd = X_sd * Y_sd * Z_sd

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.grid(False)
ax.scatter(X_raw, Y_raw, Z_raw, color="skyblue")
ax.scatter(np.average(X_raw), np.average(Y_raw), np.average(Z_raw), color="salmon", s=sd)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

"""
Request confidence interval from user.
"""


def clean(x_raw, y_raw, z_raw):
    z_x = list(stats.zscore(x_raw))
    z_y = list(stats.zscore(y_raw))
    z_z = list(stats.zscore(z_raw))

    x, y, z = [], [], []

    for i in range(len(z_x)):
        if 1 > z_x[i] > -1:
            if 1 > z_y[i] > -1:
                if 1 > z_z[i] > -1:
                    x.append(x_raw[i]), y.append(y_raw[i]), z.append(z_raw[i])
        else:
            x.append(None), y.append(None), z.append(None)

    x_c, y_c, z_c = [], [], []

    for i in x:
        if x != None:
            x_c.append(i)

    for i in y:
        if y != None:
            y_c.append(i)

    for i in z:
        if z != None:
            z_c.append(i)

    print(len(x_raw) - len(x_c), " values removed")

    return x_c, y_c, z_c


x, y, z = (clean(X_raw, Y_raw, Z_raw))


