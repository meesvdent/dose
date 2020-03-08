
def calc_dose_conc(dose_mass, molecularMass, DV):
    doseMoll = []
    for mass in dose_mass:
        doseMoll.append(mass/molecularMass)
    dose_conc = []
    for mol in doseMoll:
        dose_conc.append(mol/DV)
    return dose_conc