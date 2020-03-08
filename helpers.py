import numpy as np
import time


def generate_timeline(days, dosing):
    timeline = np.linspace(0, 3600 * 24 * days, 24 * 60 * days)
    sec_dosing = []
    for dose in dosing:
        in_sec = sum([a * b for a, b in zip([3600, 60, 1], map(int, dose[0].split(':')))])
        for day in range(days):
            sec_dosing.append([day*3600*24+in_sec, dose[1]])
    return timeline, sec_dosing


def mol_to_conc(mol_amount, dis_vol):
    '''Takes iterable of molair amounts and return iterable of
    conc coresponding to given distribution volume.

    :param mol_amount: float list
    :param dis_vol: float
    :return: dose_conc: float list
    '''
    dose_conc = []
    for mol in mol_amount:
        dose_conc.append(mol/dis_vol)
    return dose_conc


def mass_to_mol(mass_list, molecular_mass):
    dose_moll = []
    for mass in mass_list:
        dose_moll.append(mass / molecular_mass)
    return dose_moll


def calc_dose_conc(dose_masses, mol_mass, dis_vol):
    dose_mol = mass_to_mol(dose_masses, mol_mass)
    return mol_to_conc(dose_mol, dis_vol)


def trans_ke_thalf(ke):
    return 0.693/ke


def trans_thalf_ke(thalf):
    return 0.693/(thalf)

