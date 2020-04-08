"""
Exercise 5.1. Fill arrays; loop version
Author: Mohammed Shartaz Mostafa
"""
from numpy import log, zeros  # Importing necessary modules
f = lambda x: log(x)  # Defining function

N = 101
x,y = zeros(N), zeros(N)  # Creating empty arrays
for i in range(N):  # Assigning values to indeces with for loop
    x[i] = 1+i*9/100
    y[i] = f(x[i])

"""
C:Users\moham\IN1900\Oblig5>python fill_log_arrays_loop.py
"""

