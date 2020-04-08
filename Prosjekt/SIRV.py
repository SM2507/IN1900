"""
Exercise E.43: Introduce vaccination in a SIR model.
Authored by Mohammed Shartaz Mostafa
Warning: Delivered in an earlier course by me.
"""

from SIR_class import *  # Here we import everything from the file, SIR_class.


# In this task we are going to use the concept of inheritance, in a nutshell meaning the classes use other classes.
# The structure of the code is quite similar to the one in the previous task.
class ProblemSIRV(ProblemSIR):  # New class, ProblemSIRV, is going to inherit the "traits" from ProblemSIR.
    def __init__(self, nu, beta, S0, I0, R0, T, V0, p):  # Initializes the values required, exists in ProblemSIR.

        # We are going to initialize the values from ProblemSIR.
        # ProblemSIR has everything with the exception of V0 and p.
        ProblemSIR.__init__(self, nu, beta, S0, I0, R0, T); self.V0 = V0

        # The same "treatment" beta received in SIR_class.
        if isinstance(p, (float, int)):
            self.p = lambda t: p
        elif callable(p):
            self.p = p

    # Here we are gong to accommodate for the right side of the ODE system.
    # Since we have an additional value, V, we are going to override the method in ProblemSIR.
    def __call__(self, u, t):
        S, I, R, V = u
        # Returns the equations for S, I, R, and V, in said order.
        return [-self.beta(t)*S*I - self.p(t)*S, self.beta(t)*S*I - self.nu(t)*I, self.nu(t)*I, self.p(t)*S]


class SolverSIRV(SolverSIR):  # The solver class is also identical to its parent class, with a few exceptions.
    # We still use the RungeKutta method for solving the equations.
    def solve(self, method=ODESolver.RungeKutta4):
        self.solver = method(self.problem)
        ic = [self.problem.S0, self.problem.I0, self.problem.R0, self.problem.V0]  # The addition of V0 is new.
        self.solver.set_initial_condition(ic)
        n = int(round(self.problem.T / float(self.dt))); t = linspace(0, self.problem.T, n + 1)
        u, self.t = self.solver.solve(t)
        self.S, self.I, self.R, self.V = u[:, 0], u[:, 1], u[:, 2], u[:, 3]

    def plot(self):
        SolverSIR.plot(self)
        plot(self.t, self.V, label = "Vaccinated"); legend(loc = 'best')


def main():  # We are going to solve two differential equation
    problem = ProblemSIRV(nu=0.1, beta=beta_, S0=1500, I0=1, R0=0, T=60, p=0.1, V0=0)
    problem_solved = SolverSIRV(problem, 0.5); problem_solved.solve(); problem_solved.plot()

    # Finding the maximum in the solution, I for infected.
    print("The maximum of infected people with the vaccine introduced is ", int(max(problem_solved.I)))
    show()


if __name__ == '__main__':
    main()

# Run program:
"""
C:Anaconda2\python.exe "C:Users/Windows User/Desktop/PYTHON/SIRV.py"
The maximum of infected people with the vaccine introduced is  50
"""

"""
As we are able to see from graphs, the amount of susceptibles rapidly decreases as the number of
vaccinated people increases. The vaccinated become immune and will no longer be susceptible for infection, which
explains the low amount of infected people. The infected people will also become immune after a certain period of time,
and add to the number of recovered, which explains the stagnant recovered graph as the number of infected will
stagnate early itself.
"""