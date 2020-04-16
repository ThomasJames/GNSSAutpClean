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
    return sum(data)/len(data)

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
def clean_data(X_raw, Y_raw, Z_raw):

    # CI = int(input("Confidence level: "))

    # CI = (CI / 100)/2
    # print(CI)
    # Define threshold

    X_z = stats.zscore(np.array(X_raw))
    Y_z = stats.zscore(np.array(Y_raw))
    Z_z = stats.zscore(np.array(Z_raw))

    print(X_z)

    X_clean = [None] * len(X_raw)
    Y_clean = [None] * len(Y_raw)
    Z_clean = [None] * len(Z_raw)

    for i in range(len(X_raw)):
        if X_z[i] > -1:
            X_clean[i] = X_raw[i]
            Y_clean[i] = Y_raw[i]
            Z_clean[i] = Z_raw[i]
        else:
            X_clean[i] = None
            Y_clean[i] = None
            Z_clean[i] = None

    for i in range(len(Z_clean)):
        print("X:" + str(X_clean[i]), "Y:" + str(Y_clean), "Z" + str(Z_clean))
          
print(clean_data(X_raw, Y_raw, Z_raw))











# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.grid(False)
# ax.scatter(X_raw, Y_raw, Z_raw, color="skyblue")
# # ax.scatter(np.average(X), np.average(Y), np.average(Z), color="salmon", s=sd)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.show()





    # for i in range(len(X_raw)):
    #     if X_z[i] > 3:
    #         X_clean.append(None)
    #         Y_clean.append(None)
    #         Z_clean.append(None)
    #     else:
    #         X_clean.append(X_raw[i])