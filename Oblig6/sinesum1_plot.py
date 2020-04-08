"""
Exercise 5.41: Plot sum-of-sines approximations to a function
Author: Mohammed Shartaz Mostafa (python 3.6.5)
Warning: This code has been delivered before by me, the only changes made were to 
translate the code from python 2.7 to python 3.
"""

import numpy as np  # Import numpy
import matplotlib.pyplot as plt  # Import matplotlib.pyplot

def S(t, n):  # Defining the approximate function
    i = 1  # Counter
    env = 0.0
    def c(i):
        return (1./(2.*i-1.)*np.sin((2*(2*i-1)*np.pi*t)/T))
    while i <= n:   # While loop
        env += c(i)  
        i += 1  # Increase counter
    env *=  4/np.pi
    return env

def f(t):  # Defining the exact function
    if 0 < t < T/2:
        return 1
    elif t == T/2:
        return 0
    elif T/2 < t < T:
        return -1

T = 2*np.pi
t = np.linspace(0.1, T, 5000)  # Creating an array from 0.1 to T, with 5000 elements
yft = np.array([f(t[i]) for i in range(len(t))])  # Running each element through the function

plt.grid("on")  # showing grid
plt.axis([0,T,-2,2])  # Defining the range of the axes
plt.plot(t, S(t, 1), label = 'S(t; 1)')  # plotting...
plt.plot(t, S(t, 3), label = 'S(t; 3)')
plt.plot(t, S(t, 20), label =   'S(t; 20)')
plt.plot(t, S(t, 200), label = 'S(t; 200)')
plt.plot(t, yft, label = "f(t)" )
plt.xlabel("t")  # naming the x axis
plt.ylabel("S(t; n)")  # naming the y axis
plt.legend(loc = "best")  # showing legend
plt.show()  # show graph

"""
C:Users\moham\Google Drive\PHYSX\PYTHON FLS\IN1900\Oblig6>python sinesum1_plot.py
C:Users\moham\Anaconda3\lib\site-packages\matplotlib\cbook\deprecation.py:107: MatplotlibDeprecationWarning: Passing one of 'on', 'true', 'off', 'false' as a boolean is deprecated; use an actual boolean (True/False) instead.
  warnings.warn(message, mplDeprecation, stacklevel=1)

"""