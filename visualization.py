import matplotlib.pyplot as plt
import numpy as np

def plot_conc(t, X, stepsize=1):
    plt.plot(t, X)
    plt.xticks(np.arange(0, max(t), stepsize*3600), [str(n).zfill(2) + ':00' for n in np.arange(0, max(t)/3600, stepsize)], rotation=45)
    plt.show()
