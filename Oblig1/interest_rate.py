"""
Exercise 1.6: Compute the growth of money in a bank
Author: Mohammed Shartaz Mostafa (written in python 3.6.5)
"""

# Defining our variables

A = 1000  # Initial amount of money in euros
p = 5  # Percent interest rate
n = 3  # Years of receiving interest


# Printing the result, and using string formatting for a neat way of writing our float into the string.
print("Money in account after three years: {:.2f} euros".format(A*(1+p/100)**n))

"""
Run program:
Money in account after three years: 1157.63 euros
"""
