"""
Exercise 4.10: Read parameters in a formula from the command line
Author: Mohammed Shartaz Mostafa (python 3.6.5)
"""
import sys as sys  # importing the sys module
# sys.argv[] takes arguments from the command line, by default as a string, hence the conversion.
# I start indexing from 1 to ensure that the file name is not taken as an argument.
v0 = float(sys.argv[1]); g = 9.81; t = float(sys.argv[2])
y = v0*t - 0.5*g*t**2
print(y)
"""
Run program
C: Users\moham\IN1900\Oblig4>python ball_cml.py 30 5
27.375
"""