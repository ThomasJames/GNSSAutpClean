import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statistics import stdev
from GNSSCleaner_Class import GNSSCleaner

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

result = GNSSCleaner(X_raw, Y_raw, Z_raw, CI99=True)
x_out, y_out, z_out = (result.clean())


# Standard deviation = SD of X x Y x Z (Plotting)
X_sd, Y_sd, Z_sd = stdev(x_out), stdev(y_out), stdev(z_out)
sd = X_sd * Y_sd * Z_sd
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.grid(False)
ax.scatter(x_out, y_out, z_out, color="skyblue")
ax.scatter(np.average(x_out), np.average(y_out), np.average(z_out), color="salmon", s=sd)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

