import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

class OneCompModel(object):
    def __init__(self, doses, kout, kabs):
        self.doses = doses
        self.kout = kout
        self.kabs = kabs

    def __str__(self):
        return f"model parameters: {self.doses}, {self.kout}, {self.kabs}"

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
        dIb_dt = self.kabs * self.calc_unabs(t) - X[0] * self.kout
        return dIb_dt

    def dX_dt(self, X, t):
        return np.array([self.dIblood_dt(X, t)])

    def intergrate(self, t):
        X0 = [0]
        X, infodict = integrate.odeint(self.dX_dt, X0, t, full_output=True)
        return X, infodict



t = np.linspace(0, 1, 1000)

model = OneCompModel([[0.001, 5], [0.4, 5]], 0, 0.5)
amount_unabs = model.calc_unabs(t)
delta_abs = model.delta_abs(amount_unabs)

X, infodict = model.intergrate(t)

plt.plot(t, X)
plt.show()
