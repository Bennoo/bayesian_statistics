import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
import seaborn as sns

# this will make plots a little bit prettier
sns.set(style='darkgrid')
sns.set_context('talk')

# exercice 1
# A friend finds a coin on the ground, flips it, and gets six heads in a row and then one tails.
# Give the beta distribution that describes this.
# Use integration to determine the probability that the true rate of flipping heads is between 0.4 and 0.6,
# reflecting that the coin is reasonably fair.
a = 6 # six heads
b = 1 # one tail
p = [0.4, 0.6] #proba before 0.4 and proba before 0.6 (to get between, make the difference)

results = beta.sf(x=p, a=a, b=b)
results_diff = beta.sf(x=p, a=a, b=b)[0] - beta.sf(x=p, a=a, b=b)[1]

# Plot the Beta distribution
x = np.linspace(0, 1, 1000)
plt.plot(x, beta.pdf(x, a, b))

print(f'probability for the coin to be fair regarding experiment:{results_diff}')

# exercice 2
# Come up with a prior probability that the coin is fair.
# Use a beta distribution such that there is at least a 95 percent chance that
# the true rate of flipping heads is between 0.4 and 0.6.

# defining a strong prior
a2 = 55   
b2 = 55

# Plot the prior Beta distribution
x = np.linspace(0, 1, 1000)
plt.plot(x, beta.pdf(x, a2, b2))

# beta posterior = beta prior+likekihood
ac = a2 + a
bc = b2 + b

results2 = beta.sf(x=p, a=ac, b=bc)
results2_diff = beta.sf(x=p, a=ac, b=bc)[0] - beta.sf(x=p, a=ac, b=bc)[1]

# Plot the posterior Beta distribution
x = np.linspace(0, 1, 1000)
plt.plot(x, beta.pdf(x, ac, bc))
plt.savefig('chapter9Ex2pdf.png')

print(f'probability for the coin to be fair regarding experiment and a strong prior:{results2_diff}')

# Exercice 3
# Now see how many more heads (with no more tails) it would take to 
# convince you that there is reasonable chance that the coin is not fair.
# In this case, let's say that this means that our belief in the rate of the coing being between 0.4 and 0.6 drops below 0.5.

# We will now change likelihood
a = 6 + 23   # adding 23 heads
b = 1

# beta of posterior
ac = a + a2
bc = b + b2
posterior3_diff = beta.sf(x=p, a=ac, b=bc)[0] - beta.sf(x=p, a=ac, b=bc)[1]
print(f'probability for the coin to be fair regarding augemented experiment and the strong prior:{posterior3_diff}')