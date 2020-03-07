import numpy as np

class OneCompModel(object):
    def __init__(self, doses, kout, kabs):
        self.doses = doses
        self.kout = kout
        self.kabs = kabs

    def delta_absorb(self, t):
        isum = 0
        for dt, conc in self.doses:
            isum += self.step(t - dt) * conc * np.exp(self.kabs * (t - dt))
        return isum

    def step(self, x):
        return 1 * (x > 0)


