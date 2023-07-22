# Python program to display variance of data groups

# Import library
import numpy as np
import scipy.stats as stats

# Creating data groups
data_group1 = np.array([14, 15, 15, 16, 13, 8, 14,
						17, 16, 14, 19, 20, 21, 15,
						15, 16, 16, 13, 14, 12])
data_group2 = np.array([15, 17, 14, 17, 14, 8, 12,
						19, 19, 14, 17, 22, 24, 16,
						13, 16, 13, 18, 15, 13])

# Print the variance of both data groups
print(np.var(data_group1), np.var(data_group2))