import numpy as np
from models import SourceOneCompFirstOrder
from helpers import calc_dose_conc, trans_thalf_ke
from visualisation import plot_conc

t = np.linspace(0, 24*3600, 24*3600+1)

dose = [0.1]  # grams, seconds
time = [3600]
molecularMass = 194.19  # Caffeine

patientMass = 75  # kg
DV = 0.625*patientMass  # L/kg, for caffeine
ke = trans_thalf_ke(4*3600)

dose_conc = calc_dose_conc(dose, molecularMass, DV)
time_conc = [list(a) for a in zip(time, dose_conc)]

model = OneCompModel(time_conc, ke, 0.0055)
amount_unabs = model.calc_unabs(t)
delta_abs = model.delta_abs(amount_unabs)

X, infodict = model.integrate(t)

plot_conc(t, X, 2)
