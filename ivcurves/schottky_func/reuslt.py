import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import ufloat
import matplotlib.pyplot as plt
import scipy.constants as const
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

print(k_B, e)


def schottky_function(I_L, x):
	return I_L * ( np.exp( x)  -1 )

u_bias_vanilla, i_leak_vanilla_down   = np.genfromtxt('I_V_curve_-30_200.txt', unpack = True)
#u_bias_vanilla, i_leak_vanilla_down   = np.genfromtxt('iv_curve_0_130_V_second.txt', unpack = True)

u_bias = unp.uarray( [u_bias_vanilla, np.abs(u_bias_vanilla) * 0.02 ])

schotty_argument = (e * u_bias) / (  k_B* T)
plt.plot( noms(schotty_argument), i_leak_vanilla_down,'.')
plt.plot( noms(schotty_argument), schottky_function(-0.14, -0.5e-3*noms(schotty_argument)))
plt.xlim(0, 8000)
plt.ylim(0, 0.15)
#plt.show()




#errorbar_plot_schottky = root.TGraphErrors( len(u_bias), array( 'f', noms(schotty_argument)), array( 'f', i_leak_vanilla_down), array( 'f',  stds(schotty_argument) ), array( 'f', np.abs(i_leak_vanilla_down) * 0.035 ) )
errorbar_plot_schottky = root.TGraphErrors( len(u_bias), array( 'f', noms(u_bias)), array( 'f', i_leak_vanilla_down), array( 'f',  stds(u_bias) ), array( 'f', np.abs(i_leak_vanilla_down) * 0.035 ) )
schottky_fit_func = root.TF1('schottky_fun', ' [0] * ( - exp( -[1] * x) + 1) + [2] ', min( noms(schotty_argument) ), max( noms(schotty_argument) ))
c1 = root.TCanvas("c1","c1",1980,1080)
#c1.SetLogy()
schottky_fit_func.SetParLimits(0,.01, .5)
schottky_fit_func.SetParLimits(1,1e-6,1e-1)
schottky_fit_func.SetParLimits(2,-1,1)

errorbar_plot_schottky.GetXaxis().SetRangeUser(0,250);
#errorbar_plot_schottky.GetYaxis().SetRangeUser(0.001,0.2);
errorbar_plot_schottky.SetMinimum(0.00)
errorbar_plot_schottky.SetMaximum(0.15)

#errorbar_plot_schottky.GetXaxis().SetRangeUser(-1200,0);
#errorbar_plot_schottky.GetYaxis().SetRangeUser(0,0.2);
#qMap_Ag_C0_V0.GetYaxis().SetRange(61,72);

errorbar_plot_schottky.Fit(schottky_fit_func,"","", 10, 150)
errorbar_plot_schottky.Draw("ap*")
#time.sleep(120)
c1.SaveAs('test.pdf')
