import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import siunitx_ticks as si_ticks


############ Printint Measurepoints
plt.clf()
u_bias_vanilla, i_leak_vanilla_up,  i_leak_vanilla_down,  i_leak_vanilla_second_up,  i_leak_vanilla_second_down  = np.genfromtxt('iv_data_hysterese.txt', unpack = True)

u_bias = unp.uarray( [u_bias_vanilla, u_bias_vanilla * 0.0005 ])
i_leak_up = unp.uarray( [i_leak_vanilla_up, 0.001 ])
i_leak_down = unp.uarray( [i_leak_vanilla_down,  0.001])
i_leak_second_up = unp.uarray( [i_leak_vanilla_second_up,  0.001])
i_leak_second_down = unp.uarray( [i_leak_vanilla_second_down,  0.001])




#plt.plot(u_bias, i_leak, 'x')
plt.errorbar(u_bias_vanilla ,i_leak_vanilla_up, xerr=u_bias_vanilla * 0.02, yerr= i_leak_vanilla_up * 0.035, fmt='.', label = '1. Aufsteigend')
plt.errorbar(u_bias_vanilla ,i_leak_vanilla_down, xerr=u_bias_vanilla * 0.02, yerr= i_leak_vanilla_down * 0.035, fmt='.', label = '1. Absteigend')
plt.errorbar(u_bias_vanilla ,i_leak_vanilla_second_up, xerr=u_bias_vanilla * 0.02, yerr= i_leak_vanilla_second_up * 0.035, fmt='.', label = '2. Aufsteigend')
plt.errorbar(u_bias_vanilla ,i_leak_vanilla_second_down, xerr=u_bias_vanilla * 0.02, yerr= i_leak_vanilla_up * 0.035, fmt='.', label = '2. Absteigend')

plt.tick_params(axis ='both', labelsize = 16 )
si_ticks.siunitx_ticklabels(round_number=2)
#plt.plot(u_bias, np.sqrt(u_bias)*0.02, 'x')
plt.grid()
plt.ylabel(r'$ I \, \, / \, \, \mu\mathrm{A}$',fontsize = 16)
plt.xlabel(r'$ U_{\mathrm{ex}} \, \, / \, \,  \mathrm{V}$',fontsize = 16)

#plt.xlim(80, 100)

plt.legend(fontsize = 16)
#plt.show()
plt.savefig('iv_curve_hysterese.pdf',bbox_inches='tight')
