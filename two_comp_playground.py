from two_comp_model import TwoCompModel
import numpy as np
import matplotlib.pyplot as plt

mass = 10
time = 1
ingestion_dur = 0.1  # hours

dose = [[mass, time, ingestion_dur]] # dose mass, moment of ingestion, duration of ingestion


start = [0, 0]

ex = TwoCompModel(X0=start, dose=dose, k1=2, vmax=0.47, km=0.38)
t_span = np.linspace(0, 5, 101)
print(t_span)


X = ex.integrate(t_span)

comp1 = X[:, 0]
comp2 = X[:, 1]

plt.plot(t_span, comp1)
plt.plot(t_span, comp2)

plt.show()
