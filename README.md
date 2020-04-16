# Statistical treatment of GNSS data

GNSS recievers are used to establish geospatial coordinates. The [X, Y, Z] ouput will usualy contain gross errors and random noise.
This program aims to statistically remove the gross errors. 
[This](https://ieeexplore.ieee.org/abstract/document/7063664/) book is great for information about GNSS (and multisensor intergration).

This code has applicatons outside survey. 

Some sample generator is generated [here](https://github.com/ThomasJames/GNSS_Cleaning_3D/blob/master/Generate_Data.py)

The class performing the computations is [here](https://github.com/ThomasJames/GNSS_Cleaning_3D/blob/master/GNSSCleaner_Class.py)

Confidence levels. 95%, 98% and 99% are potential defaults. 

### Libraries needed

``` 
pip install numpy 
pip install matplotlib
pip install statistics 

```

### Visualised
<img src="https://github.com/ThomasJames/GNSS_Cleaning_3D/blob/master/Raw%20Data.png" width="280"> <img src="https://github.com/ThomasJames/GNSS_Cleaning_3D/blob/master/First%20Iteration.png" width="280"> <img src="https://github.com/ThomasJames/GNSS_Cleaning_3D/blob/master/Second%20Iteration.png" width="280">






