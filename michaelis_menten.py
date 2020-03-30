import numpy as np
from scipy import integrate

class MichaelisMentemModel():

    def __init__(self, X0, dose, v_max, km, kabs):
        self.X0 = X0
        self.dose = dose
        self.v_max = v_max
        self.km = km
        self.kabs = kabs

    def step(self, x):
        return 1 * (x > 0)

    def calc_delta_abs(self, conc, t, dt):
        delta_abs = conc * np.exp(-self.kabs * (t - dt))
        return delta_abs

    def calc_unabs(self, t):
        tot = 0
        for dt, conc in self.doses:
            tot += self.step(t - dt) * self.calc_delta_abs(conc, t, dt)
        return tot

    def delta_abs(self, amount_unabs):
        return amount_unabs * self.kabs

    def dIblood_dt(self, X, t):
        dIb_dt = self.kabs * self.calc_unabs(t) - X[0] * self.ke
        return dIb_dt

    def dX_dt(self, X, t):
        return np.array([self.dIblood_dt(X, t)])

    def integrate(self, t):
        X, infodict = integrate.odeint(self.dX_dt, self.X0, t, full_output=True)
        return X, infodict





