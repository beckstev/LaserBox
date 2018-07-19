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

height = [ 5.5e-3, 6e-3, 7e-3, 8e-3, 9e-3, 10e-3, 11e-3, 12e-3, 13e-3, 14e-3, 15e-3]

sigma_y = [1.6762046817955716 * 100e-6, 1.538489775708743 * 100e-6, 1.2667996551684635 * 100e-6, 0.9227732749310865 * 100e-6, 0.8606704620816109 * 100e-6,
0.6315702583843055* 100e-6,1.0875502579337843* 100e-6, 2.364140282852443* 100e-6, 2.319778855771209* 100e-6, 3.8146331190426035* 100e-6, 3.458809626725272* 100e-6  ]

sigma_y_error = [0.004200939478237076, 0.002775160952841804, 0.005456730565488788, 0.006134716355516601, 0.013508877486089588,
 0.0019198433852926633,0.005618933751150967, 0.053682807653258724, 0.017732913060791056, 0.007950141650115095, 0.004731836802477574  ]


z = np.linspace( 5, 16)
#params, cov = curve_fit(omega, height, sigma_y, p_0=[1e-4])
#error = np.sqrt(np.diag(cov))

params = Parameters()
params.add('omega', value = 1e-4)

out = minimize(omega, params, args=(height, sigma_y))
#plt.errorbar( height, sigma_y, xerr = 0.05, yerr = sigma_y_error, fmt ='x')

print('Parameter', params)
print('errors', error)
plt.plot(z, omega(params[0], z))

plt.show()
