from models import PietersModel, SourceOneCompFirstOrder
import numpy as np
import matplotlib.pyplot as plt

dose_mass = 0.1  # grams of caffeine
dv = 0.6 * 75
dose_conc = dose_mass/dv
time = 3600  # start drinking at t=3600s
ingestion_dur = 0  # x mins of drinking at steady pace

dose = []
for i in range(1):
    dose.append([dose_conc, i*3600, 0])

print(dose)

start = [0, 0, 0]  # start alcohol conc in all three comps

ex = SourceOneCompFirstOrder(X0=[0, 0], doses=dose, k_s1=0.000755556, k_ex=(0.693/(4.7*3600)))

t = np.linspace(0, 7*3600, 7*60+1)  # simulate for 5 hours at 1 second resolution

X = ex.integrate(t)

#X = soc.integrate(t)
print(f"shape array {X.shape[1]}")

comp1 = X[:, 0]  # extract comp 1 (stomach)
comp2 = X[:, 1]  # extract comp 2 (plasma)

plt.plot(t, comp1)
plt.plot(t, comp2)

plt.show()

cmax = max(X[:, 1])

print(f'cmax: {cmax}')



