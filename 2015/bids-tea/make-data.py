import numpy as np
import csv

N = 100
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)

with open("data.csv", "wb") as f:
    writer = csv.writer(f, delimiter='\t')

    for i in xrange(N):
        writer.writerow([x[i], y[i], colors[i]])
