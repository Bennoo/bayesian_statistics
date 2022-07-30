import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# positive events
a = 14
# negative events
b = 27

# compute probabilities of the probability
value_less = beta.cdf(x=0.5, a=a, b=b)
value_more = beta.sf(x=0.5, a=a, b=b)

print(f'Probability that the return is less than 0.5 is {value_less}')
print(f'Probability that the return is more than 0.5 is {value_more}')

# Plot the Beta distribution
x = np.linspace(0, 1, 1000)
plt.plot(x, beta.pdf(x, a, b))
plt.savefig('pdf.png')