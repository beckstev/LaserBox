import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy.constants as const
from uncertainties import ufloat
from uncertainties.unumpy import nominal_values as noms
from uncertainties.unumpy import std_devs as stds
from scipy.optimize import curve_fit
from scipy import odr

import ROOT as root

boltzmann_constant = const.physical_constants["Boltzmann constant"]
electron_charge = const.physical_constants["elementary charge"]

def schottky_function(p, U):
	k_B =  boltzmann_constant[0]
	e = electron_charge[0]
	T =  293.15
	return I_L * ( np.exp( (e * U)/(k_B * T) -1 )

u_bias_vanilla, i_leak_vanilla_down   = np.genfromtxt('iv_data_hysterese.txt', unpack = True)

schottky_model = odr.Model(schottky_function)
data = odr.RealData(u_bias_vanilla, i_leak_vanilla_down , sx= u_bias_vanilla * 0.02 , sy= i_leak_vanilla_up * 0.035)

odr = odr.ODR(data, quad_model)

out = odr.run()


############ Printint Measurepoints
#
#
#u_bias = unp.uarray( [u_bias_vanilla, u_bias_vanilla * 0.0005 ])
#i_leak_up = unp.uarray( [i_leak_vanilla_up, 0.001 ])
#i_leak_down = unp.uarray( [i_leak_vanilla_down,  0.001])
#i_leak_second_up = unp.uarray( [i_leak_vanilla_second_up,  0.001])
#i_leak_second_down = unp.uarray( [i_leak_vanilla_second_down,  0.001])
#
#
##plt.plot(u_bias, i_leak, 'x')
#plt.errorbar(u_bias_vanilla ,i_leak_vanilla_up, xerr=u_bias_vanilla * 0.02, yerr= i_leak_vanilla_up * 0.035, fmt='x', label = 'First Up')
#plt.errorbar(u_bias_vanilla ,i_leak_vanilla_down, xerr=u_bias_vanilla * 0.02, yerr= i_leak_vanilla_down * 0.035, fmt='x', label = 'First Down')
#plt.errorbar(u_bias_vanilla ,i_leak_vanilla_second_up, xerr=u_bias_vanilla * 0.02, yerr= i_leak_vanilla_second_up * 0.035, fmt='x', label = 'Second Up')
#plt.errorbar(u_bias_vanilla ,i_leak_vanilla_second_down, xerr=u_bias_vanilla * 0.02, yerr= i_leak_vanilla_up * 0.035, fmt='x', label = 'Second Down')
#
##plt.plot(u_bias, np.sqrt(u_bias)*0.02, 'x')
#plt.grid()
#plt.ylabel(r'$ I_{\mathrm{leak}} \, \, / \, \, \mu\mathrm{A}$')
#plt.xlabel(r'$ U_{\mathrm{bias}} \, \, / \, \,  \mathrm{V}$')
#
##plt.xlim(80, 100)
#
#plt.legend()
##plt.show()
#plt.savefig('iv_curve.pdf')
