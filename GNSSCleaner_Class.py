import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statistics import stdev

"""
x_raw - List of X coordinates
y_raw - List of Y coordinates
z_raw - List of Z coordinates
CI99/CI98/CI95 - % confidence levels 99%/98%/95% respectivley 
"""

class GNSSCleaner:

    def __init__(self, x_raw, y_raw, z_raw, CI99=True, CI98=False, CI95=False):

        # Confidence level options.
        if CI99:
            ci = 2.58

        if CI98:
            ci = 2.33

        if CI95:
            ci = 1.96

        self.x_raw = x_raw
        self.y_raw = y_raw
        self.z_raw = z_raw
        self.ci = ci

    def clean(self):

        # Retrieve Z-scores, put them in a list.
        z_x = list(stats.zscore(self.x_raw))
        z_y = list(stats.zscore(self.y_raw))
        z_z = list(stats.zscore(self.z_raw))

        x, y, z = [], [], []
        
        # If Z-Scores are within confidence level.
        for i in range(len(z_x)):
            if self.ci > z_x[i] > -self.ci: # For x
                if self.ci > z_y[i] > -self.ci: # For y
                    if self.ci > z_z[i] > -self.ci: # For z
                        # Put the raw value back in the list
                        x.append(self.x_raw[i]), y.append(self.y_raw[i]), z.append(self.z_raw[i])
            else:
                # Exclude the value 
                x.append(None), y.append(None), z.append(None)

        x_c, y_c, z_c = [], [], []

        # Get rid of None values.    
        x_c = [i for i in x if i]
        y_c = [i for i in y if i]
        z_c = [i for i in z if i]

        # Tell user how many values have had to be removed. 
        print(len(self.x_raw) - len(x_c), " values removed")

        return x_c, y_c, z_c
