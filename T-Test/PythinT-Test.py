# Python program to conduct two-sample
# T-test using pingouin library

# Importing library
from statsmodels.stats.weightstats import ttest_ind
import numpy as np
import pingouin as pg

# Creating data groups
data_group1 = np.array([160, 150, 160, 156.12, 163.24,
						160.56, 168.56, 174.12,
						167.123, 165.12])
data_group2 = np.array([157.97, 146, 140.2, 170.15,
						167.34, 176.123, 162.35, 159.123,
						169.43, 148.123])

# Conducting two-sample ttest
result = pg.ttest(data_group1,
				data_group2,
				correction=True)

# Print the result
print(result)