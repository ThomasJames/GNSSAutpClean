import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statistics import stdev
from GNSSCleaner_Class import GNSSCleaner
from Generate_Data import X_raw, Y_raw, Z_raw

if __name__=="__main__":

    """
    Raw Data
    """
    # Standard deviation = SD of X x Y x Z (Plotting)
    X_sd, Y_sd, Z_sd = stdev(X_raw), stdev(Y_raw), stdev(Z_raw)
    sd = X_sd * Y_sd * Z_sd

    # Plot Raw data
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.grid(False)
    ax.scatter(X_raw, Y_raw, Z_raw, color="skyblue")
    ax.scatter(np.average(X_raw), np.average(Y_raw), np.average(Z_raw), color="salmon", s=sd)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title("Raw Data")
    ax.set_xlim3d(5, 15)
    ax.set_ylim3d(5, 15)
    ax.set_zlim3d(5, 15)
    plt.show()

    """
    First Iteration
    """

    result = GNSSCleaner(X_raw, Y_raw, Z_raw, CI99=True)
    x_out, y_out, z_out = (result.clean())

    # Plot first iteration:
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
    ax.set_title("First Iteration")
    ax.set_xlim3d(5, 15)
    ax.set_ylim3d(5, 15)
    ax.set_zlim3d(5, 15)
    plt.show()

    """
    Second Iteration
    """

    result = GNSSCleaner(x_out, y_out, z_out, CI99=True)
    x_out, y_out, z_out = (result.clean())

    # Plot second iteration:
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
    ax.set_title("Second Iteration")
    ax.set_xlim3d(5, 15)
    ax.set_ylim3d(5, 15)
    ax.set_zlim3d(5, 15)
    plt.show()

