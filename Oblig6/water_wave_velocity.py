"""
Exercise 5.31: Explore a complicated function graphically
Author: Mohammed Shartaz Mostafa, Python 3
Warning: This code has been delivered before by me, the only changes made were to 
translate the code from python 2.7 to python 3.
"""
import numpy as np  # Import numpy
import matplotlib.pyplot as plt  # matplotlib.pyplot
# Defining variables
g = 9.81  # [m/s^2]
s = 7.9E-2  # [N/m]
rho = 1000  # [kg/m^3]
h = 50  # [m]
# Creating arrays
wavelength_small = np.linspace(0.001, 0.1, 2000)  
wavelength_big = np.linspace(1., 2000., 2000 )

# Defining function I'm going to plot
def c(wavelength):
    k = (g * wavelength)/(2* np.pi)
    l = (1 + ((s*4*np.pi**2)/(rho * g* wavelength**2)))
    m = np.tanh((2* np.pi*h)/wavelength)
    return np.sqrt(k*l*m)


plt.subplot(2,1,1); plt.grid("on")  # Using subplots to show to graphs in one plot
plt.title("Small wavelength")
plt.plot(wavelength_small, c(wavelength_small), label = "c(Wavelength)  [\
0.001m  ,     0.100m]")
plt.xlabel("Wavelength     [m]")
plt.ylabel("wave speed     [m/s]")
plt.legend(loc = "best")

plt.subplot(2,1,2); plt.grid("on")
plt.title("Large wavelength")
plt.plot(wavelength_big, c(wavelength_big), label = "c(Wavelength)  [1.0m \
 ,     2000.0m]")
plt.xlabel("Wavelength     [m]")
plt.ylabel("wave speed     [m/s]")
plt.legend(loc = "best")
plt.show()
"""
C:Users\moham\Google Drive\PHYSX\PYTHON FLS\IN1900\Oblig6>python water_wave_velocity.py
C:Users\moham\Anaconda3\lib\site-packages\matplotlib\cbook\deprecation.py:107: MatplotlibDeprecationWarning: Passing one of 'on', 'true', 'off', 'false' as a boolean is deprecated; use an actual boolean (True/False) instead.
  warnings.warn(message, mplDeprecation, stacklevel=1)
"""