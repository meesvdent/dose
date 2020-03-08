import numpy as np
import matplotlib.pyplot as plt

class OneCompModel(object):
    def __init__(self, doses, kout, kabs):
        self.doses = doses
        self.kout = kout
        self.kabs = kabs

    def __str__(self):
        return f"model parameters: {self.doses}, {self.kout}, {self.kabs}"

    def calc_delta_abs(self, conc, t, dt):
        delta_abs = conc * np.exp(-self.kabs * (t - dt))
        return delta_abs

    def calc_unabs(self, t):
        tot = 0
        for dt, conc in self.doses:
            tot += self.step(t - dt) * self.calc_delta_abs(conc, t, dt)
        return tot

    def d_abs(self, amount_unabs):
        return amount_unabs * self.kabs

    def step(self, x):
        return 1 * (x > 0)



t = np.linspace(0, 1, 1000)

model = OneCompModel([[0.001, 5], [0.4, 5]], 0, 1)
amount_unabs = model.calc_unabs(t)
delta_abs = model.d_abs(amount_unabs)
print(amount_unabs)
print(delta_abs)
plt.plot(t, amount_unabs)
plt.plot(t, delta_abs)
plt.show()

