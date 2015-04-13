### "imports"
import matplotlib
import numpy as np
import csv
import json

### "pyplot"
matplotlib.use("Agg")
import matplotlib.pyplot as plt

### "import-data"
x = []
y = []
colors = []
with open("data.csv", "rb") as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        _x, _y, _c = [float(i) for i in row]
        x.append(_x)
        y.append(_y)
        colors.append(_c)
N = len(x)
area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses

### "graph-data"
plt.scatter(x, y, s=area, c=colors, alpha=0.5)

### "save"
with open("pyplot-scatter-example.png", "wb") as f:
    plt.savefig(f)
with open("results.json", "wb") as f:
    json.dump({'n' : N}, f)
