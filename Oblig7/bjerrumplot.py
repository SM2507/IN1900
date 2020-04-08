"""
Oppgave 5.5: Bjerrumplot
Author: Mohammed Shartaz Mostafa
"""

from matplotlib import pylab  # Pylab contains numpy and pyplot modules

# a)

# Equilibrium constants 
K1 = 5.01E-7
K2 = 4.79E-11

pH = pylab.linspace(4,12,1000)  # pH values between 4 and 12

cH = 10**((-1)*pH)  # The concentratrion of H+ ions in equilibrium solution
cCO2 = cH**2/(cH**2+K1*cH+K1*K2)  # Concentration of dissolved CO2 
cHCO3 = (K1*cH)/(cH**2+K1*cH+K1*K2)  # Concentration of dissolved HCO3
cCO3 = (K1*K2)/(cH**2+K1*cH+K1*K2)  # Concentration of dissolved CO3

# Plotting
pylab.title("Concentrations")
pylab.grid("on")
pylab.plot(pH,cCO2, label = "$[CO_2 (aq)]$")
pylab.plot(pH,cHCO3, label = "$[HCO_3^{-} (aq)]$")
pylab.plot(pH,cCO3, label = "$[CO_3^{2-} (aq)]$")
pylab.xlabel("pH")
pylab.ylabel("M $(mol/L)$")
pylab.legend(loc = "best")

idx = pylab.argwhere(pylab.diff(pylab.sign(cCO2 - cHCO3))).flatten()
pylab.plot(pH[idx], cCO2[idx], 'ro')  # Point of intersection between cCO2 and cCHO3

idy = pylab.argwhere(pylab.diff(pylab.sign(cCO3 - cHCO3))).flatten()
pylab.plot(pH[idy], cCO3[idy], 'bo')  # Point of intersection between cCO3 and cCHO3

pylab.show()

# b)
tup = (pH[idx][0], cCO2[idx][0])  # The coordinates for the point of intersection
print("The point of intersection between cCO2 and cHCO3 is {}".format(\
tup))

tup = (pH[idy][0], cCO2[idy][0])
print("The point of intersection between cCO3 and cHCO3 is {}".format(\
tup))

"""
(base) C:Users\dorth\Google Drive\PHYSX\PYT\IN1900\Oblig7>python bjerrumplot.py
C:Users\dorth\Anaconda3\lib\site-packages\matplotlib\cbook\deprecation.py:107: MatplotlibDeprecationWarning: Passing one of 'on', 'true', 'off', 'false' as a boolean is deprecated; use an actual boolean (True/False) instead.
  warnings.warn(message, mplDeprecation, stacklevel=1)
The point of intersection between cCO2 and cHCO3 is (6.298298298298299, 0.5010491905072781)
The point of intersection between cCO3 and cHCO3 is (10.318318318318319, 4.802481109982548e-05)
"""
