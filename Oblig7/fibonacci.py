"""
Exercise A.2. Solve a difference equation numerically
Author: Mohammed Shartaz Mostafa
"""

from numpy import zeros

n = 15  # number of iterations
x = zeros(n); x[0] = 1; x[1] = 1  # Empty array, and initial values

for i in range(2,n):  # For loop for solving recurrence relation
    x[i] = x[i-1] + x[i-2]

for i in range(n):  # Printing the first 15 elements
    print(x[i])

"""
(base) C:Users\dorth\Google Drive\PHYSX\PYT\IN1900\Oblig7>python fibonacci.py
1.0
1.0
2.0
3.0
5.0
8.0
13.0
21.0
34.0
55.0
89.0
144.0
233.0
377.0
610.0
"""