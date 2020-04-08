"""
Oppgave 5.5 - Oscillerende fjær
Author: Mohammed Shartaz Mostafa, Python 3
"""
# Importing the needed module
from matplotlib.pylab import *
# Define the variables
m = 9  # mass
A = 0.3  # Area
k = 4  # spring kkkontant
gamma = 0.15
y = lambda t: A*exp(-gamma*t)*cos(sqrt(k/m)*t)  # Define the function 

#a)
t_array, y_array = zeros(101), zeros(101)  # Creating 'empty' arrays with 101 zeros
for i in range(len(t_array)):  # Assigning values to indeces with for loop
    t_array[i] = i*25/100
    y_array[i] = y(t_array[i])
plot(t_array, y_array, label = "Looped")  # plotting 

#b)
# Creating array with linspace, running array through function
t_array = linspace(0,25,101); y_array = y(t_array)  
plot(t_array, y_array, label = "Vectorized")  # plotting...

#c)
grid("on"); xlabel("t [s]"); ylabel("y(t) [m]")
legend(loc = "best")
show()

"""
C:Users\moham\IN1900\Oblig5>python oscilating_spring.py
C:Users\moham\Anaconda3\lib\site-packages\matplotlib\cbook\deprecation.py:107: MatplotlibDeprecationWarning: Passing one of 'on', 'true', 'off', 'false' as a boolean is deprecated; use an actual boolean (True/False) instead.
  warnings.warn(message, mplDeprecation, stacklevel=1)
"""