import numpy as np
from scipy.integrate import odeint


class KineticsModel(object):
    
    def __init__(self, X0, doses):
        """

        :param X0: n dims array for n comps in model
        :param doses: array containing dose arrays [[dose (grams), time, duration], ]
        """
        self.X0 = X0
        self.doses = doses

    def __str__(self):
        return f"model parameters: {self.doses}, {self.ke}, {self.kabs}"

    def step(self, x):
        return 1 * (x >= 0)

    def pulse(self, t):
        tot = 0
        for mass, ing_time, ingestion_dur in self.doses:
            tot += self.step(t-ing_time) * self.step((ing_time+ingestion_dur)-t) * mass/ingestion_dur
        return tot

    def dX_dt(self, X, t):
        return np.array([])  # functions to be integrated

    def integrate(self, t):
        """The integration function. Integrates differential equations defined in subclass dX_dt function.

        :param t: np.linspace
        :param functions: n dim. np.array containing functions to integrate over, should be defined in inherited class
        :return: t x n dim. array containing integration output
        """
        X = odeint(self.dX_dt, self.X0, t, full_output=False)
        return X


class SourceOneCompFirstOrder(KineticsModel):
    def __init__(self, k_s1, k_ex, *args, **kwargs):
        super(SourceOneCompFirstOrder, self).__init__(*args, **kwargs)
        self.k_s1 = k_s1  # source to comp 1 rate
        self.k_ex = k_ex  # excretion rate

    def d_source(self, X, t):  # the source compartment, small intestine
        return self.pulse(t) - X[0] * self.k_s1

    def d_c1(self, X):  # plasma
        return X[0] * self.k_s1 - X[1] * self.k_ex

    def dX_dt(self, X, t):
        return np.array([self.d_source(X, t), self.d_c1(X)])


class PietersModel(KineticsModel):

    def __init__(self, k12, k23, vmax, km, a, *args, **kwargs):
        super(PietersModel, self).__init__(*args, **kwargs)
        self.k12 = k12
        self.k23 = k23
        self.vmax = vmax
        self.km = km
        self.a = a

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


