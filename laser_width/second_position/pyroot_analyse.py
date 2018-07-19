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
import sys

############### Readout command line argument

try:
    name_of_folder = sys.argv[1]

    try:
        plot_style = sys.argv[2]
    except IndexError:
        plot_style = None

except IndexError:
    print('No Argument given Or other Index out of Range Er')


print(name_of_folder)

sys.path.insert(0, './' + name_of_folder + '/')

 ########################## import pyData.py  ######################################

from pyData import *

##################################################### Insert Data above line #############################


root.gStyle.SetOptTitle(0)
root.gStyle.SetOptFit(1)

########################### Def Gaus function ######################

personal_gaus =  root.TF1("personal_gaus",  " [0] * exp(  -0.5 * ( (x - [1])  / [2] )  * ( (x - [1])  /  [2] ) ) ")
name_params = [ "amplitude/[MeanVcal]", "mean/[Col]", "sigma/[Col]"]

personal_gaus.SetParName(0,'Amplitude')
personal_gaus.SetParName(1,'Mean')
personal_gaus.SetParName(2,'Sigma')


############################### Save Data in list #######################################

mean_value_col_list = []
mean_error_col_list = []
x_value = []
x_error = []

##############################################################################################################################

################################### Getting the mean hit value of all columns near the laserspot #############################

###############################################################################################################################


################################## Set sum area, size of sensetive area ###############################

xmin = 18
xmax = 26

ymin = 61
ymax = 72

####################################  calculating mean of each coloum ################################

for i in range(xmin,xmax): # going thru all col
    content = []
    error = []
    x_value.append(i)
    x_error.append(0.5)


    for j in range(ymin,ymax): # going thru all rows
        if qMap_Ag_C0_V0.GetBinContent(i,j) >2500 :
            pass

        if qMap_Ag_C0_V0.GetBinContent(i,j) != 0:
            content.append( qMap_Ag_C0_V0.GetBinContent(i,j))
            error.append( qMap_Ag_C0_V0.GetBinError(i,j) ) # Is this the real error


        else:
            pass

    content_bin = unp.uarray( content, error)
    mean_content_col = content_bin.sum() # mean value of each bin in the col
    # Saving values in lists
    mean_value_col_list.append( noms(mean_content_col))
    mean_error_col_list.append( stds(mean_content_col) )


########################### Create errorbar plot #####################################

errorbar_plot_col = root.TGraphErrors( len(x_value), array( 'f', x_value), array( 'f', mean_value_col_list), array( 'f', x_error), array( 'f', mean_error_col_list) )

############################## Set axis label and range of errobar plot ##################################

if plot_style == 'thesis':
    errorbar_plot_col.GetXaxis().SetTitle("Spalte")
    errorbar_plot_col.GetYaxis().SetTitle("Summe Hits / Vcal")
else:
    errorbar_plot_col.GetXaxis().SetTitle("Col")
    errorbar_plot_col.GetYaxis().SetTitle("Mean Hit / Vcal")

errorbar_plot_col.SetMinimum(0)
errorbar_plot_col.SetMaximum( max( mean_value_col_list) + 0.3 * max(mean_value_col_list) )



####################### create Canvas and FIT ##########################################

c1 = root.TCanvas("c1", "c1", 1980, 1080)

personal_gaus.SetParLimits(0, max(mean_value_col_list) * .5, max(mean_value_col_list) * 5 )
personal_gaus.SetParLimits(1, np.mean(x_value) * .5, np.mean(x_value) * 1.5 )
personal_gaus.SetParLimits(2, np.std(np.array(x_value)) * 0.5, np.std(np.array(x_value)) * 1.5 )

errorbar_plot_col.Fit(personal_gaus, "", "", min(x_value) -0.5 , max( x_value) +0.5 )
#errorbar_plot_col.Fit("gaus", "", "", min(x_value) -0.5 , max( x_value) +0.5 )

errorbar_plot_col.Draw("ap*")

############################### Create legend ####################################

if plot_style == 'thesis':
    legend = root.TLegend(0.81,0.48,0.98,0.7)
    legend.SetTextSize(0.04)
    legend.AddEntry(errorbar_plot_col,"Summe Hits","lep")
    legend.AddEntry( personal_gaus,"Gaus Fit","l")
    legend.Draw()


else:
    legend = root.TLegend(0.65,0.47,0.98,0.7)
    legend.SetTextSize(0.04)
    legend.AddEntry(errorbar_plot_col,"Row sum hit value","lep")
    legend.AddEntry( personal_gaus,"Gaussian Fit","l")
    legend.Draw()

############################### Save parameter and plot ###########################################

with open( f'./fit_params/{name_of_folder}_fit_parameters_col_xaxis.txt', 'w') as file:
    for i in range(0,3):
        file.write( name_params[i] + ' ' + str( personal_gaus.GetParameter(i) ) + ' ' + str(personal_gaus.GetParError(i)) + '\n')

with open( f'./sigma_col_xaxis.txt', 'a') as file:
        file.write( name_params[i] + '_' + name_of_folder + ' ' + str( personal_gaus.GetParameter(2) ) + ' ' + str(personal_gaus.GetParError(2)) + '\n')


c1.SaveAs(f'./plots/{name_of_folder}_erorbar_plot_col.pdf')



##############################################################################################################################

################################### Getting the mean hit value of all rows near the laserspot #############################

###############################################################################################################################



############################Reset lists###########################################
mean_value_row_list = []
mean_error_row_list = []
x_value = []
x_error = []
row_with_hits = []


#################################### calculating mean of each row #####################################

for i in range(ymin,ymax): # going thru all rows
    content = []
    error = []

    x_value.append(i)
    x_error.append(0.5)

    for j in range(xmin,xmax): # going thru all col
        if qMap_Ag_C0_V0.GetBinContent(j,i) >2500 :
            pass

        elif qMap_Ag_C0_V0.GetBinContent(j,i) != 0:
            content.append( qMap_Ag_C0_V0.GetBinContent(j,i))
            error.append( qMap_Ag_C0_V0.GetBinError(j,i)) # Is this the real error

        else:
            pass
    content_bin = unp.uarray( content, error)
    mean_content_row = content_bin.sum() # mean value of each bin in the col
    # Saving values in lists
    mean_value_row_list.append( noms(mean_content_row))
    mean_error_row_list.append( stds(mean_content_row))

############################# Create new errorbar plot ####################################
errorbar_plot_rows = root.TGraphErrors( len(x_value), array( 'f', x_value), array( 'f', mean_value_row_list), array( 'f', x_error), array( 'f', mean_error_row_list) )

############################### create Canvas ########################################
c2 = root.TCanvas("c2", "c2", 1980, 1080);

############################## Set axis label of errobar plot ##################################

if plot_style == 'thesis':
    errorbar_plot_col.GetXaxis().SetTitle("Zeile")
    errorbar_plot_col.GetYaxis().SetTitle("Summe Hits / Vcal")
else:
    errorbar_plot_rows.GetXaxis().SetTitle("Row")
    errorbar_plot_rows.GetYaxis().SetTitle("Mean Hit / Vcal")

errorbar_plot_rows.SetMinimum(0)
errorbar_plot_rows.SetMaximum( max(mean_value_row_list) + 0.3 * max(mean_value_row_list) )


############################### Plot fucntion and fit #############################################


personal_gaus.SetParLimits(0, max(mean_value_row_list) * .5, max(mean_value_row_list) * 4 )
personal_gaus.SetParLimits(1, np.mean(x_value) * .5, np.mean(x_value) * 1.5 )
personal_gaus.SetParLimits(2, np.std(np.array(x_value)) * .5, np.std(np.array(x_value)) * 1.5 )

errorbar_plot_rows.Fit( personal_gaus, "", "", min(x_value) -0.5 , max( x_value) +0.5 )
errorbar_plot_rows.Draw("ap*")

##################################### create legend ################################################

if plot_style == 'thesis':
    legend = root.TLegend(0.81,0.48,0.98,0.7)
    legend.SetTextSize(0.04)
    legend.AddEntry(errorbar_plot_rows,"Summe Hits","lep")
    legend.AddEntry( personal_gaus,"Gaus Fit","l")
    legend.Draw()


else:
    legend = root.TLegend(0.65,0.47,0.98,0.7)
    legend.SetTextSize(0.04)
    legend.AddEntry(errorbar_plot_col,"Row sum hit value","lep")
    legend.AddEntry( personal_gaus,"Gaussian Fit","l")
    legend.Draw()

########################################### saveplot and fit params ########################################

with open( f'./fit_params/{name_of_folder}_fit_parameters_row_yaxis.txt', 'w') as file:
    for i in range(0,3):
        file.write( name_params[i] + ' ' + str( personal_gaus.GetParameter(i) ) + ' ' + str(personal_gaus.GetParError(i)) + '\n')

with open( f'./sigma_row_yaxis.txt', 'a') as file:
        file.write( name_params[i] +'_' + name_of_folder + ' ' + str( personal_gaus.GetParameter(2) ) + ' ' + str(personal_gaus.GetParError(2)) + '\n')


c2.SaveAs(f'./plots/{name_of_folder}_erorbar_plot_row.pdf')
