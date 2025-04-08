import numpy as np


def coinFlip(p):
    result = np.random.binomial(1, p)
    return result


n = eval(input('number of trials:'))

probability = 0.5

finalResults = np.arange(n)

for i in range(0, n):
    finalResults[i] = coinFlip(probability)
    i += 1

print("Tails = 0, Heads = 1: ", finalResults)

print("Heads: ", np.count_nonzero(finalResults == 1))
print("Tails: ", np.count_nonzero(finalResults == 0))

print('Heads Probability % =', np.count_nonzero(finalResults == 1) * 100 / (n))
print('Tails Probability % =', np.count_nonzero(finalResults == 0) * 100 / (n))
