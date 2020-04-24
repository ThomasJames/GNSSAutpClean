# Statistical treatment of GNSS data

GNSS recievers are used to establish geospatial coordinates. The [X, Y, Z] ouput will always contain gross and random errors.
The purpose of this program is to remove the gross errors using Z-Scores. 
[This](https://ieeexplore.ieee.org/abstract/document/7063664/) book is great for information about GNSS (and multisensor intergration).

Some sample generator is generated [here](https://github.com/ThomasJames/GNSS_Cleaning_3D/blob/master/Generate_Data.py)

The class performing the computations is [here](https://github.com/ThomasJames/GNSS_Cleaning_3D/blob/master/GNSSCleaner_Class.py)

Confidence levels can be adjusted. 95%, 98% and 99% are potential defaults as these are most often used. 

### Libraries needed

``` 
pip install numpy 
pip install matplotlib
pip install statistics 
pip install seaborn
pip install scipy

```

### Visualised

Eg: A GNSS Reciever is placed at 10m North, 10m East and a height of 10m. 

<img src="https://github.com/ThomasJames/GNSS_Cleaning_3D/blob/master/Plots/Raw%20Data.png" width="280"> <img src="https://github.com/ThomasJames/GNSS_Cleaning_3D/blob/master/Plots/First%20Iteration.png" width="280"> <img src="https://github.com/ThomasJames/GNSS_Cleaning_3D/blob/master/Plots/Second%20Iteration.png" width="280">

<img src="https://github.com/ThomasJames/GNSS_Cleaning_3D/blob/master/Plots/Raw%20DataZ-Scores.png" width="280"> <img src="https://github.com/ThomasJames/GNSS_Cleaning_3D/blob/master/Plots/First%20IterationZ-Scores.png" width="280"> <img src="https://github.com/ThomasJames/GNSS_Cleaning_3D/blob/master/Plots/Second%20IterationZ-Scores.png" width="280">





