"""
Exercise: 1.2 Population growth
Author: Mohammed Shartaz Mostafa (python 3.6.5)
"""
from numpy import exp

# Defining variables
B = 50000; k = 0.2; C = 9

# Defining a function 
def N(t):
    return B/(1+C*exp(-k*t))  # Returning the wanted function

print("The bacterium population is {:d} bacteria after 24 hours.".format(int(N(24))))

"""
Run program
The bacterium population is 46551 bacteria after 24 hours.
"""