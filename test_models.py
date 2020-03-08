from unittest import TestCase
import matplotlib.pyplot as plt


class TestOneCompModel(TestCase):
    def test_intergrate_zero_kout(self):
        from helpers import calc_dose_conc
        from models import OneCompModel
        import numpy as np
        t = np.linspace(0, 1, 1000)

        dose = [0.160, 0.160]  # grams, seconds
        time = [0.001, 0.4]
        molecular_mass = 194.19  # Caffeine

        patient_mass = 75  # kg
        DV = 0.625 * patient_mass  # L/kg, for caffeine

        dose_conc = calc_dose_conc(dose, molecular_mass, DV)
        time_conc = [list(a) for a in zip(time, dose_conc)]

        model = OneCompModel(time_conc, 0, 0.5)

        X, infodict = model.intergrate(t)

        self.assertAlmostEqual(np.max(X), 1.149E-5, 4)


    def test_integrate_kout(self):
        from helpers import calc_dose_conc
        from models import OneCompModel
        import numpy as np
        t = np.linspace(0, 1, 1000)

        dose = [0.100]  # grams, seconds
        time = [0.001, 0.4]
        molecular_mass = 194.19  # Caffeine

        patient_mass = 75  # kg
        DV = 0.625 * patient_mass  # L/kg, for caffeine

        dose_conc = calc_dose_conc(dose, molecular_mass, DV)
        time_conc = [list(a) for a in zip(time, dose_conc)]

        model = OneCompModel(time_conc, 0.0045, 0.0055)

        X, infodict = model.intergrate(t)

        plt.plot(t, X)
        print(max(X))

        self.assertAlmostEqual(np.max(X), 4.43209211e-06, 4)
