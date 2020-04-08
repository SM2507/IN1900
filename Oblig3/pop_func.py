"""
Exercise 3.1. Implement a function for population growth
Author: Mohammed Shartaz Mostafa
"""
from numpy import exp

def population(t,k,B,C):  # Defining the function 
    return B/(1+C*exp(-k*t))  # Returning given function

t = [i for i in range(0,48+1,4)]  # Making a list of time values between 0 and 48
N = [population(t[i],0.2,50000,9) for i in range(len(t))]  
# Calling the function using list comprehension

print("{:15s}{:>15s}".format("Time[h]","Popluation"))  # Header
for val in zip(t,N):  # Creating tuples of t and population(t)
    print("{:<15d}{:>15d}".format(int(val[0]),int(val[1])))  # Printing the values

"""
C:Users\moham\Google Drive\PHYSX\PYTHON FLS\IN1900\Oblig3>python pop_func.py
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