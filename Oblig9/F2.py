"""
Exercise 7.11: Implement special methods in a class
Author: Mohammed Shartaz Mostafa
"""

from math import exp, sin
class F:
    def __init__(self,a,w):  # Constructor assigns initial values
        self.a = a
        self.w = w

    def value(self,x):
        return exp(-self.a*x)*sin(self.w*x)

 # Rather than changing the previous method, this magic method makes the instance callable and calls on value()
    def __call__(self,x): 
        return self.value(x)

    def __repr__(self):  # __repr__ returns a printable representation of the object, alternatively __str__
        return "exp(-a*x)*sin(w*x)"

"""
(base) C:Users\dorth\Google Drive\PHYSX\PYT\IN1900\Oblig9>python F2.py

"""

# Interactive session

"""
(base) C:Users\dorth\Google Drive\PHYSX\PYT\IN1900\Oblig9>python
Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from F2 import F
>>> f = F(1,0.1)
>>> from math import pi
>>> print(f(pi))
0.01335383513703555
>>> f.a = 2
>>> print(f(pi))
0.0005770715401197441
>>> print(f)
exp(-a*x)*sin(w*x)
>>>
"""