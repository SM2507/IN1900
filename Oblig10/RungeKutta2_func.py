"""
Exercise E.30: Implement a 2nd-order Runge-Kutta method; function
Author: Mohammed Shartaz Mostafa
"""

import numpy as np
import matplotlib.pyplot as plt

# Solving xy' + y = e^x   y(1) = 2

def RungeKutta2(f,u0,T,n):
    u = np.zeros(n); t = np.zeros(n)
    t[0] = 1
    u[0] = u0  # Initial value
    dt = (T-t[0])/n  # T is the interval from 0 to T
    for k in range(1,n):  # RK 2nd order recurrence relation
        t[k] = dt + t[k-1]
        K1 = dt*f(u[k-1],t[k-1])
        K2 = dt*f(u[k-1]+.5*K1, t[k-1]+.5*dt)
        u[k] = u[k-1]+K2
    return t,u  # Return t and u

def f(u,t):  # y' = f(u,t)
    return (np.e**t-u)/t

RKn5 = RungeKutta2(f,2,10,5)  # dt is reduced at the same rate as n increases
RKn10 = RungeKutta2(f,2,10,10)

def exact(t):
    return (np.e**t+2-np.e)/t
    
t = np.linspace(1,10,100)  # For exact

# Plotting
plt.title("RungeKutta 2nd order") 
plt.plot(t, exact(t), label = "Exact")
plt.plot(RKn5[0], RKn5[1], label = "n = 5")
plt.plot(RKn10[0], RKn10[1], label = "n = 10")
plt.xlabel("x"); plt.ylabel("y(x)")
plt.legend( loc = "best")
plt.show()

"""
C:Users\Bambi\Google Drive\PHYSX\PYT\IN1900\Oblig10>python RungeKutta2_func.py

"""