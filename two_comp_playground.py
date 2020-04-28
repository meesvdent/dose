from models import PietersModel
import numpy as np
import matplotlib.pyplot as plt

dose_mass = 10  # grams of alcohol
dv = 0.6 * 75
dose_conc = dose_mass/dv
time = 3600  # start drinking at t=3600s
ingestion_dur = 20*60  # x mins of drinking at steady pace

dose = []
for i in range(1):
    dose.append([dose_conc, i*3600, 10*60])

start = [0, 0, 0]  # start alcohol conc in all three comps

for a in [-10, 10]:
    ex = PietersModel(X0=start, dose=dose, k12=5.55 / 3600, k23=7.05 / 3600, vmax=0.47 / 3600, km=0.38, a=a)

    t = np.linspace(0, 5*3600, 5*60+1)  # simulate for 5 hours at 1 second resolution

    X, infodict = ex.integrate(t)

    dif = []
    for i in range(len(t)):
        dif.append(((ex.vmax/(ex.km + X[:, 2][i])) * X[:, 2][i])*10000)

    comp1 = X[:, 0]  # extract comp 1 (stomach)
    comp2 = X[:, 1]  # extract comp 2 (small intestine)
    comp3 = X[:, 2]  # extract comp 3 (plasma)

    plt.plot(t, comp1)
    plt.plot(t, comp2)
    plt.plot(t, comp3)
    plt.plot(t, dif)

    plt.show()

