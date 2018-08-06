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



heigh_m = [ 5*1e-3, 6*1e-3, 7*1e-3, 8*1e-3, 9*1e-3,9.5*1e-3, 10*1e-3,10.5*1e-3,11*1e-3, 12*1e-3, 13*1e-3, 14*1e-3, 15*1e-3]

#heigh_m = [ 5*1e-3, 6*1e-3, 7*1e-3, 8*1e-3, 9*1e-3,9.5*1e-3, 10*1e-3,10.5*1e-3, 12*1e-3, 13*1e-3, 14*1e-3, 15*1e-3]
height = [ 5, 6, 7, 8, 9,9.5, 10,10.5,11, 12, 13, 14, 15]

#height = [ 5, 6, 7, 8, 9,9.5, 10,10.5, 12, 13, 14, 15]

#   name, ysigma, ysigma_error = np.genfromtxt( 'sigma_row_yaxis.txt', unpack =True)
#   name, xsigma, xsigma_error = np.genfromtxt('sigma_col_xaxis.txt', unpack = True)


name, xsigma, xsigma_error = np.genfromtxt('sigma_col_in_mumeter_xaxis.txt', unpack = True)
name, ysigma, ysigma_error = np.genfromtxt( 'sigma_row_in_mumeter_yaxis.txt', unpack =True)

xsigma  *= 1e-6
xsigma_error  *= 1e-6

ysigma  *= 1e-6
ysigma_error  *= 1e-6



usigma_x = unp.uarray( xsigma, xsigma_error)
usigma_y = unp.uarray( ysigma, ysigma_error)




xerror = 1e-3 * np.ones(len(xsigma)) * 0.05

a = 1
b = 1

usigma_x = usigma_x**2 * a
usigma_y = usigma_y**2 * a

uheight = unp.uarray( heigh_m, xerror) *b

################## Plot and Fit with ROOT ############################

root.gStyle.SetLabelSize(.055, "XY");
root.gStyle.SetLabelFont(42, "XY");
root.gStyle.SetTitleSize(.055, "XY");
root.gStyle.SetTitleOffset(0.9, "XY");
root.gStyle.SetStatFontSize(.065)
root.TGaxis.SetMaxDigits(2)




#######################

polyx=  root.TF1("polyx",  " [0] * x * x + [1] * x + [2]") # Fitfunctions for data
polyy=  root.TF1("polyy",  " [0] * x * x + [1] * x + [2]")

omega_x = root.TF1('omega_x',  "[0]  +  [2] * (x - [1] )**2 / ( [0] )")
#omega_x = root.TF1('omega_x',  "[0] * ( 1 +  [2]*  ( (x - [1] ) / [0] )**2 )**0.5  ")
omega_y = root.TF1('omega_y',  "[0]  +  [2] * (x - [1] )**2 / ( [0] ) ")

#omega_x.SetParLimits(0, 0, 260e-6*a )
#omega_x.SetParLimits(1,5e-3*b,15e-3*b)
#omega_x.SetParLimits(2, 1e-14,1e-12)

omega_x.SetParameter(0,4.5e-10  )
omega_x.SetParameter(1,0.00898)
omega_x.SetParameter(2,(1060e-9)**2/np.pi**2)

omega_y.SetParameter(0,4.5e-10  )
omega_y.SetParameter(1,0.00898)
omega_y.SetParameter(2,(1060e-9)**2/np.pi**2)

c1 = root.TCanvas("c1", "c1", 1980, 1080)
c1.SetGrid()

mg = root.TMultiGraph() #Create multigraph


#mg.GetXaxis.SetMaxDigits(2,'Y')



plot_xsigma = root.TGraphErrors( len(xsigma), array( 'f', noms(uheight)), array( 'f',noms(usigma_x)), array( 'f', stds(uheight)), array( 'f',stds(usigma_x)) )
plot_ysigma = root.TGraphErrors( len(xsigma), array( 'f', noms(uheight)), array( 'f',noms(usigma_y)), array( 'f', stds(uheight)), array( 'f',stds(usigma_y)) )


plot_xsigma.GetXaxis().SetLimits(0,1) #Set xLimits
plot_ysigma.GetXaxis().SetLimits(0,1) #Set xLimits



plot_xsigma.SetMarkerColor(1756)
plot_xsigma.SetLineColor(1756)

plot_ysigma.SetMarkerColor(1757)
plot_ysigma.SetLineColor(1757)

omega_x.SetLineColor(1759) #Set Linecolor xsigma
omega_y.SetLineColor(1758) # Set Linecolor ysigma

#plot_xsigma.Fit('polyx')
plot_xsigma.Fit('omega_x', 'E')
plot_ysigma.Fit('omega_y', 'E')


#for i in range(0,10):
#    plot_xsigma.GetX()[i]*=1e3
#    print(plot_xsigma.GetX()[i])


#plot_ysigma.Fit('polyy')

#plot_xsigma.Draw('ap*')
#plot_ysigma.Draw('SAME ap*')

mg.Add(plot_xsigma) # Add TGraphErrors to Multigraph
mg.Add(plot_ysigma)

mg.GetXaxis().SetTitle("Relative Verschiebung #it{z} / #{m}")
mg.GetYaxis().SetTitle(" \sigma^2 / #mathcal{m^2}")

#plot_xsigma.GetXaxis().
mg.SetMinimum(0)
#mg.SetMaximum(1.5e-7)

mg.GetXaxis().SetNdivisions(20)
mg.Draw('ap*')


A_x = ufloat( omega_x.GetParameter(0), omega_x.GetParError(0))
B_x =  ufloat( omega_x.GetParameter(1), omega_x.GetParError(1))
C_x =  ufloat( omega_x.GetParameter(2), omega_x.GetParError(2))

print('\n\n\n------------- sigma x -----------------------')
print('A_x: ', A_x , 'A**1/2',unp.sqrt(A_x) )
print('B_x: ', B_x)
print('C_x:', C_x )
print('Lambda_x in nm', unp.sqrt(C_x)*np.pi*1e9 )
print('-------------------------------------------------------- ')

A_y = ufloat( omega_y.GetParameter(0), omega_y.GetParError(0))
B_y =  ufloat( omega_y.GetParameter(1), omega_y.GetParError(1))
C_y =  ufloat( omega_y.GetParameter(2), omega_y.GetParError(2))

print('\n\n\n------------- sigma y -----------------------')
print('A_y: ', A_y , 'A**1/2',unp.sqrt(A_y) )
print('B_y: ', B_y)
print('C_y:', C_y )
print('Lambda_y in nm', unp.sqrt(C_y)*np.pi*1e9 )
print('-------------------------------------------------------- ')

################# HARD CODED - Add chisquare to legend ################################

chisquare_xsigma = str( int( omega_x.GetChisquare()))
NDI_xsigma =  str(omega_x.GetNDF())

chisquare_ysigma = str( int( omega_y.GetChisquare()) )
NDI_ysigma =  str(omega_y.GetNDF())

xlabel =  "Fit von \sigma_{x}(z), \chi^{2} / ndf = " + chisquare_xsigma + " / " +  NDI_xsigma
ylabel =  "Fit von \sigma_{y}(z), \chi^{2} / ndf = " + chisquare_ysigma + " / " +  NDI_ysigma


legend = root.TLegend(0.13,0.66,0.50,0.87)
legend.SetTextSize(0.04)
legend.AddEntry(plot_xsigma," \sigma_{x}(z)", "lep")
legend.AddEntry(omega_x,f"{xlabel}", "l")
legend.AddEntry(plot_ysigma,"\sigma_{y}(z)", "lep")
legend.AddEntry(omega_y,f'{ylabel}',"l")
legend.Draw()


c1.SaveAs('perfect_height_root_version_sigma_mu_meter_test.pdf')


kappa_x = ufloat( omega_x.GetParameter(2), omega_x.GetParError(2))
kappa_y = ufloat( omega_y.GetParameter(2), omega_y.GetParError(2))

print('kappa', kappa_x)
def lambdar ( fit_para):
    return unp.sqrt( fit_para) * np.pi

print('Lambdar x: ', lambdar(kappa_x))
print('Lambdar y: ', lambdar(kappa_y), '\n\n')
############################# Print fit parameters and find minimum of the fits ################################
#z = np.linspace(5,15,10000)
#
#sigmax_fit_para_0 = ufloat( polyx.GetParameter(0), polyx.GetParError(0))
#sigmax_fit_para_1 = ufloat( polyx.GetParameter(1), polyx.GetParError(1))
#sigmax_fit_para_2 = ufloat( polyx.GetParameter(2), polyx.GetParError(2))
#
#sigmax_fit =  sigmax_fit_para_0 * z**2 + sigmax_fit_para_1 * z + sigmax_fit_para_2
#
#print('A sigma x Fit:', sigmax_fit_para_0, '\n')
#print('B sigma x Fit:', sigmax_fit_para_1, '\n')
#print('C sigma x Fit:', sigmax_fit_para_2, '\n')
#
#print('Das Minimum von sigmax Fit ist: ', min(sigmax_fit), ' und liegt bei z gleich',   z[np.where( sigmax_fit == min(sigmax_fit))[0][0]], '\n\n\n')
#
#sigmay_fit_para_0 = ufloat( polyy.GetParameter(0), polyy.GetParError(0))
#sigmay_fit_para_1 = ufloat( polyy.GetParameter(1), polyy.GetParError(1))
#sigmay_fit_para_2 = ufloat( polyy.GetParameter(2), polyy.GetParError(2))
#
#sigmay_fit =  sigmay_fit_para_0 * z**2 + sigmay_fit_para_1 * z + sigmay_fit_para_2
#
#print('A sigma y Fit:', sigmay_fit_para_0, '\n')
#print('B sigma y Fit:', sigmay_fit_para_1, '\n')
#print('C sigma y Fit:', sigmay_fit_para_2, '\n')
#
#print('Das Minimum von sigmay Fit ist: ', min(sigmay_fit), ' und liegt bei z gleich',   z[np.where( sigmay_fit == min(sigmay_fit))[0][0]])
