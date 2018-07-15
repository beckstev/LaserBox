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

qMap_Ag_C0_V0 = root.TProfile2D("qMap_Ag_C0_V0","qMap_Ag_C0 (V0)",52,0,52,80,0,80,0,0);
qMap_Ag_C0_V0.SetBinEntries(2344,1751);
qMap_Ag_C0_V0.SetBinEntries(2345,13606);
qMap_Ag_C0_V0.SetBinEntries(2346,3);
qMap_Ag_C0_V0.SetBinEntries(2397,83);
qMap_Ag_C0_V0.SetBinEntries(2398,14436);
qMap_Ag_C0_V0.SetBinEntries(2399,14317);
qMap_Ag_C0_V0.SetBinEntries(2400,14371);
qMap_Ag_C0_V0.SetBinEntries(2451,14518);
qMap_Ag_C0_V0.SetBinEntries(2452,55056);
qMap_Ag_C0_V0.SetBinEntries(2453,57458);
qMap_Ag_C0_V0.SetBinEntries(2454,14335);
qMap_Ag_C0_V0.SetBinEntries(2455,1413);
qMap_Ag_C0_V0.SetBinEntries(2505,14452);
qMap_Ag_C0_V0.SetBinEntries(2506,89375);
qMap_Ag_C0_V0.SetBinEntries(2507,84660);
qMap_Ag_C0_V0.SetBinEntries(2508,19176);
qMap_Ag_C0_V0.SetBinEntries(2509,6654);
qMap_Ag_C0_V0.SetBinEntries(2559,14521);
qMap_Ag_C0_V0.SetBinEntries(2560,80034);
qMap_Ag_C0_V0.SetBinEntries(2561,90658);
qMap_Ag_C0_V0.SetBinEntries(2562,17511);
qMap_Ag_C0_V0.SetBinEntries(2563,62);
qMap_Ag_C0_V0.SetBinEntries(2613,150);
qMap_Ag_C0_V0.SetBinEntries(2614,17076);
qMap_Ag_C0_V0.SetBinEntries(2615,36260);
qMap_Ag_C0_V0.SetBinEntries(2616,14546);
qMap_Ag_C0_V0.SetBinEntries(2668,10793);
qMap_Ag_C0_V0.SetBinEntries(2669,13073);
qMap_Ag_C0_V0.SetBinContent(2344,155344);
qMap_Ag_C0_V0.SetBinContent(2345,1128042);
qMap_Ag_C0_V0.SetBinContent(2346,275);
qMap_Ag_C0_V0.SetBinContent(2397,4606);
qMap_Ag_C0_V0.SetBinContent(2398,1711722);
qMap_Ag_C0_V0.SetBinContent(2399,1836729);
qMap_Ag_C0_V0.SetBinContent(2400,1408068);
qMap_Ag_C0_V0.SetBinContent(2451,985426);
qMap_Ag_C0_V0.SetBinContent(2452,6480075);
qMap_Ag_C0_V0.SetBinContent(2453,9177472);
qMap_Ag_C0_V0.SetBinContent(2454,1783801);
qMap_Ag_C0_V0.SetBinContent(2455,114572);
qMap_Ag_C0_V0.SetBinContent(2505,1367722);
qMap_Ag_C0_V0.SetBinContent(2506,1.482972e+07);
qMap_Ag_C0_V0.SetBinContent(2507,4.668824e+07);
qMap_Ag_C0_V0.SetBinContent(2508,2599669);
qMap_Ag_C0_V0.SetBinContent(2509,623834);
qMap_Ag_C0_V0.SetBinContent(2559,1312394);
qMap_Ag_C0_V0.SetBinContent(2560,1.394541e+07);
qMap_Ag_C0_V0.SetBinContent(2561,1.95714e+07);
qMap_Ag_C0_V0.SetBinContent(2562,6382667);
qMap_Ag_C0_V0.SetBinContent(2563,5933);
qMap_Ag_C0_V0.SetBinContent(2613,12218);
qMap_Ag_C0_V0.SetBinContent(2614,2172727);
qMap_Ag_C0_V0.SetBinContent(2615,3681722);
qMap_Ag_C0_V0.SetBinContent(2616,1496081);
qMap_Ag_C0_V0.SetBinContent(2668,829080);
qMap_Ag_C0_V0.SetBinContent(2669,1165780);
qMap_Ag_C0_V0.SetBinError(2344,3769.952);
qMap_Ag_C0_V0.SetBinError(2345,9888.298);
qMap_Ag_C0_V0.SetBinError(2346,159.54);
qMap_Ag_C0_V0.SetBinError(2397,516.0407);
qMap_Ag_C0_V0.SetBinError(2398,14276.88);
qMap_Ag_C0_V0.SetBinError(2399,15418.18);
qMap_Ag_C0_V0.SetBinError(2400,11864.88);
qMap_Ag_C0_V0.SetBinError(2451,8326.981);
qMap_Ag_C0_V0.SetBinError(2452,117610.6);
qMap_Ag_C0_V0.SetBinError(2453,366432.5);
qMap_Ag_C0_V0.SetBinError(2454,14962.44);
qMap_Ag_C0_V0.SetBinError(2455,3103.91);
qMap_Ag_C0_V0.SetBinError(2505,11494.87);
qMap_Ag_C0_V0.SetBinError(2506,225151.8);
qMap_Ag_C0_V0.SetBinError(2507,1398062);
qMap_Ag_C0_V0.SetBinError(2508,19570.16);
qMap_Ag_C0_V0.SetBinError(2509,7760.907);
qMap_Ag_C0_V0.SetBinError(2559,11063.44);
qMap_Ag_C0_V0.SetBinError(2560,565151.2);
qMap_Ag_C0_V0.SetBinError(2561,481702.2);
qMap_Ag_C0_V0.SetBinError(2562,524473.1);
qMap_Ag_C0_V0.SetBinError(2563,762.9856);
qMap_Ag_C0_V0.SetBinError(2613,1020.252);
qMap_Ag_C0_V0.SetBinError(2614,17352.26);
qMap_Ag_C0_V0.SetBinError(2615,21992.88);
qMap_Ag_C0_V0.SetBinError(2616,12498.79);
qMap_Ag_C0_V0.SetBinError(2668,8216.387);
qMap_Ag_C0_V0.SetBinError(2669,10342.23);
qMap_Ag_C0_V0.SetMinimum(0);
qMap_Ag_C0_V0.SetEntries(710348);
qMap_Ag_C0_V0.SetStats(0);
qMap_Ag_C0_V0.SetContour(20);
qMap_Ag_C0_V0.SetContourLevel(0,0);
qMap_Ag_C0_V0.SetContourLevel(1,27.57397);
qMap_Ag_C0_V0.SetContourLevel(2,55.14794);
qMap_Ag_C0_V0.SetContourLevel(3,82.7219);
qMap_Ag_C0_V0.SetContourLevel(4,110.2959);
qMap_Ag_C0_V0.SetContourLevel(5,137.8698);
qMap_Ag_C0_V0.SetContourLevel(6,165.4438);
qMap_Ag_C0_V0.SetContourLevel(7,193.0178);
qMap_Ag_C0_V0.SetContourLevel(8,220.5917);
qMap_Ag_C0_V0.SetContourLevel(9,248.1657);
qMap_Ag_C0_V0.SetContourLevel(10,275.7397);
qMap_Ag_C0_V0.SetContourLevel(11,303.3137);
qMap_Ag_C0_V0.SetContourLevel(12,330.8876);
qMap_Ag_C0_V0.SetContourLevel(13,358.4616);
qMap_Ag_C0_V0.SetContourLevel(14,386.0356);
qMap_Ag_C0_V0.SetContourLevel(15,413.6095);
qMap_Ag_C0_V0.SetContourLevel(16,441.1835);
qMap_Ag_C0_V0.SetContourLevel(17,468.7575);
qMap_Ag_C0_V0.SetContourLevel(18,496.3314);
qMap_Ag_C0_V0.SetContourLevel(19,523.9054);

ci = root.TColor.GetColor("#000099");
qMap_Ag_C0_V0.SetLineColor(ci);
qMap_Ag_C0_V0.GetXaxis().SetTitle("col");
qMap_Ag_C0_V0.GetXaxis().SetRange(16,31);
qMap_Ag_C0_V0.GetXaxis().SetNdivisions(508);
qMap_Ag_C0_V0.GetXaxis().SetLabelFont(42);
qMap_Ag_C0_V0.GetXaxis().SetLabelSize(0.05);
qMap_Ag_C0_V0.GetXaxis().SetTitleSize(0.05);
qMap_Ag_C0_V0.GetXaxis().SetTitleOffset(1.1);
qMap_Ag_C0_V0.GetXaxis().SetTitleFont(42);
qMap_Ag_C0_V0.GetYaxis().SetTitle("row");
qMap_Ag_C0_V0.GetYaxis().SetRange(30,60);
qMap_Ag_C0_V0.GetYaxis().SetLabelFont(42);
qMap_Ag_C0_V0.GetYaxis().SetLabelSize(0.05);
qMap_Ag_C0_V0.GetYaxis().SetTitleSize(0.05);
qMap_Ag_C0_V0.GetYaxis().SetTitleOffset(1.1);
qMap_Ag_C0_V0.GetYaxis().SetTitleFont(42);
qMap_Ag_C0_V0.GetZaxis().SetLabelFont(42);
qMap_Ag_C0_V0.GetZaxis().SetLabelSize(0.035);
qMap_Ag_C0_V0.GetZaxis().SetTitleSize(0.035);
qMap_Ag_C0_V0.GetZaxis().SetTitleFont(42);


root.gStyle.SetOptTitle(0) # no title
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

name_params = [ "amplitude/[MeanVcal]", "mean/[Bin]", "sigma/[Bin]"]

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
