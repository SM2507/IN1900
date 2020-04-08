"""
Oppgave 6.2: Lese og bruke fysiske konstanter
Author: Mohammed Shartaz Mostafa
"""

# a)

with open("physics_constants.dat", "r") as file_:  # Opening the file and making the dictionary 
    P_C = {(line.split(":")[1].split()[0]): float((line.split(":")[1].split()[1]))\
for line in file_}  # Using dictionary comprehension to assign keys and values 

# b)

# Variables
c = P_C["c"]
g = P_C["g"]
G = P_C["G"]
h = P_C["h"]
hbar = P_C["hbar"]
e = P_C["e"]
a0 = P_C["a0"]
ke = P_C["ke"]
me = P_C["me"]

print( "Energy level n = 1:", (ke**2*me*e**4)/(2*hbar**2))
print( "In eV:", (ke**2*me*e**4)/(2*hbar**2)*6.24150913E18)

"""
(base) C:Users\dorth\Google Drive\PHYSX\PYT\IN1900\Oblig7> python constants_hydrogen.py
Energy level n = 1: 2.1798723086817252e-18
In eV: 13.605692916871167
"""






