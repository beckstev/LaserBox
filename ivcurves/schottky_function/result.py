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

root.gStyle.SetOptTitle(0)
root.gStyle.SetOptFit(1)


boltzmann_constant = const.physical_constants["Boltzmann constant"]
electron_charge = const.physical_constants["elementary charge"]
k_B = ufloat( boltzmann_constant[0], boltzmann_constant[2])
e = ufloat( electron_charge[0], electron_charge[2])
T = ufloat( 293.15, 2)

def schottky_function(I_L, x):
	return I_L * ( np.exp( x)  -1 )

u_bias_vanilla, i_leak_vanilla_down   = np.genfromtxt('I_V_curve_-30_200.txt', unpack = True)

u_bias = unp.uarray( [u_bias_vanilla, np.abs(u_bias_vanilla) * 0.02 ])

schotty_argument = ( e* u_bias)/(T*k_B)


errorbar_plot_schottky = root.TGraphErrors( len(u_bias), array( 'f', noms(schotty_argument)), array( 'f', i_leak_vanilla_down), array( 'f',  stds(schotty_argument) ), array( 'f', np.abs(i_leak_vanilla_down) * 0.035 ) )


schottky_fun = root.TF1('schottky_fun', '[0] * ( -exp(-x) + 1)', min( noms(schotty_argument) ), max( noms(schotty_argument) ))
schottky_fun.SetParameter(0,0.12)
errorbar_plot_schottky.Fit(schottky_fun)
errorbar_plot_schottky.Draw()
time.sleep(5)

############ Printint Measurepoints
#
#
#
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
