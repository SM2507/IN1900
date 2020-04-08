"""
Exercise E.41: Simulate the spreading of a disease by a SIR model.
Authored by Mohammed Shartaz Mostafa.
Warning: Delivered in an earlier course by me.
"""

from numpy import linspace
from ODESolver import RungeKutta4
from matplotlib.pyplot import *


def f(U,t):  # This function returns the differential equations.
    S = U[0]; I = U[1]; R = U[2]  # U is a list with a length of 3. S, I, and R are one value each (The initial values).
    return [-beta*S*I, beta*S*I - v*I, v*I]


# "check" tests if S + I + R equals S0 + I0 + R0 within a selected tolerance:
def check(u,t,n):
    tol = 1E-8
    # u[n] is a list of new values for S, I, and R.
    return abs(sum(u[n]) - sum(U0)) > tol


def plot_func(f, U0, time_points):
    solve = RungeKutta4(f)  # RungeKutta4 receives a list of equations.
    solve.set_initial_condition(U0)  # Going to set the initial conditions of S, I, and R.
    # "time_points"decides over how many t-values (days) the equation is to be solved for:
    U, t = solve.solve(time_points, check)
    S, I, R = U[:,0], U[:,1], U[:,2]
    plot(t,S, label = 'Susceptibles'); plot(t,I, label = 'Infected'); plot(t,R, label = 'Recovered'); legend(loc='best')



U0 = [1500, 1, 0]; beta = 0.0005; v = 0.1
subplot(211); plot_func(f, U0, linspace(0,60,121))
# Here we change the beta value, the rate of infection of said disease, and see the difference in the plot.
beta = 0.0001
subplot(212); plot_func(f,U0,linspace(0,60,121))
show()

"""
As viewed in both charts, an increased beta value rapidly decreases the amount of susceptibles and quickly increases
the amount of infected. A reduced beta value decreased the growth of the infected,
as well as the likelihood of further infection. Considering the recovery is independent of beta,
the susceptibles/uninfected would have a much lower risk of infection as the number of infected would drop swiftly.
"""
