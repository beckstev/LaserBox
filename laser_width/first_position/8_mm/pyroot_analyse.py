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
qMap_Ag_C0_V0.SetBinEntries(2398,475);
qMap_Ag_C0_V0.SetBinEntries(2399,53);
qMap_Ag_C0_V0.SetBinEntries(2452,17960);
qMap_Ag_C0_V0.SetBinEntries(2453,20947);
qMap_Ag_C0_V0.SetBinEntries(2505,14);
qMap_Ag_C0_V0.SetBinEntries(2506,96610);
qMap_Ag_C0_V0.SetBinEntries(2507,71998);
qMap_Ag_C0_V0.SetBinEntries(2508,4);
qMap_Ag_C0_V0.SetBinEntries(2560,60905);
qMap_Ag_C0_V0.SetBinEntries(2561,26300);
qMap_Ag_C0_V0.SetBinEntries(2614,203);
qMap_Ag_C0_V0.SetBinContent(2398,21489);
qMap_Ag_C0_V0.SetBinContent(2399,2567);
qMap_Ag_C0_V0.SetBinContent(2452,2484134);
qMap_Ag_C0_V0.SetBinContent(2453,1736812);
qMap_Ag_C0_V0.SetBinContent(2505,588);
qMap_Ag_C0_V0.SetBinContent(2506,3.779257e+07);
qMap_Ag_C0_V0.SetBinContent(2507,1.138812e+07);
qMap_Ag_C0_V0.SetBinContent(2508,238);
qMap_Ag_C0_V0.SetBinContent(2560,9969095);
qMap_Ag_C0_V0.SetBinContent(2561,3129128);
qMap_Ag_C0_V0.SetBinContent(2614,9838);
qMap_Ag_C0_V0.SetBinError(2398,1015.413);
qMap_Ag_C0_V0.SetBinError(2399,372.1814);
qMap_Ag_C0_V0.SetBinError(2452,94536.17);
qMap_Ag_C0_V0.SetBinError(2453,12606.79);
qMap_Ag_C0_V0.SetBinError(2505,162.5977);
qMap_Ag_C0_V0.SetBinError(2506,318028.3);
qMap_Ag_C0_V0.SetBinError(2507,355299);
qMap_Ag_C0_V0.SetBinError(2508,120.5073);
qMap_Ag_C0_V0.SetBinError(2560,528936);
qMap_Ag_C0_V0.SetBinError(2561,68615.32);
qMap_Ag_C0_V0.SetBinError(2614,709.8141);
qMap_Ag_C0_V0.SetMinimum(0);
qMap_Ag_C0_V0.SetEntries(295469);
qMap_Ag_C0_V0.SetStats(0);
qMap_Ag_C0_V0.SetContour(20);
qMap_Ag_C0_V0.SetContourLevel(0,0);
qMap_Ag_C0_V0.SetContourLevel(1,19.55935);
qMap_Ag_C0_V0.SetContourLevel(2,39.11869);
qMap_Ag_C0_V0.SetContourLevel(3,58.67804);
qMap_Ag_C0_V0.SetContourLevel(4,78.23739);
qMap_Ag_C0_V0.SetContourLevel(5,97.79673);
qMap_Ag_C0_V0.SetContourLevel(6,117.3561);
qMap_Ag_C0_V0.SetContourLevel(7,136.9154);
qMap_Ag_C0_V0.SetContourLevel(8,156.4748);
qMap_Ag_C0_V0.SetContourLevel(9,176.0341);
qMap_Ag_C0_V0.SetContourLevel(10,195.5935);
qMap_Ag_C0_V0.SetContourLevel(11,215.1528);
qMap_Ag_C0_V0.SetContourLevel(12,234.7122);
qMap_Ag_C0_V0.SetContourLevel(13,254.2715);
qMap_Ag_C0_V0.SetContourLevel(14,273.8308);
qMap_Ag_C0_V0.SetContourLevel(15,293.3902);
qMap_Ag_C0_V0.SetContourLevel(16,312.9495);
qMap_Ag_C0_V0.SetContourLevel(17,332.5089);
qMap_Ag_C0_V0.SetContourLevel(18,352.0682);
qMap_Ag_C0_V0.SetContourLevel(19,371.6276);

ci = root.TColor.GetColor("#000099");
qMap_Ag_C0_V0.SetLineColor(ci);
qMap_Ag_C0_V0.GetXaxis().SetTitle("col");
qMap_Ag_C0_V0.GetXaxis().SetRange(16,30);
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
