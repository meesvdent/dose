import numpy as np
from scipy.integrate import odeint


class PietersModel:

    def __init__(self, X0, dose, k12, k23, vmax, km, a):
        self.X0 = X0
        self.dose = dose
        self.k12 = k12
        self.k23 = k23
        self.vmax = vmax
        self.km = km
        self.count = 0
        self.a = a

    def __str__(self):
        return f"model parameters: {self.X0}, {self.k1}, {self.k2}"

    def step(self, x):
        return 1 * (x >= 0)

    def pulse(self, t):
        self.count += 1
        tot = 0
        for mass, time, ingestion_dur in self.dose:
            tot += self.step(t-time) * self.step((time+ingestion_dur)-t) * mass/ingestion_dur
        return tot

    def d_c1(self, X, t):
        d_c1 = self.pulse(t) - (self.k12 / (1 + self.a * X[0] * X[0])) * X[0]
        return d_c1

    def d_c2(self, X):
        d_c2 = (self.k12/(1 + self.a * X[0] * X[0])) * X[0] - X[1] * self.k23
        return d_c2

    def d_c3(self, X):
        d_c3 = X[1] * self.k23 - (self.vmax/(self.km + X[2])) * X[2]
        return d_c3

    def dX_dt(self, X, t):
        dX_dt = np.array([self.d_c1(X, t), self.d_c2(X), self.d_c3(X)])
        return dX_dt

    def integrate(self, t_span):
        X , infodict = odeint(self.dX_dt, self.X0, t_span, full_output=True)
        return X, infodict

