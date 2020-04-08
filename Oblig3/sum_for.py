"""
Exercise 2.4. Errors in summation
Author: Mohammed Shartaz Mostafa (python 3.6.5)
"""

# The error was an undefined variable, k, which wasn't indexed after each loop.
# k was undefined, but could be used as an iterator, but then the range is incorrect.
# If k is an iterator, the range is incorrect, from 0 to 2. It needs to run values from 1 to 3.
# Also a lack of paratheses in the denominator.

s1 = 0; M = 3; k = 1
for i in range(M):
    s1 += 1/(2*k)**2
    k += 1

print(s1)

# Alternatively:
s = 0; M = 3
for k in range(1,M+1):
    s += 1/(2*k)**2

print(s)

# The while-loop equivalent
s2 = 0; M = 3; k = 1
while k <= M:
    s2 += 1/(2*k)**2
    k += 1
print(s2)    

assert s1==s2==s, "Error in loop"
"""
C:Users\moham\Google Drive\PHYSX\PYTHON FLS\IN1900\Oblig3>python sum_for.py
0.3402777777777778
0.3402777777777778
0.3402777777777778
"""
