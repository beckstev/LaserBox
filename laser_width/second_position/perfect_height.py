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

height = [ 5e-3, 6e-3, 7e-3, 8e-3, 9e-3,9.5e-3, 10e-3,10.5e-3, 12e-3, 13e-3, 14e-3, 15e-3]

name, sigma_y, sigma_y_error = np.genfromtxt( 'sigma_row_yaxis.txt', unpack =True)
name, sigma_x, sigma_x_error = np.genfromtxt('sigma_col_xaxis.txt', unpack = True)



plt.errorbar( height, sigma_y, xerr = 5e-5, yerr = sigma_y_error , fmt ='x')
plt.errorbar( height,sigma_x, xerr = 5e-5, yerr = sigma_x_error , fmt ='x')

#plt.plot(z, omega(params[0], z))

plt.show()
