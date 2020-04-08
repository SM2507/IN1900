"""
Exercise E.1. Decrease the length of the time steps
Author: Mohammed Shartaz Mostafa
"""

# Imports
import numpy as np 
import matplotlib.pyplot as plt
from ODESolver import ForwardEuler

# List of ns
n_range = [20,30,35,40,50,100,1000,10000]


def f(u,t):
    return np.cos(6*t)/(1+t+u)


U0 = 0  # Initial condition
f20 = ForwardEuler(f)  # Instance of class ForwardEuler
f20.set_initial_condition(U0)  # Set initial condition

plt.title("Decrease dt")
for n in n_range:  # Plotting everything 
    #plt.clf()  # Clear frame
    t = np.linspace(0,10,n)  # Varying n
    s = f20.solve(t)  # Solve for interval t
    plt.plot(s[1],s[0], label = "Approximation n = {}".format(n))  # Plot
    plt.xlabel("t"); plt.ylabel("u")
    #plt.axis([0,10,0.9,1.2])  # Locking the axes
    plt.legend(loc = "best")
    #plt.pause(1)  # Freeze frame, 1 second
plt.show()

"""
(base) c:Users\Bambi\Google Drive\PHYSX\PYT\IN1900\Oblig10>python decrease_dt.py

"""

