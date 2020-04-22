import numpy as np
from scipy.integrate import odeint

import matplotlib.pyplot as plt


class TwoCompModel:

    def __init__(self, X0, dose, k1, vmax, km):
        self.X0 = X0
        self.dose = dose
        self.k1 = k1
        self.vmax = vmax
        self.km = km
        self.count = 0

    def __str__(self):
        return f"model parameters: {self.X0}, {self.k1}, {self.k2}"

    def calc_unabs(self, t):
        self.count += 1
        tot = 0
        for mass, time, ingestion_dur in self.dose:
            if (t >= time) and (t <= time + ingestion_dur):
                tot += mass/ingestion_dur
            else:
                print("not")
        return tot

    def d_c1(self, X, t):
        d_c1 = self.calc_unabs(t) - X[0] * self.k1
        return d_c1

    def d_c2(self, X):
        d_c2 = X[0] * self.k1 - (self.vmax/(self.km + X[1])) * X[1]
        return d_c2

    def dX_dt(self, X, t):
        print("dx_dt: ", t)
        dX_dt = np.array([self.d_c1(X, t), self.d_c2(X)])
        return dX_dt

    def integrate(self, t_span):
        print(t_span)
        X = odeint(self.dX_dt, self.X0, t_span)
        print("count: ", self.count)
        return X

