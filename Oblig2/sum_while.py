"""
Exercise 2.11: Compute a mathematical sum.
Author: Mohammed Shartaz Mostafa (python 3.6.5)
"""

"""
In python v3, I could the errors are the following: One being the print function 
lacking its parantheses, 
the second one being a constant k such that condition used in the while is always 
true, creating an infinte loop, 
and the final error is the loop not calculating for k = M, since the loop breaks at that point.
"""

s = 0; k = 1; M = 3  # Defining the variables
while k <= M:  # Using a while loop which breaks when k = M, including the M = 3
    s += 1/k  # Adding to the sum
    k += 1  # Increasing k by 1 for each repetition
print(s)  # Print the sum

"""
C:Users\moham\Google Drive\PHYSX\PYTHON FLS\IN1900\Oblig2>python sum_while.py
1.8333333333333333
"""