import numpy as np
from models import OneCompModel
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)

model = OneCompModel([[0.001, 5], [0.4, 5]], 0, 0.5)
amount_unabs = model.calc_unabs(t)
delta_abs = model.delta_abs(amount_unabs)

X, infodict = model.intergrate(t)

plt.plot(t, X)
plt.show()
