"""
Exercise 4.9: Prompt the user for input to a formula
Author: Mohammed Shartaz Mostafa (pyhton 3.6.5)
"""
# Using the input function to get user input. 
# By default the input function reads user input as a string, hence the conversion.
v0 = float(input("v0 = ")); g = 9.81; t = float(input("t = "))
y = v0*t - 0.5*g*t**2
print(y)

"""
C:Users\moham\IN1900\Oblig4>python ball_qa.py
v0 = 10
t = 2
0.379999999999999
"""