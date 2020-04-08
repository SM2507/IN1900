"""
6.4: Interpret output from a program.
Authored by Mohammed Shartaz Mostafa.
"""

from numpy import array
import matplotlib.pyplot as plt  # Imports

with open("file","r") as out:  # Open file
    for i in range(24):  # Read the lines that will not be used
        out.readline()  

    epsilon = []  # Empty lists
    ex_error = []
    n = []

    for line in out:  # Substring indexing to extract needed information
        epsilon.append(float(line[9:14]))
        ex_error.append(float(line[29:37]))
        n.append(float(line[41:]))

epsilon = array(epsilon)
ex_error = array(ex_error)
n = array(n)

# Plotting
plt.title("read_error.py")
plt.semilogy(n,epsilon, label = "epsilon")
plt.semilogy(n,ex_error, label = "error")
plt.xlabel("x"); plt.ylabel("y"); plt.legend(loc = "best")
plt.show()

"""
(base) C:Users\Bambi\Google Drive\PHYSX\PYT\IN1900\Oblig8>C:/Users/Bambi/Anaconda3/pythonw.exe "c:Users/Bambi/Google Drive/PHYSX/PYT/IN1900/Oblig8/read_error.py"

"""
