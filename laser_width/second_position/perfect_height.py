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

###### Creating colors

ci = 1756
color_blue = root.TColor(ci, 0.082, 0.361, 1.)
ci = 1757
color_orange= root.TColor(ci, 100, 0.667, 0)
ci = 1758
color_purple = root.TColor(ci,0.298, 0.094, 1)
ci = 1759
color_yellow = root.TColor(ci,1, 0.824, 0)

######

def omega(omega_0, z):
    return omega_0 * np.sqrt( 1 + ( (1060e-9 * z)/(np.pi * omega_0) )**2 )



height = [ 5, 6, 7, 8, 9,9.5, 10,10.5,11, 12, 13, 14, 15]
#height = [ 5, 6, 7, 8, 9,9.5, 10,10.5, 12, 13, 14, 15]

#   name, ysigma, ysigma_error = np.genfromtxt( 'sigma_row_yaxis.txt', unpack =True)
#   name, xsigma, xsigma_error = np.genfromtxt('sigma_col_xaxis.txt', unpack = True)


name, ysigma, ysigma_error = np.genfromtxt( 'sigma_row_in_mumeter_yaxis.txt', unpack =True)
name, xsigma, xsigma_error = np.genfromtxt('sigma_col_in_mumeter_xaxis.txt', unpack = True)

xerror = np.ones(len(xsigma)) * 0.05
################## Plot and Fit with ROOT ############################

root.gStyle.SetLabelSize(.055, "XY");
root.gStyle.SetTitleSize(.055, "XY");
root.gStyle.SetTitleOffset(0.875, "XY");
root.gStyle.SetStatFontSize(.065)



#######################
polyx=  root.TF1("polyx",  " [0] * x * x + [1] * x + [2]")
polyy=  root.TF1("polyy",  " [0] * x * x + [1] * x + [2]")

c1 = root.TCanvas("c1", "c1", 1980, 1080)

mg = root.TMultiGraph();
plot_xsigma = root.TGraphErrors( len(xsigma), array( 'f', height), array( 'f',xsigma), array( 'f', xerror), array( 'f', xsigma_error) )
plot_ysigma = root.TGraphErrors( len(xsigma), array( 'f', height), array( 'f',ysigma), array( 'f', xerror), array( 'f', ysigma_error) )

plot_xsigma.SetMarkerColor(1756)
plot_xsigma.SetLineColor(1756)

plot_ysigma.SetMarkerColor(1757)
plot_ysigma.SetLineColor(1757)

polyx.SetLineColor(1759)
plot_xsigma.Fit('polyx')
polyy.SetLineColor(1758)
plot_ysigma.Fit('polyy')

#plot_xsigma.Draw('ap*')
#plot_ysigma.Draw('SAME ap*')
mg.Add(plot_xsigma)
mg.Add(plot_ysigma)

mg.GetXaxis().SetTitle("Relative Verschiebung #it{z} / mm")
mg.GetYaxis().SetTitle(" \sigma / \mum")

mg.Draw('ap*')

################# HARD CODED

chisquare_xsigma = str( int( polyx.GetChisquare()))
NDI_xsigma =  str(polyx.GetNDF())

chisquare_ysigma = str( int( polyy.GetChisquare()) )
NDI_ysigma =  str(polyy.GetNDF())

xlabel =  "Fit von \sigma_{x}(z), \chi^{2} / ndf = " + chisquare_xsigma + " / " +  NDI_xsigma
ylabel =  "Fit von \sigma_{y}(z), \chi^{2} / ndf = " + chisquare_ysigma + " / " +  NDI_ysigma
print(xlabel)

print(str(polyx.GetChisquare()))
legend = root.TLegend(0.13,0.66,0.50,0.87)
legend.SetTextSize(0.04)
legend.AddEntry(plot_xsigma," \sigma_{x}(z)", "lep")
legend.AddEntry(polyx,f"{xlabel}", "l")
legend.AddEntry(plot_ysigma,"\sigma_{y}(z)", "lep")
legend.AddEntry(polyy,f'{ylabel}',"l")
legend.Draw()

c1.SaveAs('perfect_height_root_version_sigma_mu_meter.pdf')

z = np.linspace(5,15,10000)

sigmax_fit_para_0 = ufloat( polyx.GetParameter(0), polyx.GetParError(0))
sigmax_fit_para_1 = ufloat( polyx.GetParameter(1), polyx.GetParError(1))
sigmax_fit_para_2 = ufloat( polyx.GetParameter(2), polyx.GetParError(2))

sigmax_fit =  sigmax_fit_para_0 * z**2 + sigmax_fit_para_1 * z + sigmax_fit_para_2

print('A sigma x Fit:', sigmax_fit_para_0, '\n')
print('B sigma x Fit:', sigmax_fit_para_1, '\n')
print('C sigma x Fit:', sigmax_fit_para_2, '\n')

print('Das Minimum von sigmax Fit ist: ', min(sigmax_fit), ' und liegt bei z gleich',   z[np.where( sigmax_fit == min(sigmax_fit))[0][0]], '\n\n\n')

sigmay_fit_para_0 = ufloat( polyy.GetParameter(0), polyy.GetParError(0))
sigmay_fit_para_1 = ufloat( polyy.GetParameter(1), polyy.GetParError(1))
sigmay_fit_para_2 = ufloat( polyy.GetParameter(2), polyy.GetParError(2))

sigmay_fit =  sigmay_fit_para_0 * z**2 + sigmay_fit_para_1 * z + sigmay_fit_para_2

print('A sigma y Fit:', sigmay_fit_para_0, '\n')
print('B sigma y Fit:', sigmay_fit_para_1, '\n')
print('C sigma y Fit:', sigmay_fit_para_2, '\n')

print('Das Minimum von sigmay Fit ist: ', min(sigmay_fit), ' und liegt bei z gleich',   z[np.where( sigmay_fit == min(sigmay_fit))[0][0]])


 ######################## Plot with matplotlib ######################
#plt.errorbar( height, xsigma, xerr = 0.05, yerr = xsigma_error , fmt ='x', label = r'$\sigma_{\mathrm{x}}$')
#plt.errorbar( height,ysigma, xerr = 0.05, yerr = ysigma_error , fmt ='x', label = r'$\sigma_{\mathrm{y}}$')
#plt.legend()
#plt.grid()
#plt.xlabel(r'$\mathrm{Relative \, Verschiebung \, des \, Lasers} \, \, / \, \, \mathrm{mm}$')
#plt.ylabel(r'$\sigma \, \, \mathrm{in \, Einheiten \, von \, Bins}$' )
##plt.show()
#
#plt.savefig('perfect_height.pdf')
