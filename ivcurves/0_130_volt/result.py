import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.unumpy import nominal_values as noms
from uncertainties.unumpy import std_devs as stds
from scipy.optimize import curve_fit
from scipy import odr
from array import array
import time
import ROOT as root

####################################################################################################

u_bias, I  = np.genfromtxt('iv_curve_0_130_V_second.txt', unpack = True)

plt.errorbar( u_bias, I, xerr=u_bias * 0.02, yerr= I* 0.035, fmt='.', label = 'Pixelstrom')
plt.legend(fontsize = 13)
plt.grid()
plt.ylabel(r'$ I \, \, / \, \, \mu\mathrm{A}$',fontsize = 13)
plt.xlabel(r'$ U_{\mathrm{ex}} \, \, / \, \,  \mathrm{V}$',fontsize = 13)

plt.tick_params(axis ='both', labelsize = 13 )
#plt.show()
plt.savefig('iv_curve_0_130_V.pdf')

###################################################################################

plt.clf()

########################################################################################

u_bias_first, I_first  = np.genfromtxt('iv_curve_first_run.txt', unpack = True)

plt.errorbar( u_bias_first, I_first, xerr=u_bias_first * 0.02, yerr= I_first* 0.035, fmt='.', label = 'Pixelstrom')
plt.legend(fontsize = 13)
plt.grid()
plt.ylabel(r'$ I \, \, / \, \, \mu\mathrm{A}$',fontsize = 13)
plt.xlabel(r'$ U_{\mathrm{ex}} \, \, / \, \,  \mathrm{V}$',fontsize = 13)
plt.tick_params(axis ='both', labelsize = 13 )
plt.savefig('iv_curve_0_90__V_one_volt_steps.pdf')

############################################################################################

plt.clf()

#############################################################################################

u_bias_second, I_second  = np.genfromtxt('iv_curve_second_run.txt', unpack = True)

plt.errorbar( u_bias_second, I_second, xerr=u_bias_second * 0.02, yerr= I_second* 0.035, fmt='.', label = 'Pixelstrom')
plt.legend(loc = 'upper left',fontsize = 13)
plt.grid()
plt.ylabel(r'$ I \, \, / \, \, \mu\mathrm{A}$',fontsize = 13)
plt.xlabel(r'$ U_{\mathrm{ex}} \, \, / \, \,  \mathrm{V}$',fontsize = 13)
plt.tick_params(axis ='both', labelsize = 13 )
plt.savefig('iv_curve_90_130__V_one_volt_steps.pdf')
