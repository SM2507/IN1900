"""
Exercise 4.14: Evaluate a formula for data in a file
Author: Mohammed Shartaz Mostafa
Warning: Parts of the code have been delivered in an earlier course by me. 
"""
# a)
def readfile(filename):
    with open(filename, "r") as x:  # Open the file, and read "r"
        v0 = float(x.readline().split(" ")[1])  # Split whatever in the line, and add the second element as a float
        x.readline()  # Read next line
        t = [line.split() for line in x] # Split every remaining line and add elements to the list
        # Turn the values into float
        t = [float(t[i][j]) for i in range(len(t)) for j in range(len(t[i]))]

    return v0,t  # Return v0 and t

# b)
from numpy import random as r  # Import random

def test_func():  # Define test function
    v0_actual = 3.00
    t_values_actual = [str(r.random()*r.randint(1,5)) for i in range(5)]
    test_file = open('temp.dat', 'w')  # Generates the input file
    test_file.write('v0: %.2f\n' %(v0_actual))  # Write the line, go to the next line
    test_file.write('t:\n')  # write t:, and go to the next line
# Joins the elemtents in a list, but with a selected separator in the method.
    test_file.write('  '.join(t_values_actual))
    test_file.close()  # Stop writing 

    v0_test = readfile("temp.dat")[0] # Calls the function in task a)
    t_values_test = readfile("temp.dat")[1]  # read the test file
    tol = 1e-9
    msg = "Error"
    assert abs(v0_actual - v0_test) < tol, msg  # Asserts conditon
    for i in range(len(t_values_actual)):
        assert float(t_values_actual[i]) - t_values_test[i] < tol, msg

test_func()

# c)

def real_func(filename):
    g = 9.81  # [m/s^2]
    v0 = readfile(filename)[0]  
    t_values = sorted((readfile(filename)[1]))  # sorts the elements in the list
    y = [v0*t_values[i] - 0.5*g*t_values[i]**2 for i in range(len(t_values))]  # List of heights
    with open("time_n_height.dat", "w") as ty:  # Writing a new file
        ty.write("  t-values                 corresponding y-values\n")  # Header
        ty.write("___________________________________________________\n")
        for i in range(0, len(t_values)):
            ty.write("%4.5f seconds               %4.2f meters\n"\
 %(t_values[i], y[i]))  # writes the times and corresponding heights

real_func("ball.dat")  # Call the function

"""
C:Users\moham\IN1900\Oblig5>python ball_file_read_write.py
"""