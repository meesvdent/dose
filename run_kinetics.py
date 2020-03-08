import numpy as np
#import pylab as p
import matplotlib.pyplot as plt
from scipy import integrate

# set time parameters of interest
tmin = 0      # first time point of interest
tmax = 108000  # last time point of interest
tres = 1000    # time resolution of output

# set dose profile
dose_mass = [160E-3, 0,0] # in g
dose_time = [1000,36000,72000] # in s
molecularMass = 194.19 # Caffeine

I0 = 1  # initial concentration of unabsorbed compound
Etot = 5  # total concentration of protein
X0 = np.array([0,0,0])
R = np.array([0.0055,0.0035,10,1,1E6,0.001])

# functions
def dose_conc_func(dose_mass):
    doseMoll = []
    for mass in dose_mass:
        doseMoll.append(mass/molecularMass)
    dose_conc = []
    for mol in dose_conc:
        dose_conc.append(mol/DV)
    return(dose_conc)


def I_of_t (t):
    isum = 0
    for dt, conc in zip(dose_time, dose_conc):
        isum += step(t-dt)*conc*np.exp(-R[0]*(t-dt))
    return isum


def step(x):
    return 1 * (x > 0)


def dIblood_dt (X,t):
    dIb_dt = R[0]*I_of_t(t) - X[0]*(R[1])
    return dIb_dt


def dItissue_dt (X,t):
    dIt_dt = R[2]*X[0] - X[1]*(R[3] + (1.-X[2])*Etot*R[4]) + X[2]*R[5]*Etot
    return dIt_dt


def df_dt (X,t):
    df_dt = X[1]*R[4] - X[2]*(X[1]*R[4] + R[5])
    return df_dt


def dX_dt(X,t):
    return np.array([dIblood_dt(X,t), dItissue_dt(X,t), df_dt(X,t)])

dose_conc = dose_conc_func(dose_mass)

t = np.linspace(tmin,tmax,tres)
plt.plot(t,I_of_t(t))
plt.xlabel("Time")
plt.ylabel("Unabsorbed drug concentration")
# p.savefig('I_of_t.png', bbox_inches='tight')

X, infodict = integrate.odeint(dX_dt, X0, t, full_output=True);
print(infodict['message'])
print(X)

plt.figure(1)
plt.clf()
plt.plot(t,X.T[0],'r')
plt.xlabel("Time")
plt.ylabel("I_blood")
plt.show()
# p.savefig('Iblood.png', bbox_inches='tight')

plt.clf()
plt.plot(t,X.T[1],'b')
plt.xlabel("Time")
plt.ylabel("I_tissue")
plt.show()
# p.savefig('Itissue.png', bbox_inches='tight')

plt.clf()
plt.plot(t,X.T[2],'g')
plt.xlabel("Time")
plt.ylabel("Fraction of complex bound")
plt.show()
# p.savefig('frac_bound.png', bbox_inches='tight')

plt.clf()
EI = Etot*X.T[2]  # get EI concentration as a function of time
E = Etot*(1.-X.T[2])  # get free E concentration as a function of time
plt.plot(t,EI,'g--')
plt.xlabel("Time")
plt.ylabel("Bound complex concentration")
plt.show()
# p.savefig('bound.png', bbox_inches='tight')