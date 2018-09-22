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
import siunitx_ticks as si_ticks


####################################################################################################

u_bias, I  = np.genfromtxt('iv_curve_0_130_V_second.txt', unpack = True)

plt.errorbar( u_bias, I, xerr=u_bias * 0.02, yerr= I* 0.035, fmt='.', label = 'Pixelstrom')
plt.legend(fontsize = 16)
plt.grid()
plt.ylabel(r'$ I \, \, / \, \, \mu\mathrm{A}$',fontsize = 16)
plt.xlabel(r'$ U_{\mathrm{ex}} \, \, / \, \,  \mathrm{V}$',fontsize = 16)
si_ticks.siunitx_ticklabels(round_number=2)
plt.tick_params(axis ='both', labelsize = 16)
#plt.show()
plt.savefig('iv_curve_0_130_V.pdf',bbox_inches='tight')

###################################################################################

plt.clf()

########################################################################################

u_bias_first, I_first  = np.genfromtxt('iv_curve_first_run.txt', unpack = True)

plt.errorbar( u_bias_first, I_first, xerr=u_bias_first * 0.02, yerr= I_first* 0.035, fmt='.', label = 'Pixelstrom')
plt.legend(fontsize = 16)
plt.grid()
plt.ylabel(r'$ I \, \, / \, \, \mu\mathrm{A}$',fontsize = 16)
plt.xlabel(r'$ U_{\mathrm{ex}} \, \, / \, \,  \mathrm{V}$',fontsize = 16)
plt.tick_params(axis ='both', labelsize = 16 )
si_ticks.siunitx_ticklabels(round_number=2)
plt.savefig('iv_curve_0_90__V_one_volt_steps.pdf',bbox_inches='tight')

############################################################################################

plt.clf()

#############################################################################################

u_bias_second, I_second  = np.genfromtxt('iv_curve_second_run.txt', unpack = True)

plt.errorbar( u_bias_second, I_second, xerr=u_bias_second * 0.02, yerr= I_second* 0.035, fmt='.', label = 'Pixelstrom')
plt.legend(loc = 'upper left',fontsize = 16)
plt.grid()
plt.ylabel(r'$ I \, \, / \, \, \mu\mathrm{A}$',fontsize = 16)
plt.xlabel(r'$ U_{\mathrm{ex}} \, \, / \, \,  \mathrm{V}$',fontsize = 16)
plt.tick_params(axis ='both', labelsize = 16 )
si_ticks.siunitx_ticklabels(round_number=3)
plt.savefig('iv_curve_90_130__V_one_volt_steps.pdf',bbox_inches='tight')

############################################################################################

plt.clf()

#############################################################################################

u_bias_second, I_second  = np.genfromtxt('iv_curve_second_run.txt', unpack = True)

print(u_bias_first[-10:])
print(u_bias_second[:5])
plt.errorbar( u_bias_first, I_first, xerr=u_bias_first * 0.02, yerr= I_first* 0.035, fmt='.', color = 'C0')
plt.errorbar( u_bias_second, I_second, xerr=u_bias_second * 0.02, yerr= I_second* 0.035, fmt='.', color = 'C0',  label = 'Pixelstrom')
#plt.axvline(90, color = 'r', alpha = 0.5)
plt.legend(loc = 'upper left',fontsize = 16)
#plt.xlim(  u_bias_first[-10],u_bias_second[5])
plt.grid()
plt.ylabel(r'$ I \, \, / \, \, \mu\mathrm{A}$',fontsize = 16)
plt.xlabel(r'$ U_{\mathrm{ex}} \, \, / \, \,  \mathrm{V}$',fontsize = 16)
plt.tick_params(axis ='both', labelsize = 16 )
si_ticks.siunitx_ticklabels(round_number=3)
plt.savefig('iv_curve_0_130__V_one_volt_steps.pdf',bbox_inches='tight')
