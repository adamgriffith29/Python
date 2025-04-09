import numpy as np
from matplotlib import pyplot as plt

g = 9.8
a = 0.2
n = 101
t0 = 0
y0 = 0
tp = 20
h = (tp - t0) / (n - 1)
x = np.linspace(t0, tp, n)
y = np.zeros([n])
y[0] = y0
for i in range(1, n):
    y[i] = y[i - 1] + h * (g - (a * y[i - 1]))
for i in range(n):
    print(x[i], y[i])

analytical_solution = (g / a) * (1 - (np.exp((-a) * x)))
print('real solution is: ', analytical_solution)

plt.plot(x, y, 'ro', label="Euler's Method")
plt.xlabel("time")
plt.ylabel("Velocity")
plt.title("Euler’s Method Result and Analytical result")
plt.plot(analytical_solution, 'k-', label="Analytical result")
plt.legend()
plt.show()
