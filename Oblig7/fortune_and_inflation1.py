"""
A.5: Solve a system of difference equations.
Authored by Mohammed Shartaz Mostafa.
Warning: This task has been delivered in an earlier course by me.
"""

import numpy as np
import matplotlib.pyplot as plt

F = 250E6  # Fortune
p = 4  # Annual interest
I = 3  # Inflation percentage
q = 1.  # Percent of interest consumed
y = 10  # Years

# Arrays and initial values
x = np.zeros(y+1); c = np.zeros(y+1); n = np.linspace(0,y,11)
x[0] = F; c[0] = (p*q/1E4)*F

# Solving recurrence relations
for i in range(1,y+1):
    c[i] = c[i-1] + (I/100.)*c[i-1]
    x[i] = x[i-1] + (p/100.)*x[i-1]-c[i-1]

# Plotting
plt.title("fortune_and_inflation1")
plt.plot(n, x, label = "Fortune")
plt.axis([0,10, 200E6, 500E6])
plt.grid("on")
plt.xlabel("n (years)")
plt.ylabel("Money")
plt.legend(loc = "best")
plt.show()

"""
(base) C:Users\dorth\Google Drive\PHYSX\PYT\IN1900\Oblig7>python fortune_and_inflation1.py
C:Users\dorth\Anaconda3\lib\site-packages\matplotlib\cbook\deprecation.py:107: MatplotlibDeprecationWarning: Passing one of 'on', 'true', 'off', 'false' as a boolean is deprecated; use an actual boolean (True/False) instead.
  warnings.warn(message, mplDeprecation, stacklevel=1)

"""
