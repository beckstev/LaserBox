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


 ########################## Data of .C file, insert data underneath ######################################
 # !!!!!!!!!!!!!!!! ATTENTION !!!!!!!!!!!!!!!!!!!! At 12 mm I had to use the not zoomed version of .C, becuase the other do not include any data !!!!!!!!!!!!!!!!!!!!!!!!

qMap_Ag_C0_V0 = root.TProfile2D("qMap_Ag_C0_V0","qMap_Ag_C0 (V0)",52,0,52,80,0,80,0,0);
qMap_Ag_C0_V0.SetBinEntries(2398,766);
qMap_Ag_C0_V0.SetBinEntries(2399,30882);
qMap_Ag_C0_V0.SetBinEntries(2400,27501);
qMap_Ag_C0_V0.SetBinEntries(2401,6);
qMap_Ag_C0_V0.SetBinEntries(2452,39429);
qMap_Ag_C0_V0.SetBinEntries(2453,47506);
qMap_Ag_C0_V0.SetBinEntries(2454,32437);
qMap_Ag_C0_V0.SetBinEntries(2455,17547);
qMap_Ag_C0_V0.SetBinEntries(2506,60081);
qMap_Ag_C0_V0.SetBinEntries(2507,60970);
qMap_Ag_C0_V0.SetBinEntries(2508,38567);
qMap_Ag_C0_V0.SetBinEntries(2509,32169);
qMap_Ag_C0_V0.SetBinEntries(2560,59757);
qMap_Ag_C0_V0.SetBinEntries(2561,68381);
qMap_Ag_C0_V0.SetBinEntries(2562,42673);
qMap_Ag_C0_V0.SetBinEntries(2563,31477);
qMap_Ag_C0_V0.SetBinEntries(2614,46510);
qMap_Ag_C0_V0.SetBinEntries(2615,60021);
qMap_Ag_C0_V0.SetBinEntries(2616,46944);
qMap_Ag_C0_V0.SetBinEntries(2617,28919);
qMap_Ag_C0_V0.SetBinEntries(2669,38108);
qMap_Ag_C0_V0.SetBinEntries(2670,34267);
qMap_Ag_C0_V0.SetBinContent(2398,54772);
qMap_Ag_C0_V0.SetBinContent(2399,3680644);
qMap_Ag_C0_V0.SetBinContent(2400,3248506);
qMap_Ag_C0_V0.SetBinContent(2401,458);
qMap_Ag_C0_V0.SetBinContent(2452,7756269);
qMap_Ag_C0_V0.SetBinContent(2453,5682173);
qMap_Ag_C0_V0.SetBinContent(2454,3713081);
qMap_Ag_C0_V0.SetBinContent(2455,1934529);
qMap_Ag_C0_V0.SetBinContent(2506,8268977);
qMap_Ag_C0_V0.SetBinContent(2507,9254173);
qMap_Ag_C0_V0.SetBinContent(2508,5332565);
qMap_Ag_C0_V0.SetBinContent(2509,3880769);
qMap_Ag_C0_V0.SetBinContent(2560,7785578);
qMap_Ag_C0_V0.SetBinContent(2561,1.643886e+07);
qMap_Ag_C0_V0.SetBinContent(2562,1.271932e+07);
qMap_Ag_C0_V0.SetBinContent(2563,4008075);
qMap_Ag_C0_V0.SetBinContent(2614,5407358);
qMap_Ag_C0_V0.SetBinContent(2615,8550902);
qMap_Ag_C0_V0.SetBinContent(2616,8776634);
qMap_Ag_C0_V0.SetBinContent(2617,3446091);
qMap_Ag_C0_V0.SetBinContent(2669,5653963);
qMap_Ag_C0_V0.SetBinContent(2670,3994621);
qMap_Ag_C0_V0.SetBinError(2398,2015.691);
qMap_Ag_C0_V0.SetBinError(2399,197529.9);
qMap_Ag_C0_V0.SetBinError(2400,186185.1);
qMap_Ag_C0_V0.SetBinError(2401,193.0648);
qMap_Ag_C0_V0.SetBinError(2452,449922.7);
qMap_Ag_C0_V0.SetBinError(2453,149054.3);
qMap_Ag_C0_V0.SetBinError(2454,22536.48);
qMap_Ag_C0_V0.SetBinError(2455,15075.53);
qMap_Ag_C0_V0.SetBinError(2506,136119.5);
qMap_Ag_C0_V0.SetBinError(2507,323021.2);
qMap_Ag_C0_V0.SetBinError(2508,29519.39);
qMap_Ag_C0_V0.SetBinError(2509,22877.77);
qMap_Ag_C0_V0.SetBinError(2560,119213.6);
qMap_Ag_C0_V0.SetBinError(2561,697761.9);
qMap_Ag_C0_V0.SetBinError(2562,672134.6);
qMap_Ag_C0_V0.SetBinError(2563,23575.53);
qMap_Ag_C0_V0.SetBinError(2614,162677.5);
qMap_Ag_C0_V0.SetBinError(2615,220446.4);
qMap_Ag_C0_V0.SetBinError(2616,399993.8);
qMap_Ag_C0_V0.SetBinError(2617,21285.97);
qMap_Ag_C0_V0.SetBinError(2669,315107.7);
qMap_Ag_C0_V0.SetBinError(2670,161902.7);
qMap_Ag_C0_V0.SetMinimum(0);
qMap_Ag_C0_V0.SetEntries(844918);
qMap_Ag_C0_V0.SetStats(0);
qMap_Ag_C0_V0.SetContour(20);
qMap_Ag_C0_V0.SetContourLevel(0,0);
qMap_Ag_C0_V0.SetContourLevel(1,14.90325);
qMap_Ag_C0_V0.SetContourLevel(2,29.80649);
qMap_Ag_C0_V0.SetContourLevel(3,44.70974);
qMap_Ag_C0_V0.SetContourLevel(4,59.61299);
qMap_Ag_C0_V0.SetContourLevel(5,74.51623);
qMap_Ag_C0_V0.SetContourLevel(6,89.41948);
qMap_Ag_C0_V0.SetContourLevel(7,104.3227);
qMap_Ag_C0_V0.SetContourLevel(8,119.226);
qMap_Ag_C0_V0.SetContourLevel(9,134.1292);
qMap_Ag_C0_V0.SetContourLevel(10,149.0325);
qMap_Ag_C0_V0.SetContourLevel(11,163.9357);
qMap_Ag_C0_V0.SetContourLevel(12,178.839);
qMap_Ag_C0_V0.SetContourLevel(13,193.7422);
qMap_Ag_C0_V0.SetContourLevel(14,208.6455);
qMap_Ag_C0_V0.SetContourLevel(15,223.5487);
qMap_Ag_C0_V0.SetContourLevel(16,238.4519);
qMap_Ag_C0_V0.SetContourLevel(17,253.3552);
qMap_Ag_C0_V0.SetContourLevel(18,268.2584);
qMap_Ag_C0_V0.SetContourLevel(19,283.1617);

ci = root.TColor.GetColor("#000099");
qMap_Ag_C0_V0.SetLineColor(ci);
qMap_Ag_C0_V0.GetXaxis().SetTitle("col");
qMap_Ag_C0_V0.GetXaxis().SetRange(1,52);
qMap_Ag_C0_V0.GetXaxis().SetNdivisions(508);
qMap_Ag_C0_V0.GetXaxis().SetLabelFont(42);
qMap_Ag_C0_V0.GetXaxis().SetLabelSize(0.05);
qMap_Ag_C0_V0.GetXaxis().SetTitleSize(0.05);
qMap_Ag_C0_V0.GetXaxis().SetTitleOffset(1.1);
qMap_Ag_C0_V0.GetXaxis().SetTitleFont(42);
qMap_Ag_C0_V0.GetYaxis().SetTitle("row");
qMap_Ag_C0_V0.GetYaxis().SetRange(1,80);
qMap_Ag_C0_V0.GetYaxis().SetLabelFont(42);
qMap_Ag_C0_V0.GetYaxis().SetLabelSize(0.05);
qMap_Ag_C0_V0.GetYaxis().SetTitleSize(0.05);
qMap_Ag_C0_V0.GetYaxis().SetTitleOffset(1.1);
qMap_Ag_C0_V0.GetYaxis().SetTitleFont(42);
qMap_Ag_C0_V0.GetZaxis().SetLabelFont(42);
qMap_Ag_C0_V0.GetZaxis().SetLabelSize(0.035);
qMap_Ag_C0_V0.GetZaxis().SetTitleSize(0.035);
qMap_Ag_C0_V0.GetZaxis().SetTitleFont(42);

root.gStyle.SetOptTitle(0)
##################################################### Insert Data above line #############################




############################### Get name of folder #################################

name_of_folder = os.path.basename( os.getcwd() )


############################### Save Data in list #######################################

mean_value_col_list = []
mean_error_col_list = []
x_value = []
y_value = []


##############################################################################################################################

################################### Getting the mean hit value of all columns near the laserspot #############################

###############################################################################################################################


################################## Set sum area ###############################

xmin = 18
xmax = 27

ymin = 40
ymax = 52

####################################  calculating mean of each coloum ################################

for i in range(xmin,xmax): # going thru all col
    content = []
    error = []

    x_value.append(i)
    y_value.append(0)

    for j in range(ymin,ymax): # going thru all rows
        content.append( qMap_Ag_C0_V0.GetBinContent(i,j))
        error.append( qMap_Ag_C0_V0.GetBinError(i,j)) # Is this the real error

    content_bin = unp.uarray( content, error)
    mean_content_col = content_bin.mean() # mean value of each bin in the col

    # Saving values in lists
    mean_value_col_list.append( noms(mean_content_col))
    mean_error_col_list.append( stds(mean_content_col))


########################### Create errorbar plot #####################################

errorbar_plot_col = root.TGraphErrors( len(x_value), array( 'f', x_value), array( 'f', mean_value_col_list), array( 'f', y_value), array( 'f', mean_error_col_list) )

############################## Set axis label of errobar plot ##################################

errorbar_plot_col.GetXaxis().SetTitle("Col")
errorbar_plot_col.GetYaxis().SetTitle("Mean Hit / Vcal")

####################### create Canvas ##########################################

c1 = root.TCanvas("c1", "c1", 1980, 1080)
errorbar_plot_col.Fit('gaus')
errorbar_plot_col.Draw("ALP")

name_params = [ "amplitude/[MeanVcal]", "mean/[Col]", "sigma/[Col]"]

############################### Create legend ####################################
gaus_fit_col = errorbar_plot_col.GetFunction('gaus')
legend = root.TLegend(0.75,0.75,0.98,0.98)
legend.AddEntry(errorbar_plot_col,"Coloumn mean hit value","lep")
legend.AddEntry( gaus_fit_col,"Gaussian Fit","l")
legend.Draw()

############################### Save parameter and plot ###########################################

with open( f'../fit_params/{name_of_folder}_fit_parameters_col_xaxis.txt', 'w') as file:
    for i in range(0,3):
        file.write( name_params[i] + ' ' + str( gaus_fit_col.GetParameter(i) ) + ' ' + str(gaus_fit_col.GetParError(i)) + '\n')

with open( f'../sigma_col_xaxis.txt', 'a') as file:
        file.write( name_params[i] + '_' + name_of_folder + ' ' + str( gaus_fit_col.GetParameter(2) ) + ' ' + str(gaus_fit_col.GetParError(2)) + '\n')


c1.SaveAs(f'../plots/{name_of_folder}_erorbar_plot_col.pdf')



##############################################################################################################################

################################### Getting the mean hit value of all rows near the laserspot #############################

###############################################################################################################################


############################Reset lists###########################################
mean_value_col_list = []
mean_error_col_list = []
x_value = []
y_value = []


#################################### calculating mean of each row #####################################

for i in range(ymin,ymax): # going thru all rows
    content = []
    error = []

    x_value.append(i)
    y_value.append(0)

    for j in range(xmin,xmax): # going thru all col
        content.append( qMap_Ag_C0_V0.GetBinContent(j,i))
        error.append( qMap_Ag_C0_V0.GetBinError(j,i)) # Is this the real error

    content_bin = unp.uarray( content, error)
    mean_content_col = content_bin.mean() # mean value of each bin in the col

    # Saving values in lists
    mean_value_col_list.append( noms(mean_content_col))
    mean_error_col_list.append( stds(mean_content_col))


############################# Create new errorbar plot ####################################
errorbar_plot_rows = root.TGraphErrors( len(x_value), array( 'f', x_value), array( 'f', mean_value_col_list), array( 'f', y_value), array( 'f', mean_error_col_list) )

############################### create Canvas ########################################
c2 = root.TCanvas("c2", "c2", 1980, 1080);

############################## Set axis label of errobar plot ##################################

errorbar_plot_rows.GetXaxis().SetTitle("Row")
errorbar_plot_rows.GetYaxis().SetTitle("Mean Hit / Vcal")


############################### Plot fucntion and fit #############################################
errorbar_plot_rows.Fit('gaus')
errorbar_plot_rows.Draw("ALP")

##################################### create legend ################################################
gaus_fit_row = errorbar_plot_rows.GetFunction('gaus')
legend = root.TLegend(0.75,0.75,0.98,0.98)
legend.AddEntry(errorbar_plot_rows,"Mean Mean Vcal of each row","lep")
legend.AddEntry( gaus_fit_row,"Gaussian Fit","l")
legend.Draw()

########################################### saveplot and fit params ########################################
with open( f'../fit_params/{name_of_folder}_fit_parameters_row_yaxis.txt', 'w') as file:
    for i in range(0,3):
        file.write( name_params[i] + ' ' + str( gaus_fit_row.GetParameter(i) ) + ' ' + str(gaus_fit_row.GetParError(i)) + '\n')

with open( f'../sigma_row_yaxis.txt', 'a') as file:
        file.write( name_params[i] +'_' + name_of_folder + ' ' + str( gaus_fit_row.GetParameter(2) ) + ' ' + str(gaus_fit_row.GetParError(2)) + '\n')


c2.SaveAs(f'../plots/{name_of_folder}_erorbar_plot_row.pdf')
