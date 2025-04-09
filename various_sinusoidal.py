import numpy as np
import matplotlib.pyplot as plt


def fi(x, n):
    return np.sin(x) / (x ** n)


def f1(x):
    return fi(x, 1)


def f2(x):
    return fi(x, 2)


def f3(x):
    return fi(x, 3)


x = np.linspace(-5, 5, 100)

plt.subplot(3, 1, 1)
plt.plot(x, f1(x), 'k')
plt.ylabel('fi(x)')
plt.xlabel('x')
plt.title('f1 Sub-plot')
plt.xlim([-5, 5])

plt.subplot(3, 1, 2)
plt.plot(x, f2(x), 'b+')
plt.ylabel('fi(x)')
plt.xlabel('x')
plt.title('f2 Sub-plot')
plt.xlim([-5, 5])

plt.subplot(3, 1, 3)
plt.plot(x, f3(x), 'r')
plt.ylabel('fi(x)')
plt.xlabel('x')
plt.title('f3 Sub-plot')
plt.xlim([-5, 5])
plt.ylim([0, 450])

plt.tight_layout()
plt.savefig('sinx.png')
plt.show()
