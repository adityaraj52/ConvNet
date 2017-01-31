import numpy as np

def softmax(x):
	"""Compute softmax values for x."""
	return(np.exp(x)/np.sum(np.exp(x), axis = 0))

scores = [3.0, 1.0,0.2]

print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt

x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

# plt.plot(x, softmax(scores).T, linewidth=2)
# plt.show()

# Show that the sum at each point is equal to one
# beside being aware of errors occuring by rounding of.
a = sum(softmax(scores))
print((a>0.999).all() & (a<=1.001).all())