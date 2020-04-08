"""
Exercise 4.11: Use exceptions to handle wrong input
Author: Mohammed Shartaz Mostafa (python 3.6.5)
"""
from sys import argv
g = 9.81
try:  # Asks python to try taking arguments from the command line.
    v0 = float(argv[1]); t = float(argv[2])
except IndexError:  # In case of IndexError, take user input instead.
    v0 = float(input("v0 = ")); t = float(input("t = "))
y = v0*t - 0.5*g*t**2
print(y)
"""
C:Users\moham\IN1900\Oblig4 python ball_cml_qa.py
v0 = 1
t = 3
-41.145
"""