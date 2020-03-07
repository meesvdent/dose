# This script integrates a set of differential equations forward in time using scipy.integrate
#  that together describe the pharmacokinetic properties of a drug as follows:
#
#
#     kabs            k1           kon
#  I  --->   Iblood  ----> Itissue ---->  EI
#            |       <----         <----
#            | kout   k2           koff
#           \/
#
#
#   where kout is the sum of the rates of elimination and metabolism.
# All rates are in units of 1/s, except for kon, which is in 1/(M s).
# Concentrations are in mol/L, and time is in seconds.
#
# All species are described in the system vector X:
#   X = [Iblood, Itissue, f]
#
# All rates are described in the rate vector R:
#   R = [kabs, kout, k1, k2, kon, koff]
#
#   where [E] = (1-f)Etot and [EI] = f*Etot
#     and Etot is the total concentration of target protein
#
# Alex Dickson
# Michigan State University, 2016
#

import numpy as np


def I_of_t (t):
    isum = 0
    for dt, conc in zip(dose_time, dose_conc):
        isum += step(t-dt)*conc*np.exp(-R[0]*(t-dt))
    return isum

def step(x):
    return 1 * (x > 0)

def dIblood_dt (X,t):
    dIb_dt = R[0]*I_of_t(t) - X[0]*(R[1] + R[2]) + X[1]*R[3]
    return dIb_dt

def dItissue_dt (X,t):
    dIt_dt = R[2]*X[0] - X[1]*(R[3] + (1.-X[2])*Etot*R[4]) + X[2]*R[5]*Etot
    return dIt_dt

def df_dt (X,t):
    df_dt = X[1]*R[4] - X[2]*(X[1]*R[4] + R[5])
    return df_dt

def dX_dt(X,t):
    return np.array([dIblood_dt(X,t), dItissue_dt(X,t), df_dt(X,t)])
