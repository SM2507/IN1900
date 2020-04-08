"""
Exercise 5.28: Plot a wave packet
Author: Mohammed Shartaz Mostafa (python 3.6.5)
"""
from matplotlib.pylab import grid, plot, xlabel, ylabel, \
linspace, legend, show, sin, exp, pi, title
f = lambda x,t: exp(-(x-3*t)**2)*sin(3*pi*(x-t))

intrvl = linspace(-4,4,1000)

title("plot wavepacket")
grid("on")  # Ensuring the grid is visible
plot(intrvl,f(intrvl,0), label = "$f(x,t = 0)$")  # plotting and namng the figure
xlabel("x"); ylabel("$f(x,t)$"); legend(loc = 2)  # naming x- and y-axis, adding legend
show()  # Shows plot

"""
C:Users\moham\Google Drive\PHYSX\PYTHON FLS\IN1900\Oblig6>python plot_wavepacket.py
C:Users\moham\Anaconda3\lib\site-packages\matplotlib\cbook\deprecation.py:107: MatplotlibDeprecationWarning: Passing one of 'on', 'true', 'off', 'false' as a boolean is deprecated; use an actual boolean (True/False) instead.
  warnings.warn(message, mplDeprecation, stacklevel=1)
"""
