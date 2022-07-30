import math
# n choose k
print('10 choose 5, avec un tirage de 10, combien contiennent 5 cas positifs?')
print(math.comb(10, 5))

from scipy.stats import binom
import matplotlib.pyplot as plt
# setting the values
# of n and p
n = 10 #10 dice rolls
p = 0.1666667 #1/6

#defining list of n values
r= list(range(n + 1))

#calling the binom.pmf function and printing its return value
return_val=binom.pmf(r, n, p)

plt.bar(r, return_val)
plt.savefig('pmf.png')