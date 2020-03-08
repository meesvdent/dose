# import numpy as np
# from models import OneCompModel
# from helpers import calc_dose_conc
# import matplotlib.pyplot as plt
#
# t = np.linspace(0, 30000, 30000)
#
# dose = [0.160]  # grams, seconds
# time = [0.001]
# molecularMass = 194.19  # Caffeine
#
# patientMass = 75  # kg
# DV = 0.625*patientMass  # L/kg, for caffeine
#
# dose_conc = calc_dose_conc(dose, molecularMass, DV)
# time_conc = [list(a) for a in zip(time, dose_conc)]
#
# print(list(time_conc))
#
# model = OneCompModel(time_conc, 0.0015, 0.0055)
# amount_unabs = model.calc_unabs(t)
# delta_abs = model.delta_abs(amount_unabs)
#
# X, infodict = model.intergrate(t)
#
# plt.plot(t, X)
# plt.show()


def test_integrate_kout():
    from helpers import calc_dose_conc
    from models import OneCompModel
    import numpy as np
    import matplotlib.pyplot as plt

    t = np.linspace(0, 36000, 36000)

    dose = [0.100]  # grams, seconds
    time = [0.001]
    molecular_mass = 194.19  # Caffeine

    patient_mass = 75  # kg
    DV = 0.625 * patient_mass  # L/kg, for caffeine

    dose_conc = calc_dose_conc(dose, molecular_mass, DV)
    time_conc = [list(a) for a in zip(time, dose_conc)]

    model = OneCompModel(time_conc, 0.0045, 0.0055)

    X, infodict = model.intergrate(t)

    plt.plot(t, X)
    plt.show()

    print(max(X))

test_integrate_kout()