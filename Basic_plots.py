import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles

#data points for scatter, line, bar
X_data = ["person 1","person 2","person 3","person 4","person 5","person 6","person 7","person 8","person 9", "person 10",]
Y_data = np.random.random(10) * 50

plt.scatter(X_data, Y_data, c="#00f", marker="*", s=150)
plt.plot(X_data, Y_data, c="red", lw = 2, linestyle="--")
plt.bar(X_data, Y_data, color="g", width=0.5, alpha=0.5, edgecolor="black", lw=4)
plt.show()


#data points for histogram
ages = np.random.normal(20, 1.5, 1000)
plt.hist(ages, bins=20, cumulative=True, color="r")
plt.show()
