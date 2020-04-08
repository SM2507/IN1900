"""
Exercise 2.6: Table showing population growth.
Author: Mohammed Shartaz Mostafa (python 3.6.5)
"""

from numpy import exp  # Importing Euler's number to the power of...

# Defining variables
B = 50000; k = 0.2; C = 9
# Defining a function 
def N(t):
    return B/(1+C*exp(-k*t))  # Returning the wanted function

# See comments from ball_table2.py for explaination 
t = [i for i in range(0,48+1,4)]
N = [N(t[i]) for i in range(len(t))]

print("{:15s}{:>15s}".format("Time[h]","Popluation"))
for val in zip(t,N):
    print("{:<15d}{:>15d}".format(int(val[0]),int(val[1])))

"""
C:Users\moham\Google Drive\PHYSX\PYTHON FLS\IN1900\Oblig2>python population_table.py
Time[h]             Popluation
0                         5000
4                         9912
8                        17748
12                       27526
16                       36580
20                       42924
24                       46551
28                       48389
32                       49263
36                       49666
40                       49849
44                       49932
48                       49969
"""