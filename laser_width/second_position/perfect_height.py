import ROOT as root
import numpy as np
import time
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.unumpy import nominal_values as noms
from uncertainties.unumpy import std_devs as stds
from uncertainties import correlated_values
from array import array
import os
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

from lmfit import minimize, Parameters

##

def omega(omega_0, z):
    return omega_0 * np.sqrt( 1 + ( (1060e-9 * z)/(np.pi * omega_0) )**2 )

height = [ 5, 6, 7, 8, 9,9.5, 10,10.5,11, 12, 13, 14, 15]

name, ysigma, ysigma_error = np.genfromtxt( 'sigma_row_yaxis.txt', unpack =True)
name, xsigma, xsigma_error = np.genfromtxt('sigma_col_xaxis.txt', unpack = True)


print(len(ysigma), len(ysigma_error))
print(len(xsigma), len(xsigma_error))

plt.errorbar( height, xsigma, xerr = 0.05, yerr = xsigma_error , fmt ='x', label = r'$\sigma_{\mathrm{x}}$')
plt.errorbar( height,ysigma, xerr = 0.05, yerr = ysigma_error , fmt ='x', label = r'$\sigma_{\mathrm{y}}$')
plt.legend()
plt.xlabel(r'$\mathrm{relative \, movement \, of \, Laser} \, \, / \, \, \mathrm{mm}$')
plt.ylabel(r'$\sigma \, \, \mathrm{in \, units \, of \,bins}$' )
#plt.show()

plt.savefig('perfect_height.pdf')
