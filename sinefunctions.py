#Problem Two
import numpy as np
import matplotlib.pyplot as plt

def j0(x):
    return np.sin(x)/x
def j1(x):
    return (np.sin(x)/x**2)-(np.cos(x)/x)
def j2(x):
    return ((3/x**2)-1)*(np.sin(x)/x)-(3*np.cos(x)/x**2)

x = np.linspace(0,10,50)

plt.plot(x,j0(x),'ro',label = 'j0(x)')
plt.plot(x,j1(x),'k-',label = 'j1(x)')
plt.plot(x,j2(x),'b--',label = 'j2(x)')
plt.xlabel('x')
plt.ylabel('j_n(x)')
plt.legend()
plt.savefig('FinalPaper.png')
plt.show
