"""
Exercise E.2. Implement Euler’s midpoint method
Author: Mohammed Shartaz Mostafa
"""

# Imports
from ODESolver import ODESolver, ForwardEuler
import numpy as np
import matplotlib.pyplot as plt

class Midpoint(ODESolver):  # Creating a class that inherits from ODESolver
    def advance(self):  # Defining Euler Midpoint
        u,f,k,t = self.u,self.f,self.k,self.t
        dt = t[k+1]-t[k]
        v = u[k] + dt*f(u[k], t[k])/2
        u_new = u[k] + dt*f(v, t[k]+dt/2)
        return u_new

f = lambda u,t: t*np.cos(t)  # function
t = np.linspace(0,10,15)  # interval

mp = Midpoint(f)  # Instance of solver class
mp.set_initial_condition(0)
a = mp.solve(t)

fe = ForwardEuler(f)  # Forward Euler
fe.set_initial_condition(0)
b = fe.solve(t)

# Plotting
plt.title("Midpoint Euler")
plt.plot(a[1],a[0], label = "$Midpoint$")
plt.plot(b[1],b[0], label = "$Forward$")
plt.xlabel("x"); plt.ylabel("y(t)")
plt.legend(loc = "best")
plt.show()

"""
(base) c:Users\Bambi\Google Drive\PHYSX\PYT\IN1900\Oblig10>python Midpoint.py

"""