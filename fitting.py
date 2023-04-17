import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def chi2(x,y,sigy,b,c):
    val = 0.0
    for i in range(0,len(x)):
        expected = b * x[i] + c
        observed = y[i]
        dy= sigy[i]
        val+=(float(observed)-float(expected))**2/float(dy**2)
        return val

def line_func(x, a, b):
    return a * x + b

### read data ###

filename="linefit.dat"
data = np.loadtxt(filename,skiprows=1,usecols=(0,1,2))
x = data[:,0]
y = data[:,1]
dy = data[:,2]
start = (20, 90)
params, params_covariance = optimize.curve_fit(line_func, x, y,sigma=dy,p0
= start,absolute_sigma=True)
eparams = np.array(params.size)
eparams = np.sqrt(np.diag(params_covariance))
plt.figure(figsize=(9, 6))
plt.scatter(x, y)
slope=params[0]
intercept=params[1]
slopeerr=eparams[0]
intercepterr=eparams[1]
plt.plot(x, line_func(x, slope, intercept), label=params, color="Blue")

#calculate chi squared and the number degrees of freedom.

ndof=x.size-params.size
chisqvalue = chi2(x,y,dy,params[0],params[1])
print (params[0],chisqvalue, ndof)
plt.xlabel("x",fontsize=14)
plt.ylabel("y",fontsize=14)
plt.errorbar(x,y,xerr=0, yerr=dy,marker='.', fmt='.', capsize=4,
linewidth=2, markersize=8, mew=0)

#Put the params on diff lines and say what they are

plt.text(20, 2.1, " slope = {0:0.6f} $\pm$ {1:0.6f}"
 .format(params[0], eparams[0]), color="Blue", fontweight='bold')
plt.text(20, 2.0, "intercept = {0:0.5f} $\pm$ {1:0.5f}"
 .format(intercept, intercepterr), color="Blue", fontweight='bold')


plt.text(20, 2.2, "$\chi^2$/NDOF = {0:0.0f} $/$ {1:0.0f}"
 .format(chisqvalue, ndof), color="Blue", fontweight='bold')
plt.show()
