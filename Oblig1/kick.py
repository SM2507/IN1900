"""
Exercise 1.11: Compute the air resistance on a football
Author: Mohammed Shartaz Mostafa (python 3.6.5)
"""
from numpy import pi

# Defining the variables
m = 0.43  # kg
g = 9.81  # m/s^2
Rho = 1.2  # kg/m^3
a = 0.11  # m
A = pi*a**2  # m^2
C_D = 0.4  
V1 = 120/3.6  # m/s
V2 = 30/3.6  # m/s
F_g = m*g; F_d1 = 0.5*C_D*Rho*A*V1**2; F_d2 = 0.5*C_D*Rho*A*V2**2

print("F_d, the drag force: {:.1f} N, when initial velocity is \
{:.1f}m/s\n\
The ratio between the drag force and gravity force is {:.1f}".format(F_d1, V1, F_d1/F_g))
print("F_d, the drag force: {:.1f} N, when initial velocity is \
{:.1f}m/s\n\
The ratio between the drag force and gravity force is {:.1f}".format(F_d2, V2,F_d2/F_g))

"""
Run program
F_d, the drag force: 10.1 N, when initial velocity is 33.3m/s
The ratio between the drag force and gravity force is 2.4
F_d, the drag force: 0.6 N, when initial velocity is 8.3m/s
The ratio between the drag force and gravity force is 0.2
"""