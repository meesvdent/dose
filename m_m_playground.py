from michaelis_menten import MichaelisMentemModel
import helpers
import visualisation
import matplotlib.pyplot as plt

dose = [10]  # grams, seconds
time = ['09:00:00']
molecular_mass = 46.07  # Caffeine

patient_mass = 75  # kg
DV = 0.625 * patient_mass  # L/kg, for caffeine

dose_conc = helpers.calc_dose_conc(dose, molecular_mass, DV)
time_conc = [list(a) for a in zip(time, dose_conc)]

# Parameter prep

# adh alcohol Vm
# from g/l/min to mol/l/s
vm = 0.470 / molecular_mass / 3600

# Km
# from g/l to mol/l
km = 0.380 / molecular_mass



t, time_conc = helpers.generate_timeline(1, time_conc)

ke = helpers.trans_thalf_ke(4*3600)


model = MichaelisMentemModel(X0=0, dose=time_conc, v_max=0.1, km=0.1, kabs=0.1)
X, infodict = model.integrate(t)

print(X)

plt.plot(X, t)
plt.show()

visualisation.plot_conc(t, X, 2)