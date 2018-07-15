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
#!!!!!!!!!!!!!!!! ATTENTION !!!!!!!!!!!!!!!!!!!! At 13 mm I had to use the not zoomed version of .C, becuase the other do not include any data !!!!!!!!!!!!!!!!!!!!!!!!


qMap_Ag_C0_V0 = root.TProfile2D("qMap_Ag_C0_V0","qMap_Ag_C0 (V0)",52,0,52,80,0,80,0,0);
qMap_Ag_C0_V0.SetBinEntries(2344,19);
qMap_Ag_C0_V0.SetBinEntries(2345,14183);
qMap_Ag_C0_V0.SetBinEntries(2346,14333);
qMap_Ag_C0_V0.SetBinEntries(2347,2);
qMap_Ag_C0_V0.SetBinEntries(2398,16046);
qMap_Ag_C0_V0.SetBinEntries(2399,17020);
qMap_Ag_C0_V0.SetBinEntries(2400,14729);
qMap_Ag_C0_V0.SetBinEntries(2401,14369);
qMap_Ag_C0_V0.SetBinEntries(2451,14419);
qMap_Ag_C0_V0.SetBinEntries(2452,32449);
qMap_Ag_C0_V0.SetBinEntries(2453,32476);
qMap_Ag_C0_V0.SetBinEntries(2454,25302);
qMap_Ag_C0_V0.SetBinEntries(2455,14472);
qMap_Ag_C0_V0.SetBinEntries(2505,14523);
qMap_Ag_C0_V0.SetBinEntries(2506,44794);
qMap_Ag_C0_V0.SetBinEntries(2507,51170);
qMap_Ag_C0_V0.SetBinEntries(2508,33516);
qMap_Ag_C0_V0.SetBinEntries(2509,20073);
qMap_Ag_C0_V0.SetBinEntries(2559,14075);
qMap_Ag_C0_V0.SetBinEntries(2560,48868);
qMap_Ag_C0_V0.SetBinEntries(2561,58641);
qMap_Ag_C0_V0.SetBinEntries(2562,42812);
qMap_Ag_C0_V0.SetBinEntries(2563,17004);
qMap_Ag_C0_V0.SetBinEntries(2613,14522);
qMap_Ag_C0_V0.SetBinEntries(2614,51382);
qMap_Ag_C0_V0.SetBinEntries(2615,50565);
qMap_Ag_C0_V0.SetBinEntries(2616,44027);
qMap_Ag_C0_V0.SetBinEntries(2617,21044);
qMap_Ag_C0_V0.SetBinEntries(2618,26);
qMap_Ag_C0_V0.SetBinEntries(2668,39093);
qMap_Ag_C0_V0.SetBinEntries(2669,39409);
qMap_Ag_C0_V0.SetBinEntries(2670,30846);
qMap_Ag_C0_V0.SetBinEntries(2671,18157);
qMap_Ag_C0_V0.SetBinEntries(2723,17396);
qMap_Ag_C0_V0.SetBinEntries(2724,14476);
qMap_Ag_C0_V0.SetBinContent(2344,1727);
qMap_Ag_C0_V0.SetBinContent(2345,1541144);
qMap_Ag_C0_V0.SetBinContent(2346,1448396);
qMap_Ag_C0_V0.SetBinContent(2347,188);
qMap_Ag_C0_V0.SetBinContent(2398,1930663);
qMap_Ag_C0_V0.SetBinContent(2399,2260151);
qMap_Ag_C0_V0.SetBinContent(2400,1813706);
qMap_Ag_C0_V0.SetBinContent(2401,1458013);
qMap_Ag_C0_V0.SetBinContent(2451,1170875);
qMap_Ag_C0_V0.SetBinContent(2452,3727473);
qMap_Ag_C0_V0.SetBinContent(2453,4640774);
qMap_Ag_C0_V0.SetBinContent(2454,3218252);
qMap_Ag_C0_V0.SetBinContent(2455,1685736);
qMap_Ag_C0_V0.SetBinContent(2505,1776388);
qMap_Ag_C0_V0.SetBinContent(2506,5142724);
qMap_Ag_C0_V0.SetBinContent(2507,6040486);
qMap_Ag_C0_V0.SetBinContent(2508,4818365);
qMap_Ag_C0_V0.SetBinContent(2509,2239111);
qMap_Ag_C0_V0.SetBinContent(2559,1975378);
qMap_Ag_C0_V0.SetBinContent(2560,5531553);
qMap_Ag_C0_V0.SetBinContent(2561,8887634);
qMap_Ag_C0_V0.SetBinContent(2562,1.672008e+07);
qMap_Ag_C0_V0.SetBinContent(2563,2151277);
qMap_Ag_C0_V0.SetBinContent(2613,1603932);
qMap_Ag_C0_V0.SetBinContent(2614,5852932);
qMap_Ag_C0_V0.SetBinContent(2615,5665718);
qMap_Ag_C0_V0.SetBinContent(2616,5689668);
qMap_Ag_C0_V0.SetBinContent(2617,2508568);
qMap_Ag_C0_V0.SetBinContent(2618,2136);
qMap_Ag_C0_V0.SetBinContent(2668,4186165);
qMap_Ag_C0_V0.SetBinContent(2669,4672891);
qMap_Ag_C0_V0.SetBinContent(2670,3811861);
qMap_Ag_C0_V0.SetBinContent(2671,2255823);
qMap_Ag_C0_V0.SetBinContent(2723,2049516);
qMap_Ag_C0_V0.SetBinContent(2724,1700067);
qMap_Ag_C0_V0.SetBinError(2344,402.8734);
qMap_Ag_C0_V0.SetBinError(2345,12979.8);
qMap_Ag_C0_V0.SetBinError(2346,12166.45);
qMap_Ag_C0_V0.SetBinError(2347,134.4024);
qMap_Ag_C0_V0.SetBinError(2398,93836.64);
qMap_Ag_C0_V0.SetBinError(2399,161228.9);
qMap_Ag_C0_V0.SetBinError(2400,114305.9);
qMap_Ag_C0_V0.SetBinError(2401,12252.54);
qMap_Ag_C0_V0.SetBinError(2451,9901.228);
qMap_Ag_C0_V0.SetBinError(2452,147939.1);
qMap_Ag_C0_V0.SetBinError(2453,293709.8);
qMap_Ag_C0_V0.SetBinError(2454,218026.8);
qMap_Ag_C0_V0.SetBinError(2455,14092.93);
qMap_Ag_C0_V0.SetBinError(2505,14969.22);
qMap_Ag_C0_V0.SetBinError(2506,26160.92);
qMap_Ag_C0_V0.SetBinError(2507,198427.4);
qMap_Ag_C0_V0.SetBinError(2508,246180.4);
qMap_Ag_C0_V0.SetBinError(2509,16509.44);
qMap_Ag_C0_V0.SetBinError(2559,16717.33);
qMap_Ag_C0_V0.SetBinError(2560,27341.63);
qMap_Ag_C0_V0.SetBinError(2561,366223.7);
qMap_Ag_C0_V0.SetBinError(2562,886649);
qMap_Ag_C0_V0.SetBinError(2563,16870.58);
qMap_Ag_C0_V0.SetBinError(2613,13409.44);
qMap_Ag_C0_V0.SetBinError(2614,29248.24);
qMap_Ag_C0_V0.SetBinError(2615,96545.96);
qMap_Ag_C0_V0.SetBinError(2616,208872.5);
qMap_Ag_C0_V0.SetBinError(2617,17967.6);
qMap_Ag_C0_V0.SetBinError(2618,423.1099);
qMap_Ag_C0_V0.SetBinError(2668,69887.67);
qMap_Ag_C0_V0.SetBinError(2669,148421.3);
qMap_Ag_C0_V0.SetBinError(2670,161830.9);
qMap_Ag_C0_V0.SetBinError(2671,17107.6);
qMap_Ag_C0_V0.SetBinError(2723,16283.99);
qMap_Ag_C0_V0.SetBinError(2724,14283.94);
qMap_Ag_C0_V0.SetMinimum(0);
qMap_Ag_C0_V0.SetEntries(896238);
qMap_Ag_C0_V0.SetStats(0);
qMap_Ag_C0_V0.SetContour(20);
qMap_Ag_C0_V0.SetContourLevel(0,0);
qMap_Ag_C0_V0.SetContourLevel(1,19.52733);
qMap_Ag_C0_V0.SetContourLevel(2,39.05465);
qMap_Ag_C0_V0.SetContourLevel(3,58.58198);
qMap_Ag_C0_V0.SetContourLevel(4,78.10931);
qMap_Ag_C0_V0.SetContourLevel(5,97.63663);
qMap_Ag_C0_V0.SetContourLevel(6,117.164);
qMap_Ag_C0_V0.SetContourLevel(7,136.6913);
qMap_Ag_C0_V0.SetContourLevel(8,156.2186);
qMap_Ag_C0_V0.SetContourLevel(9,175.7459);
qMap_Ag_C0_V0.SetContourLevel(10,195.2733);
qMap_Ag_C0_V0.SetContourLevel(11,214.8006);
qMap_Ag_C0_V0.SetContourLevel(12,234.3279);
qMap_Ag_C0_V0.SetContourLevel(13,253.8552);
qMap_Ag_C0_V0.SetContourLevel(14,273.3826);
qMap_Ag_C0_V0.SetContourLevel(15,292.9099);
qMap_Ag_C0_V0.SetContourLevel(16,312.4372);
qMap_Ag_C0_V0.SetContourLevel(17,331.9645);
qMap_Ag_C0_V0.SetContourLevel(18,351.4919);
qMap_Ag_C0_V0.SetContourLevel(19,371.0192);

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
