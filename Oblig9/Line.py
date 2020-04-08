"""
7.6: Make a class for straight lines.
Authored by Mohammed Shartaz Mostafa.
Warning: This task has been delivered in an earlier course by me. 
"""
# Creating class
class Line:
# Constructor
    def __init__(self, p1, p2):
        self.p1 = p1; self.p2 = p2
# Value method
    def value(self, x):
# a here is the slope of the line.
# b is the point of intersection between the line created and the y axis.
        a = (self.p2[1] - self.p1[1])/(self.p2[0] - self.p1[0])
        b = self.p1[1] - a*self.p1[0]
        func = a*x + b
        return func


# Test function
def test_Line():  # Task said to make a test function, not a method. This is the result in said case.
    val_exp1 = 0.25; val_exp2 = -1.0; val_exp3 = 1.5
    val_com1 = Line((0,-1), (2,4)).value(0.5)
    val_com2 = Line((0,-1), (2,4)).value(0)
    val_com3 = Line((0,-1), (2,4)).value(1)
    msg = "Error in the value method."
    assert val_exp1==val_com1 and val_exp2==val_com2 and val_exp3==val_com3
    assert msg

test_Line()
"""
(base) C:Users\dorth\Google Drive\PHYSX\PYT\IN1900\Oblig9>python Line.py

"""

# interactive session
"""
(base) C:Users\dorth\Google Drive\PHYSX\PYT\IN1900\Oblig9>python
Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32                     Type "help", "copyright", "credits" or "license" for more information.
>>> from Line import Line
>>> line = Line((0,-1),(2,4))
>>> print(line.value(.5), line.value(0), line.value(1))
0.25 -1.0 1.5
>>> test_Line()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'test_Line' is not defined
>>>
"""