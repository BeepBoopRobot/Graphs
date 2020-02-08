#
# Example data, error-bar and linear fit demonstration program
#
# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Set default plot parameters.
# Note that this affects screen plots and lasts forever!
# Use carefully! We can save the plot with a given resolution anyway (see below).
# plt.rcParams['figure.dpi']=150 # minimum for printed work.
# plt.rcParams['figure.dpi']=72 # default setting.

# Define data from experiment as NumPy arrays
# A tip here would be to read this data from a file which is far more useful
# because you can keep all your data separate from program files.
y = np.array([2.85,2.50,2.13,1.79,1.65])
x = np.array([7.50,6.38,5.71,5.10,4.79])
yerror = np.array([0.01] * 5)

# Determine mean x, mean y, and N to use later in code
xbar = np.mean(x)
ybar = np.mean(y)
N = len(x)  # N is the number of data points

# Find gradient and intercept for line of best fit using least squares criterion
# equations used are those shown in lab manual page 40

numerator = np.sum((x - xbar) * y)
denominator = np.sum((x - xbar) ** 2)
m = numerator / denominator
c = ybar - m * xbar

# Find uncertainty in slope and intercept
# equations used are those shown in lab manual page 40
sigmam = np.sqrt(np.sum((y - m * x - c) ** 2) / ((N - 2) * np.sum((x - xbar) ** 2)))
sigmac = np.sqrt((np.sum((y - m * x - c) ** 2) / (N - 2)) * ((1 / N) + (xbar ** 2 / np.sum((x - xbar) ** 2))))

# Alternatively you could use NumPy polyfit to determine the gradient,
# intercept and errors.
# Use the following bit of code but we suggest you don't use it until you know what it does.
# Briefly, it can fit to a polynomial of any order. In this case the '1' means linear.
# The co-varience matrix gives the error in the
# fitted parameters where the diagonal elements of the matix are the variences (sigma squared)
# of each parameter in turn.The number of points is taken into account, do not further divide error by root(N).

# line,error = np.polyfit(x,y,1, cov=True)
# m = line[0]
# c = line[1]
# sigmam = np.sqrt(error[0][0])
# sigmac = np.sqrt(error[1][1])

# Print values for m, c and errors to screen to 6 decimal places
# Note that this level of significance may not be right for pasting directly into your report!
print("gradient is: {0:.6f} +/- {1:.6f}".format(m, sigmam, ))
print("intercept is: {0:.6f} +/- {1:.6f}".format(c, sigmac))

# Plot points and error bars. Plot points as a '.', colours set to black
plt.errorbar(x, y, yerr=yerror, fmt='.', color='k', capsize=2, ecolor='k')

# Plot line of best fit
plt.plot(x, m * x + c, color='k')

# Label axes
plt.title("Graph showing the frequency of an LED against its turn-on Voltage")
plt.xlabel('f / Hz x $10^{14}$')
plt.ylabel('p.d. / V')

# Save to file "graph.jpg" with a resolution of 300 dpi which is a suitable
# resolution for a your formal report. Note that this resolution setting over-rides
# your rcParams value (if you set it)
plt.savefig("g.jpg", dpi=300)

plt.show()
