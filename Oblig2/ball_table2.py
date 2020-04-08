"""
Exercise 2.9: Store values from a formula in lists
Author: Mohammed Shartaz Mostafa (python 3.6.5)
"""
from numpy import linspace  # Importing linspace to easily create an array with the desired values

v0 = 15; g = 9.81  # Defining the variables
yfun = lambda t: v0*t-0.5*g*t**2  # Defining the function y from the task

t = list(linspace(0,2*v0/g,10))  # Transforming the array into a list
# Using list comprehension to reduce lines of code, instead of list.append()
y = [yfun(t[i]) for i in range(len(t))]  


print("{:<10} {:>10} ".format("Time[s]","y(t)[m]"))  # Printing the header
for val in zip(t,y):  # Using the zip-function to create tuples of the elements in the lists
    print("{:>4.2f} {:14.2f}".format(val[0], val[1]))  # Printing the values for t and for y(t)
    

"""
C:Users\moham\Google Drive\PHYSX\PYTHON FLS\IN1900\Oblig2>python ball_table2.py
Time[s]       y(t)[m]
0.00           0.00
0.34           4.53
0.68           7.93
1.02          10.19
1.36          11.33
1.70          11.33
2.04          10.19
2.38           7.93
2.72           4.53
3.06          -0.00
"""