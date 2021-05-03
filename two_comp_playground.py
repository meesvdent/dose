from models import PietersModel, SourceOneCompFirstOrder
import numpy as np
import matplotlib.pyplot as plt

dose_mass = 10  # grams of alcohol
dv = 0.6 * 75
dose_conc = dose_mass/dv
time = 3600  # start drinking at t=3600s
ingestion_dur = 0  # x mins of drinking at steady pace

dose = []
for i in range(3):
    dose.append([dose_conc, i*3600, 0])

print(dose)

start = [0, 0, 0]  # start alcohol conc in all three comps

for a in [0.42]:
    ex = PietersModel(X0=start, doses=dose, k12=5.55 / 3600, k23=7.05 / 3600, vmax=0.47 / 3600, km=0.38, a=a)
    soc = SourceOneCompFirstOrder(X0=[0, 0], doses=dose, k_s1 = 0.0001, k_ex=0.001)

    t = np.linspace(0, 7*3600, 7*60+1)  # simulate for 5 hours at 1 second resolution

    X = ex.integrate(t)

    #X = soc.integrate(t)
    print(f"shape array {X.shape[1]}")

    dif = []
    for i in range(len(t)):
        dif.append(((ex.vmax/(ex.km + X[:, 2][i])) * X[:, 2][i])*10000)

    comp1 = X[:, 0]  # extract comp 1 (stomach)
    comp2 = X[:, 1]  # extract comp 2 (small intestine)
    comp3 = X[:, 2]  # extract comp 3 (plasma)

    plt.plot(t, comp1)
    plt.plot(t, comp2)
    plt.plot(t, comp3)
    #plt.plot(t, dif)

    plt.show()

cmax = max(comp3) 
print(f'cmax: {cmax}')

