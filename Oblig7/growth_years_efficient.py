"""
Exercise A.3: Reduce memory usage of difference equations
Author: Mohammed Shartaz Mostafa
Warning: This task has been delivered in an earlier course by me. 
"""

x0 = 100.  # Initial amount
N = 4  # Number of years
n = 0  # Counter

viz = open("visualized.txt", "w")  # Writing the file
viz.write("Interest accumulated after n years: \n")  # Header
viz.write("\n")
viz.write("Year            Assets\n")
viz.write("-----------------------\n")

while n <= N:  # Loop for calculating interest
    viz.write("%2i            %8.2f\n"%(n,x0))
    x1 = x0*(1.05)  # Interest rate
    x0 = x1
    n += 1

viz.close()  # Close the file

"""
(base) C:Users\dorth\Google Drive\PHYSX\PYT\IN1900\Oblig7>python growth_years_efficient.py

"""