"""
Exercise 3.4. Half-wave rectifier
Author: Mohammed Shartaz Mostafa
"""
from numpy import sin, pi  # Importing modules 

def f(x):  # Defining the function given in the task.
    if sin(x) > 0:
        return sin(x)
    elif sin(x) <= 0:
        return 0

def testf(y,ext):
    in_put = y
    tol = 1e-9  # Defining the allowed error margin
    f_sin = f(in_put)  # Calculated value from function
    condition = abs(f_sin - ext) < tol  
    msg = "Error in the tested function. Values not congruent."
    assert condition, msg  # Asserting condition
    if condition:
        print("Success")

testf(-pi/2, 0)  # Calling the test function
testf(pi/2, 1)

"""
C:Users\moham\Google Drive\PHYSX\PYTHON FLS\IN1900\Oblig3>python half_wave.py
Success
Success
"""
