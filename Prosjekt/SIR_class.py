"""
Exercise E.42: Introduce problem and solver classes in the SIR model.
Authored by Mohammed Shartaz Mostafa.
Warning: Delivered in an earlier course by me.
"""

from matplotlib.pyplot import plot, legend, subplot, show, axis
import ODESolver
from numpy import linspace

"""
Practically everything from from line 15 to line 48 is presented in the task, with the exception of beta.
I construed the current task as to use these classes as presented, and simulate the beta(t) scenario.
"""

class ProblemSIR(object):
    def __init__(self, nu, beta, S0, I0, R0, T):
        """
        nu, beta: parameters in the ODE system
        S0, I0, R0: initial values
        T: simulation for t in [0,T]
        """
        if isinstance(nu,  (float,int)):
            self.nu = lambda t: nu
        elif callable(nu):
            self.nu = nu
        if isinstance(beta, (float, int)):
            self.beta = lambda t: beta
        elif callable(beta):
            self.beta = beta
        self.S0, self.I0, self.R0, self.T = S0, I0, R0, T

    def __call__(self, u, t):
        """Right-hand side function of the ODE system."""
        S, I, R = u
        return [-self.beta(t)*S*I, self.beta(t)*S*I - self.nu(t)*I, self.nu(t)*I]

class SolverSIR(object):
    def __init__(self, problem, dt):
        self.problem, self.dt = problem, dt

    def solve(self, method = ODESolver.RungeKutta4):
        self.solver = method(self.problem)
        ic = [self.problem.S0, self.problem.I0, self.problem.R0]
        self.solver.set_initial_condition(ic)
        n = int(round(self.problem.T/float(self.dt)))
        t = linspace(0, self.problem.T, n + 1)
        u, self.t = self.solver.solve(t)
        self.S, self.I, self.R = u[:, 0], u[:, 1], u[:, 2]

    def plot(self):
        # Here we plot the time (in days) against the different values for S, I, and R as t (time) changes.
        plot(self.t, self.S, label = "Susceptibles"); plot(self.t, self.I, label = "Infected")
        plot(self.t, self.R, label = "Recovered"); legend(loc = "best")


def beta_(t):
    # The new requirement from teh task. Infectiousness reduced after 12 days.
    if 0 <= t <= 12:
        return 0.0005
    elif t > 12:
        return 0.0001

# As we progress past this task, the next ones will import SIR_class.
# The following code will only run if code is run directly, not if imported.


def main():
    # Here we are going to solve two differential equation, one with beta changing after 12 days,
    # and one with beta being constant at 0.0005.
    # We are using the ProblemSIR and SolverSIR classes to solve the equations:
    changing_beta = ProblemSIR(nu=0.1,beta=beta_,S0=1500,I0=1,R0=0,T=60)  # Filling in the variables.
    constant_beta = ProblemSIR(nu=0.1,beta=0.0005,S0=1500,I0=1,R0=0,T=60)  # Filling in the variables.
    changing_beta_solve = SolverSIR(problem=changing_beta,dt=0.1)
    constant_beta_solve = SolverSIR(problem=constant_beta,dt=0.1)

    # Plotting the solutions:
    changing_beta_solve.solve()
    subplot(211); changing_beta_solve.plot()

    constant_beta_solve.solve(); subplot(212); constant_beta_solve.plot()

    # Finding the extrema on both graph, I for infected.
    print ("Maximum infected, changing beta:", int(max(changing_beta_solve.I)))
    print ("Maximum infected, constant beta:", int(max(constant_beta_solve.I)))

    show()

if __name__ == "__main__":
    main()

# Run program:
"""
C:\Anaconda2\python.exe "C:/Users/Windows User/Desktop/PYTHON/SIR_class.py"
Maximum infected, changing beta: 745
Maximum infected, constant beta: 898
"""

"""
We can see from both charts that when the beta value changes after 12 days, the infected graph in the top chart
suddenly reaches its maximum. This means that the number of infected decreases after 12 days. In the bottom chart,
the infected graph reaches its maximum after about 14-15 days, and its maximum is greater than the infected graph's in
the top chart.
"""