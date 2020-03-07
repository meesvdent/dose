from kinetics_functions import *


# set time parameters of interest
tmin = 0      # first time point of interest
tmax = 108000  # last time point of interest
tres = 1000    # time resolution of output

# set dose profile
dose_conc = [1,1,1] # in M
dose_time = [-0.001,36000,72000] # in s

I0 = 1  # initial concentration of unabsorbed compound
Etot = 1  # total concentration of protein
X0 = np.array([0,0,0])
R = np.array([0.0001,0.05,10,1,1E6,0.001])


t = np.linspace(tmin,tmax,tres)
plt.plot(t,I_of_t(t))
plt.xlabel("Time")
plt.ylabel("Unabsorbed drug concentration")
p.savefig('I_of_t.png', bbox_inches='tight')

X, infodict = integrate.odeint(dX_dt,X0,t,full_output=True);
print(infodict['message'])
print(X)

plt.figure(1)
plt.clf()
plt.plot(t,X.T[0],'r')
plt.xlabel("Time")
plt.ylabel("I_blood")
p.savefig('Iblood.png', bbox_inches='tight')

plt.clf()
plt.plot(t,X.T[1],'b')
plt.xlabel("Time")
plt.ylabel("I_tissue")
p.savefig('Itissue.png', bbox_inches='tight')

plt.clf()
plt.plot(t,X.T[2],'g')
plt.xlabel("Time")
plt.ylabel("Fraction of complex bound")
p.savefig('frac_bound.png', bbox_inches='tight')

plt.clf()
EI = Etot*X.T[2]  # get EI concentration as a function of time
E = Etot*(1.-X.T[2])  # get free E concentration as a function of time
plt.plot(t,EI,'g--')
plt.xlabel("Time")
plt.ylabel("Bound complex concentration")
p.savefig('bound.png', bbox_inches='tight')