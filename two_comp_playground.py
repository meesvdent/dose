from pieters_model import PietersModel
import numpy as np
import matplotlib.pyplot as plt

dose_mass = 28.5  # grams of alcohol
dv = 0.5 * 75
dose_conc = dose_mass/dv
time = 3600  # start drinking at t=3600s
ingestion_dur = 20*60  # 10 mins of drinking at steady pace

dose = [[dose_conc, 0, 10*60]]  # dose mass, moment of ingestion, duration of ingestion

start = [0, 0, 0]  # start alcohol conc

for a in [0.42]:
    ex = PietersModel(X0=start, dose=dose, k12=5.55 / 3600, k23=7.05 / 3600, vmax=0.47 / 3600, km=0.38, a=a)

    t = np.linspace(0, 4*3600, 4*3600+1)  # simulate for 5 hours at 1 second resolution

    X, infodict = ex.integrate(t)

    comp1 = X[:, 0]  # extract comp 1 (stomach)
    comp2 = X[:, 1]  # extract comp 2 (small intestine)
    comp3 = X[:, 2]  # extract comp 3 (plasma)

    plt.plot(t, comp1)
    plt.plot(t, comp2)
    plt.plot(t, comp3)


plt.show()

