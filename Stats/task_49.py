# Calculating the mean
import numpy as np
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = np.mean(speed)
print(x)

# Calculating the median
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
y = np.median(speed)
print(y)

# Calculating the mode
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
z= stats.mode(speed)
print(z)