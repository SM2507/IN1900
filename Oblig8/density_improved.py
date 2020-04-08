"""
Exercise 6.3: Use string operations to improve a program
Author: Mohammed Shartaz Mostafa
"""

# a)
# Defining a function.
def read_densities(filename):
    substance = []  # Empty lists
    densities = []
    with open(filename, "r") as den:
# For each line in the file "den", we are splitting each word and adding them
# to the list.
        for line in den:  # For every line in the file
        # Since the final element is the value of density, the substances are the elements before
            Substance = (line.split()[0:-1])  
            Substance = " ".join(Substance)  # Joining elements separated by space into one element
            substance.append(Substance)  # Append to list
            densities.append(float(line.split()[-1]))
    return(substance)  # Return list of substances

read_densities("densities.dat")

# b)

def read_densities2(filename):
    substance = []
    densities = []
    with open(filename, "r") as den:
        for line in den:
            # Substances stop at index 11, strip removes excess spaces
            substance.append((line[0:12]).strip())  
            # The next linereplaces the "\n" in the string with "", then turns them into floats
            densities.append(float((line[12:]).replace("\n","")))
    return(substance)

# c)

def test_read_densities():
    a = read_densities("densities.dat")  # Calls on function 
    b = read_densities2("densities.dat")
    for i in range(len(a)):
        assert a[i] == b[i], "Error in functions"  # Assert if the elements are equivalent

test_read_densities()

"""
(base) C:Users\dorth\Google Drive\PHYSX\PYT\IN1900\Oblig7>python density_improved.py

"""
