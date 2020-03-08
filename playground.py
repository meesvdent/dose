import numpy as np
from models import OneCompModel
from helpers import calc_dose_conc, trans_thalf_ke
import matplotlib.pyplot as plt

t = np.linspace(0, 30000, 30000)

dose = [0.160]  # grams, seconds
time = [0.001]
molecularMass = 194.19  # Caffeine

patientMass = 75  # kg
DV = 0.625*patientMass  # L/kg, for caffeine
ke = trans_thalf_ke(4*3600)
print(ke)

dose_conc = calc_dose_conc(dose, molecularMass, DV)
time_conc = [list(a) for a in zip(time, dose_conc)]

print(list(time_conc))

model = OneCompModel(time_conc, ke, 0.0055)
amount_unabs = model.calc_unabs(t)
delta_abs = model.delta_abs(amount_unabs)

X, infodict = model.integrate(t)

plt.plot(t, X)
plt.show()
