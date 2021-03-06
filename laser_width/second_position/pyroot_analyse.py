import ROOT as root
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.unumpy import nominal_values as noms
from uncertainties.unumpy import std_devs as stds
from array import array
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



sys.path.insert(0, './' + name_of_folder + '/')

 ########################## import pyData.py  ######################################

from pyData import *

##################################################### Set Cnavas Style #############################


root.gStyle.SetOptTitle(0)
root.gStyle.SetOptFit(1)
root.gStyle.SetLabelSize(.05, "XY");
root.gStyle.SetTitleSize(.05, "XY");
root.gStyle.SetTitleOffset(1, "XY");
root.gStyle.SetStatFontSize(.08)


########################### Def Gaus function ######################

personal_gaus =  root.TF1("personal_gaus",  " [0] * exp(  -0.5 * ( (x - [1])  / [2] )  * ( (x - [1])  /  [2] ) ) ")
name_params = [ "amplitude/[MeanVcal]", "mean/[Col]", "sigma/[Col]"]

personal_gaus.SetParName(0,'Amplitude')
personal_gaus.SetParName(2,'Sigma')

if plot_style == 'thesis':
    personal_gaus.SetParName(1,'Mittelwert')
else :
    personal_gaus.SetParName(1,'Mean')



############################### Save Data in list #######################################

mean_value_col_list = []
mean_error_col_list = []
x_value = []
x_error = []

##############################################################################################################################

################################### Getting the mean hit value of all columns near the laserspot #############################

###############################################################################################################################


################################## Set sum area, size of sensetive area ###############################

xmin = 20
xmax = 26

ymin = 62
ymax = 72



####################################  calculating mean of each coloum ################################

for i in range(xmin,xmax): # going thru all col
    content = []
    error = []
    x_value.append(i)
    x_error.append(0.5)
    test_error = []

    for j in range(ymin,ymax): # going thru all rows
        if qMap_Ag_C0_V0.GetBinContent(i,j) != 0:
            content.append( qMap_Ag_C0_V0.GetBinContent(i,j)) # Is this the real error
            N = qMap_Ag_C0_V0.GetBinEntries(  qMap_Ag_C0_V0.GetBin(i,j))
            if N == 1:
                new_error = np.sqrt(  ( qMap_Ag_C0_V0.GetBinContent(i,j) - qMap_Ag_C0_V0.GetBinContent(i,j)/N) **2)
            else:
                new_error = np.sqrt( 1/(N-1) * ( qMap_Ag_C0_V0.GetBinContent(i,j) - qMap_Ag_C0_V0.GetBinContent(i,j)/N) **2)

            #error.append( 1/N *  np.sqrt(qMap_Ag_C0_V0.GetBinContent(i,j) *N  ) ) # Is this the real error
            error.append( new_error ) # Is this the real error

        else:
            pass

    content_bin = unp.uarray( content, error)

    mean_content_col = content_bin.sum() # mean value of each bin in the col
    # Saving values in lists
    mean_value_col_list.append( noms(mean_content_col))
    mean_error_col_list.append( stds(mean_content_col) )


########################### Create errorbar plot #####################################

errorbar_plot_col = root.TGraphErrors( len(x_value), array( 'f', x_value- np.ones(len(x_value))), array( 'f', mean_value_col_list), array( 'f', x_error), array( 'f', mean_error_col_list) )
x_value -=  np.ones(len(x_value))
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

c1.SetGrid()


if name_of_folder == '7_mm':
    personal_gaus.SetParLimits(0, max(mean_value_col_list) * .2, max(mean_value_col_list) * 1.5 )
    personal_gaus.SetParLimits(1, np.mean(x_value) * .7, np.mean(x_value) * 1.2 )
    personal_gaus.SetParLimits(2, np.std(np.array(x_value)) * 0.03, np.std(np.array(x_value)) * 1.4 )

elif name_of_folder == '14_mm':
    personal_gaus.SetParLimits(0, max(mean_value_col_list) * .4, max(mean_value_col_list) * 1.5 )
    personal_gaus.SetParLimits(1, np.mean(x_value) * .8, np.mean(x_value) * 1.1 )
    personal_gaus.SetParLimits(2, np.std(np.array(x_value)) * 0.03, np.std(np.array(x_value))*1.1  )

else:
    personal_gaus.SetParLimits(0, max(mean_value_col_list) * .5, max(mean_value_col_list) * 1.8 )
    personal_gaus.SetParLimits(1, np.mean(x_value) * .7, np.mean(x_value) * 1.2 )
    personal_gaus.SetParLimits(2, np.std(np.array(x_value)) * 0.03, np.std(np.array(x_value)) * 1.2 )

errorbar_plot_col.Fit(personal_gaus, "", "", min(x_value) -0.5 , max( x_value) +0.5 )
#errorbar_plot_col.Fit("gaus", "", "", min(x_value) -0.5 , max( x_value) +0.5 )

errorbar_plot_col.Draw("ap*")

############################### Create legend ####################################

if plot_style == 'thesis':
    legend = root.TLegend(0.15,0.71,0.37,0.93)
    legend.SetTextSize(0.055)
    legend.AddEntry(errorbar_plot_col,"Summe Hits","lep")
    legend.AddEntry( personal_gaus,"Fit","l")
    legend.Draw()


else:
    legend = root.TLegend(0.65,0.47,0.98,0.7)
    legend.SetTextSize(0.04)
    legend.AddEntry(errorbar_plot_col,"Row sum hit value","lep")
    legend.AddEntry( personal_gaus,"Gaussian Fit","l")
    legend.Draw()


######## Transfer Sigma from Bin to mumeter ############################

sigma_mu_meter_col = ufloat(personal_gaus.GetParameter(2), personal_gaus.GetParError(2)) * 150 # 150 is pixel size in y direction


#############################################################################


############################### Save parameter and plot ###########################################

with open( f'./fit_params/{name_of_folder}_fit_parameters_col_xaxis.txt', 'w') as file:
    for i in range(0,3):
        file.write( name_params[i] + ' ' + str( personal_gaus.GetParameter(i) ) + ' ' + str(personal_gaus.GetParError(i)) + '\n')

with open( f'./fit_parameters_col_xaxis.txt', 'a') as file:
        file.write( name_of_folder + 'Amplitude/Sigma/Mean:' + ' ' + str( personal_gaus.GetParameter(0) ) + ' ' + str(personal_gaus.GetParError(0)) + ' ' + str( personal_gaus.GetParameter(1) ) + ' ' + str(personal_gaus.GetParError(1)) + ' ' + str( personal_gaus.GetParameter(2) ) + ' ' + str(personal_gaus.GetParError(2)) + '\n')

with open( f'./sigma_col_xaxis.txt', 'a') as file:
        file.write( name_params[i] + '_' + name_of_folder + ' ' + str( personal_gaus.GetParameter(2) ) + ' ' + str(personal_gaus.GetParError(2)) + '\n')


with open( f'./sigma_col_in_mumeter_xaxis.txt', 'a') as file:
        file.write( name_params[i] +'_' + name_of_folder + ' ' + str( noms(sigma_mu_meter_col) ) + ' ' + str( stds(sigma_mu_meter_col) ) + '\n')


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

        if qMap_Ag_C0_V0.GetBinContent(j,i) != 0:
            content.append( qMap_Ag_C0_V0.GetBinContent(j,i))
            N = qMap_Ag_C0_V0.GetBinEntries(  qMap_Ag_C0_V0.GetBin(j,i))
            if N == 1:
                new_error = np.sqrt(  ( qMap_Ag_C0_V0.GetBinContent(i,j) - qMap_Ag_C0_V0.GetBinContent(i,j)/N )**2)
            else:
                new_error = np.sqrt( 1/(N-1) * ( qMap_Ag_C0_V0.GetBinContent(i,j) - qMap_Ag_C0_V0.GetBinContent(i,j)/N) **2)

            #error.append( 1/N *  np.sqrt(qMap_Ag_C0_V0.GetBinContent(j,i) * N  ) )
            error.append( new_error)
        else:
            pass
    content_bin = unp.uarray( content, error)
    mean_content_row = content_bin.sum() # mean value of each bin in the col
    # Saving values in lists
    mean_value_row_list.append( noms(mean_content_row))
    mean_error_row_list.append( stds(mean_content_row))

############################# Create new errorbar plot ####################################
errorbar_plot_rows = root.TGraphErrors( len(x_value), array( 'f', x_value - np.ones(len(x_value))), array( 'f', mean_value_row_list), array( 'f', x_error), array( 'f', mean_error_row_list) )
x_value -=  np.ones(len(x_value))
errorbar_plot_rows.GetXaxis().SetNdivisions(20)
############################### create Canvas ########################################
c2 = root.TCanvas("c2", "c2", 1980, 1080);
c2.SetGrid()

############################## Set axis label of errobar plot ##################################

if plot_style == 'thesis':
    errorbar_plot_rows.GetXaxis().SetTitle("Zeile")
    errorbar_plot_rows.GetYaxis().SetTitle("Summe Hits / Vcal")
else:
    errorbar_plot_rows.GetXaxis().SetTitle("Row")
    errorbar_plot_rows.GetYaxis().SetTitle("Mean Hit / Vcal")

errorbar_plot_rows.SetMinimum(0)

if name_of_folder == '10-5_mm':
    errorbar_plot_rows.SetMaximum( max(mean_value_row_list) + 0.15 * max(mean_value_row_list) )
elif name_of_folder == '11_mm':
    errorbar_plot_rows.SetMaximum( max(mean_value_row_list) + 0.9 * max(mean_value_row_list) )
elif name_of_folder == '9_mm':
    errorbar_plot_rows.SetMaximum( max(mean_value_row_list) + 0.4 * max(mean_value_row_list) )

else:
    errorbar_plot_rows.SetMaximum( max(mean_value_row_list) + 0.3 * max(mean_value_row_list) )


############################### Plot fucntion and fit #############################################
if name_of_folder == '10-5_mm':
    print(np.std(np.array(x_value)))
    personal_gaus.SetParLimits(0, max(mean_value_row_list) * .5, max(mean_value_row_list) * 1.5 )
    personal_gaus.SetParLimits(1, np.mean(x_value) * .9, np.mean(x_value) * 1.12)
    personal_gaus.SetParLimits(2, np.std(np.array(x_value)) * .1, np.std(np.array(x_value))*0.6  )

elif name_of_folder == '11_mm':
    #personal_gaus.SetParameter(1, 66 )
    personal_gaus.SetParLimits(0, max(mean_value_row_list) * .5, max(mean_value_row_list) * 1.8)
    personal_gaus.SetParLimits(1, np.mean(x_value) * .9, np.mean(x_value) * 1.12 )
    personal_gaus.SetParLimits(2, np.std(np.array(x_value)) * .05, np.std(np.array(x_value))*0.8 )

elif name_of_folder == '7_mm':
    personal_gaus.SetParLimits(0, max(mean_value_row_list) * .2, max(mean_value_row_list)*1.2 )
    personal_gaus.SetParLimits(1, np.mean(x_value) * .7, np.mean(x_value) * 1.3)
    personal_gaus.SetParLimits(2, np.std(np.array(x_value)) * .1, np.std(np.array(x_value)) * 1.05 )

elif name_of_folder == '6_mm':
    personal_gaus.SetParLimits(0, max(mean_value_row_list) * .2, max(mean_value_row_list) * 1.31 )
    personal_gaus.SetParLimits(1, np.mean(x_value) -3, np.mean(x_value)+3 )
    personal_gaus.SetParLimits(2, np.std(np.array(x_value)) * .1, np.std(np.array(x_value)) *1.05  )

elif name_of_folder == '9-5_mm':
    personal_gaus.SetParLimits(0, max(mean_value_row_list) * .4, max(mean_value_row_list) * 1.3 )
    personal_gaus.SetParLimits(1, np.mean(x_value) -1/2, np.mean(x_value)+1 )
    personal_gaus.SetParLimits(2, np.std(np.array(x_value)) * .2, np.std(np.array(x_value))  )

elif name_of_folder == '9_mm':
    personal_gaus.SetParLimits(0, max(mean_value_row_list) * .4, max(mean_value_row_list) * 1.3 )
    personal_gaus.SetParLimits(1, np.mean(x_value) -1/2, np.mean(x_value)+1 )
    personal_gaus.SetParLimits(2, np.std(np.array(x_value)) * .1, np.std(np.array(x_value))  )

elif name_of_folder == '12_mm':
    personal_gaus.SetParLimits(0, max(mean_value_row_list) * .4, max(mean_value_row_list) * 1.3 )
    personal_gaus.SetParLimits(1, np.mean(x_value) -1/2, np.mean(x_value)+1 )
    personal_gaus.SetParLimits(2, np.std(np.array(x_value)) * .1, np.std(np.array(x_value))  )

elif name_of_folder == '13_mm':
    personal_gaus.SetParLimits(0, max(mean_value_row_list) * .4, max(mean_value_row_list) * 1.3 )
    personal_gaus.SetParLimits(1, np.mean(x_value) -1/2, np.mean(x_value)+1 )
    personal_gaus.SetParLimits(2, np.std(np.array(x_value)) * .1, np.std(np.array(x_value))  )

elif name_of_folder == '14_mm':
    personal_gaus.SetParLimits(0, max(mean_value_row_list) * .4, max(mean_value_row_list) * 1.3 )
    personal_gaus.SetParLimits(1, np.mean(x_value) -1/2, np.mean(x_value)+1 )
    personal_gaus.SetParLimits(2, np.std(np.array(x_value)) * .1, np.std(np.array(x_value))  )

elif name_of_folder == '5_mm':
    personal_gaus.SetParLimits(0, max(mean_value_row_list) * .4, max(mean_value_row_list) * 1.3 )
    personal_gaus.SetParLimits(1, np.mean(x_value) -1/2, np.mean(x_value)+1 )
    personal_gaus.SetParLimits(2, np.std(np.array(x_value)) * .1, np.std(np.array(x_value))  )
#
#
elif name_of_folder == '10_mm':
    personal_gaus.SetParameter(0, max(mean_value_row_list) )

    personal_gaus.SetParLimits(0, max(mean_value_row_list) * .4, max(mean_value_row_list) * 1.8)
    personal_gaus.SetParLimits(1, np.mean(x_value) * .7, np.mean(x_value) * 1.3 )
    personal_gaus.SetParLimits(2, np.std(np.array(x_value)) * .1, np.std(np.array(x_value))*1.4  )
#
#elif name_of_folder == '15_mm':
#    #personal_gaus.SetParameter(0, 743 )
#    #personal_gaus.SetParameter(1, 66 )
#    #personal_gaus.SetParameter(2, 3.05)
#
#    personal_gaus.SetParLimits(0,max(mean_value_row_list) * .4, max(mean_value_row_list) * 1.2 )
#    personal_gaus.SetParLimits(1, np.mean(x_value) * .3, np.mean(x_value) * 1.4 )
#    personal_gaus.SetParLimits(2,np.std(np.array(x_value)) * .2, np.std(np.array(x_value)) * 1.6 )
#
#
#
else:
    personal_gaus.SetParLimits(0, max(mean_value_row_list) * .4, max(mean_value_row_list) * 1.5 )
    personal_gaus.SetParLimits(1, np.mean(x_value) * .8, np.mean(x_value) * 1.2 )
    personal_gaus.SetParLimits(2, np.std(np.array(x_value)) * .2, np.std(np.array(x_value)) * 1.1 )

errorbar_plot_rows.Fit( personal_gaus, "", "", min(x_value) -0.5 , max( x_value) +0.5 )
errorbar_plot_rows.Draw("ap*")

##################################### create legend ################################################

if plot_style == 'thesis':
    legend = root.TLegend(0.15,0.71,0.37,0.93)
    legend.SetTextSize(0.055)
    legend.AddEntry(errorbar_plot_rows,"Summe Hits","lep")
    legend.AddEntry( personal_gaus,"Fit","l")
    legend.Draw()


else:
    legend = root.TLegend(0.65,0.47,0.98,0.7)
    legend.SetTextSize(0.04)
    legend.AddEntry(errorbar_plot_col,"Row sum hit value","lep")
    legend.AddEntry( personal_gaus,"Gaussian Fit","l")
    legend.Draw()


######## Transfer Sigma from Bin to mumeter ############################

sigma_mu_meter_row = ufloat(personal_gaus.GetParameter(2), personal_gaus.GetParError(2)) * 100 # 100 is pixel size in y direction


#############################################################################

########################################### saveplot and fit params ########################################

with open( f'./fit_params/{name_of_folder}_fit_parameters_row_yaxis.txt', 'w') as file:
    for i in range(0,3):
        file.write( name_params[i] + ' ' + str( personal_gaus.GetParameter(i) ) + ' ' + str(personal_gaus.GetParError(i)) + '\n')

with open( f'./sigma_row_yaxis.txt', 'a') as file:
        file.write( name_params[i] +'_' + name_of_folder + ' ' + str( personal_gaus.GetParameter(2) ) + ' ' + str(personal_gaus.GetParError(2)) + '\n')

with open( f'./sigma_row_in_mumeter_yaxis.txt', 'a') as file:
        file.write( name_params[i] +'_' + name_of_folder + ' ' + str( noms(sigma_mu_meter_row) ) + ' ' + str( stds(sigma_mu_meter_row) ) + '\n')

with open( f'./fit_parameters_row_yaxis.txt', 'a') as file:
        file.write( name_of_folder + 'Amplitude/Sigma/Mean:' + ' ' + str( personal_gaus.GetParameter(0) ) + ' ' + str(personal_gaus.GetParError(0)) + ' ' + str( personal_gaus.GetParameter(1) ) + ' ' + str(personal_gaus.GetParError(1)) + ' ' + str( personal_gaus.GetParameter(2) ) + ' ' + str(personal_gaus.GetParError(2)) + '\n')


c2.SaveAs(f'./plots/{name_of_folder}_erorbar_plot_row.pdf')
