"""
Exercise: The spreading of a disease
Author: Mohammed Shartaz Mostafa
"""

import numpy as np  # Importing numpy
import matplotlib.pyplot as plt # Importing matplotlib
N = 50 # Weeks
# a)
x = np.zeros(N); x[0] = 100; x[1] = 150 # Empty array for avg. infection = 5/7, and initial values
y = np.zeros(N); y[0] = 100; y[1] = 150 # Empty array for avg. infection = 3/4, and initial values

for i in range(2,N):  # For-loop for solving recurrence relations with both infection rates
    x[i] = 1/4*x[i-1] + 5/7*x[i-2]
    y[i] = 1/4*x[i-1] + 3/4*x[i-2]

# Plotting
plt.title("Disease.py"); plt.grid("on")
plt.plot(np.array(range(N)),x, label = "$x_n$  IR = 5/7")
plt.plot(np.array(range(N)),y, label = "$y_n$  IR = 3/4")
plt.xlabel("Week")
plt.ylabel("Ill people")
plt.legend(loc = "best")
plt.show()

# b)
x0 = 100; x1 = 150  # Initial values

print(" Week            ill people")  # Header
print("___________________________")
print("   0                   %i" %(x0)) # N and infected people at week 0
print("   1                   %i" %(x1)) # N and infected people at week 1

for i in range(2,N):  # For-loop for calculating 
    x2 = 1/4*x1 + 5/7*x0
    x0 = x1  # Re-assigning "initial values" for the next iteration
    x1 = x2
    print(" {:>3d} {:21d}".format(i,int(x2)))  # Print the next values

"""
 C:Users\dorth\Google Drive\PHYSX\PYT\IN1900\Oblig7>python disease.py
C:Users\dorth\Anaconda3\lib\site-packages\matplotlib\cbook\deprecation.py:107: MatplotlibDeprecationWarning: Passing one of 'on', 'true', 'off', 'false' as a boolean is deprecated; use an actual boolean (True/False) instead.
  warnings.warn(message, mplDeprecation, stacklevel=1)
Week             ill people
___________________________
   0                   100
   1                   150
   2                   108
   3                   134
   4                   111
   5                   123
   6                   110
   7                   116
   8                   107
   9                   109
  10                   104
  11                   104
  12                   100
  13                    99
  14                    97
  15                    95
  16                    93
  17                    91
  18                    89
  19                    87
  20                    85
  21                    84
  22                    82
  23                    80
  24                    79
  25                    77
  26                    75
  27                    74
  28                    72
  29                    71
  30                    69
  31                    68
  32                    66
  33                    65
  34                    64
  35                    62
  36                    61
  37                    60
  38                    59
  39                    57
  40                    56
  41                    55
  42                    54
  43                    53
  44                    52
  45                    51
  46                    49
  47                    48
  48                    47
  49                    46
  """