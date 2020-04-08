"""
Exercise 5.32: Plot Taylor polynomial approximations to sin x
Author: Mohammed Shartaz Mostafa
Warning: This task has been delivered in an earlier course by me. 
"""
from math import factorial
import matplotlib.pyplot as plt
import numpy as np

# a)
def S(x, n):  # Defining the function for calculating the sum
    s = 0
    j = 0
    while j <= n:
        s = s + ((-1)**j) * ((x**(2*j+1))/factorial(2*j+1))
        j += 1
    return s

# b)

x = np.linspace(0, 4*np.pi, 1000)  # Array containing the values for x

plt.title("plot_Taylor_sin.py")
plt.plot(x, S(x,1), label = "S(x; 1)")  # 3rd degree Taylor approximation
plt.plot(x, S(x,2), label = "S(x; 2)")  # 5th degree Taylor approximation
plt.plot(x, S(x,3), label = "S(x; 3)")  # 7th degree Taylor approximation
plt.plot(x, S(x,6), label = "S(x; 6)")  # 13th degree Taylor approximation
plt.plot(x, S(x,12), label = "S(x; 12)")  # 25th degree Taylor approximation
plt.plot(x, np.sin(x), label = "sin x   [0, 4pi]", linewidth = 2)  # Exact function
plt.xlabel("x"); plt.ylabel("y"); plt.grid("on")
plt.legend(loc = "best", fontsize = "small"); plt.axis([0,4*np.pi,-1.5,1.5])
plt.show()

"""
(base) C:Users\dorth\Google Drive\PHYSX\PYT\IN1900\Oblig7>python plot_Taylor_sin.py
C:Users\dorth\Anaconda3\lib\site-packages\matplotlib\cbook\deprecation.py:107: MatplotlibDeprecationWarning: Passing one of 'on', 'true', 'off', 'false' as a boolean is deprecated; use an actual boolean (True/False) instead.
  warnings.warn(message, mplDeprecation, stacklevel=1)
"""