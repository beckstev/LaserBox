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
from array import array
import time
import ROOT as root


u_bias_first, I_first  = np.genfromtxt('iv_curve_first_run.txt', unpack = True)
u_bias_second, I_second  = np.genfromtxt('iv_curve_second_run.txt', unpack = True)


plt.errorbar( u_bias_first[:-10], I_first[:-10], xerr=u_bias_first[:-10] * 0.02, yerr= I_first[:-10] * 0.035, fmt='x', label = 'Erste Messung')
plt.errorbar(u_bias_second,  I_second, xerr=u_bias_second * 0.02, yerr=  I_second * 0.035, fmt='x', label = 'Zweite Messung')

#plt.yscale('log')
plt.legend()
plt.grid()
plt.ylabel(r'$ I \, \, / \, \, \mu\mathrm{A}$')
plt.xlabel(r'$ U_{\mathrm{bias}} \, \, / \, \,  \mathrm{V}$')

plt.show()
#lt.savefig('iv_curve_forward_and_reversebias.pdf')
