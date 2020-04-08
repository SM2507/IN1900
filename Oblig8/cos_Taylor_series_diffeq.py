"""
Exercise A.15: Find difference equations for computing cos x
Author: Mohammed Shartaz Mostafa
"""

from matplotlib.pylab import linspace, zeros, title, plot, show, xlabel, ylabel, legend, axis, cos, grid


def cos_Taylor(x,N):
    a0 = 1  # a0 is the first term in the Taylor approximation for cosine
    s1 = 1  # The first sum should be the fist term in the Taylor approximation
    j = 0  # Loop counter
    while j <= N:  # For solving the recurrence relation
        aj = -x**2/((2*j+1)*(2*j+2))*a0
        a0 = aj
        s = s1 + aj
        s1 = s
        j += 1
    return abs(a0), s1  # Returning the margin of error in the approximation and the approximation


def test_Taylor():  # The test function
    n = 2
    x = linspace(-5,5,11)
    s_by_hand = lambda x: 1-x**2/2+x**4/24-x**6/720
    tol = 1e-10
    msg = "Error in function"
    for i in range(len(x)):
        assert abs(cos_Taylor(x[i],n)[1] - s_by_hand(x[i])) < tol, msg

test_Taylor()

# Plotting task d
x = linspace(-15,15,1000)
grid(True)
title("Taylor approximation for cos(x) for various n")
plot(x,cos(x), label = "exact")
plot(x,cos_Taylor(x,2)[1], label = "n = 2")
plot(x,cos_Taylor(x,7)[1], label = "n = 7")
plot(x,cos_Taylor(x,12)[1], label = "n = 12")
xlabel("x"); ylabel("y")
axis([-15,15,-5,5])
legend(loc = "best")
show()

"""
(base) C:Users\dorth\Google Drive\PHYSX\PYT\IN1900\Oblig8>python cos_Taylor_series_diffeq.py

"""
