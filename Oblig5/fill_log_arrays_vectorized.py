"""
Exercise 5.2. Fill arrays; vectorized version
Author: Mohammed Shartaz Mostafa
"""
# Importing necessary modules
from numpy import log, linspace
# Defining function, creating array with linspace, running array through function.
f = lambda x: log(x)
x = linspace(1,10,101)
f(x)

"""
C:Users\moham\IN1900\Oblig5>python fill_log_arrays_vectorized.py
"""