"""
Exercise 9.2: Make polynomial subclasses of parabolas
Author: Mohammed Shartaz Mostafa
"""

# Parent class provided in the task
class Line(object):
    def __init__(self,c1,c0):
        self.c0 = c0
        self.c1 = c1

    def __call__(self,x):
        print("Line")
        return self.c0 + self.c1*x

    def table(self,L,R,n):
        s = ''
        import numpy as np
        for x in np.linspace(L,R,n):
            y = self(x)
            s += '%12g %12g\n' %(x, y)
        return s


class Parabola(Line):  # Creating a class which Cubic is supposed to inherit from
    def __init__(self,c2,c1,c0):
        Line.__init__(self,c1,c0)  # Using the parent class' __init__ method to assign c1 and c0
        self.c2 = c2

    def __call__(self,x):
        print("Parabola")
        return self.c2*x**2+self.c1*x+self.c0

    def table(self,L,R,n):
        s = ''
        import numpy as np
        for x in np.linspace(L,R,n):
            y = self(x)
            s += '%12g %12g\n' %(x, y)
        return s

class Cubic(Parabola):  # Class Cubic, which Poly4 is going to inherit from
    def __init__(self, c3, c2, c1, c0):
        Parabola.__init__(self,c2,c1,c0)
        self.c2 = c2
        self.c3 = c3

    def __call__(self,x):
        print("Cubic")
        return self.c3*x**3+self.c2*x**2+self.c1*x+self.c0

  # Making a table method is unnecessary since it already exists due to inheritance.
  # Making another would simply override the method which is inherited, as done in Parabola.


class Poly4(Cubic):
    def __init__(self,c4,c3,c2,c1,c0):
        Cubic.__init__(self,c3,c2,c1,c0)
        self.c4 = c4

    def __call__(self,x):
        print("Poly4")
        return self.c4*x**4+self.c3*x**3+self.c2*x**2+self.c1*x+self.c0


cubic = Cubic(1,1,1,0)
poly = Poly4(2,4,4,2,0)

print(cubic.table(0,5,6))
print(poly.table(0,5,6))

"""
(base) C:Users\dorth\Google Drive\PHYSX\PYT\IN1900\Oblig9>python Cubic_Poly4.py
Cubic
Cubic
Cubic
Cubic
Cubic
Cubic
           0            0
           1            3
           2           14
           3           39
           4           84
           5          155

Poly4
Poly4
Poly4
Poly4
Poly4
Poly4
           0            0
           1           12
           2           84
           3          312
           4          840
           5         1860

"""
