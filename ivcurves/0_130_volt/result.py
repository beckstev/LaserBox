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

def sqrroota(a,b,x,c):
    return a*np.sqrt( (x -b) ) + c

def g(m,x,b):
    return m * x + b

u_bias_first, I_first  = np.genfromtxt('iv_curve_first_run.txt', unpack = True)
u_bias_second, I_second  = np.genfromtxt('iv_curve_second_run.txt', unpack = True)

U_both = sorted(np.concatenate( (u_bias_first[:10],u_bias_second[:10]), axis=0))
I_both = np.concatenate( ( I_first[:10],I_second[:10]), axis=0)

u_bias_first, I_first  = np.genfromtxt('iv_curve_0_130_V_second.txt', unpack = True)

params, cov = curve_fit(g, U_both[:10], I_both[:10])

a = params[0]
print(a)
plt.errorbar( u_bias_first, I_first, xerr=u_bias_first * 0.02, yerr= I_first * 0.035, fmt='x', label = 'Erste Messung')
plt.errorbar(u_bias_second,  I_second, xerr=u_bias_second * 0.02, yerr=  I_second * 0.035, fmt='x', label = 'Zweite Messung')
#plt.plot( U_both[:10],    np.array(a) * U_both[:10] + params[1] )
#plt.plot(U_both[:10], I_both[:10],'x')

#plt.yscale('log')
plt.legend()
plt.grid()
plt.ylabel(r'$ I \, \, / \, \, \mu\mathrm{A}$')
plt.xlabel(r'$ U_{\mathrm{bias}} \, \, / \, \,  \mathrm{V}$')

plt.show()
#plt.savefig('iv_curve_test.pdf')
###################

sqroot_fit = root.TF1('sqroot', ' [0] * ( x - [1] )^(0.5) + [2]', 0, 40)
sqroot_fit.SetParameter(0,0.1)
sqroot_fit.SetParameter(1,0)
sqroot_fit.SetParameter(2,0.03)

linear_fit =  root.TF1('linear_fit', ' [0] * x + [1] ',40,130 )
#errorbar_plot_sqrt = root.TGraphErrors( len(u_bias_first[50:]), array( 'f', u_bias_first[50:]), array( 'f', I_first[50:]), array( 'f',  u_bias_first[50:]* 0.02 ), array( 'f', I_first[50:] * 0.035 ) )
#errorbar_plot = root.TGraphErrors( len(U_both), array( 'f', U_both), array( 'f', I_both), array( 'f',  U_both * 0.02 ), array( 'f',I_both * 0.035 ) )
#errorbar_plot_sqrt.Fit(sqroot_fit)
errorbar_plot.Fit(sqroot_fit)
#errorbar_plot.Fit(linear_fit)
errorbar_plot.Draw("ap")


time.sleep(60)
