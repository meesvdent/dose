import helpers
from models import OneCompModel
import matplotlib.pyplot as plt

dose = [0.160, 0.160]  # grams, seconds
time = ['09:00:00', '09:30:00']
molecular_mass = 194.19  # Caffeine

patient_mass = 75  # kg
DV = 0.625 * patient_mass  # L/kg, for caffeine

dose_conc = helpers.calc_dose_conc(dose, molecular_mass, DV)
time_conc = [list(a) for a in zip(time, dose_conc)]

print(time_conc)
t, time_conc = helpers.generate_timeline(1, time_conc)
print(time_conc)
print(t)
ke = helpers.trans_thalf_ke(4*3600)
print(ke)

model = OneCompModel(time_conc, ke, 1)
X, _ = model.integrate(t)

print(X)

plt.plot(X, t)
plt.show()

