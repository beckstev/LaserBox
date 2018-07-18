import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.unumpy import nominal_values as noms
from uncertainties.unumpy import std_devs as stds


u_bias_first, I_first  = np.genfromtxt('iv_curve_first_run.txt', unpack = True)
u_bias_second, I_second  = np.genfromtxt('iv_curve_second_run.txt', unpack = True)

u_bias, I  = np.genfromtxt('iv_curve_0_130_V_second.txt', unpack = True)

params, cov = curve_fit(g, U_both[:10], I_both[:10])

plt.errorbar( u_bias_first, I_first, xerr=u_bias_first * 0.02, yerr= I_first * 0.035, fmt='x', label = 'Erste Messung')
plt.errorbar(u_bias_second,  I_second, xerr=u_bias_second * 0.02, yerr=  I_second * 0.035, fmt='x', label = 'Zweite Messung')

plt.legend()
plt.grid()
plt.ylabel(r'$ I \, \, / \, \, \mu\mathrm{A}$')
plt.xlabel(r'$ U_{\mathrm{ex}} \, \, / \, \,  \mathrm{V}$')

plt.show()
#plt.savefig('iv_curve_test.pdf')
