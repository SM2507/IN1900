"""
Exercise 5.12: Plot exact and inexact Fahrenheit-Celsius conversion formulas
Author: Mohammed Shartaz Mostafa (python 3.6.5)
"""
from matplotlib.pylab import grid, plot, xlabel, ylabel, \
linspace, legend, show, title
  # Importing linspace and plot modules
approxC = lambda f:(f-30)/2  # Defining the approximate function
exactC = lambda f: (f-32)*5/9  # Defining the exact function
f = linspace(-20,120,1000)  # Creating an array with values ranging from -20 to 120, 1000 instances

title("f2c shortcut plot  ")
grid("on")  # Ensuring the grid is visible
plot(f,approxC(f), label = "Approximate")  # plotting and namng the approximate figure
plot(f,exactC(f), label = "Exact")  # plotting and namng the exact figure
xlabel("Farenheit"); ylabel("Celsius"); legend(loc = "best")  # naming x- and y-axis, adding legend
show()  # Shows plot

"""
C:Users\moham\Google Drive\PHYSX\PYTHON FLS\IN1900\Oblig6>python f2c_shortcut_plot.py
C:Users\moham\Anaconda3\lib\site-packages\matplotlib\cbook\deprecation.py:107: MatplotlibDeprecationWarning: Passing one of 'on', 'true', 'off', 'false' as a boolean is deprecated; use an actual boolean (True/False) instead.
  warnings.warn(message, mplDeprecation, stacklevel=1)
"""