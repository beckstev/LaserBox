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

qMap_Ag_C0_V0 =  root.TProfile2D("qMap_Ag_C0_V0","qMap_Ag_C0 (V0)",52,0,52,80,0,80,0,0);
qMap_Ag_C0_V0.SetBinEntries(2344,13);
qMap_Ag_C0_V0.SetBinEntries(2345,3259);
qMap_Ag_C0_V0.SetBinEntries(2398,14432);
qMap_Ag_C0_V0.SetBinEntries(2399,14421);
qMap_Ag_C0_V0.SetBinEntries(2400,12126);
qMap_Ag_C0_V0.SetBinEntries(2451,14054);
qMap_Ag_C0_V0.SetBinEntries(2452,30380);
qMap_Ag_C0_V0.SetBinEntries(2453,32456);
qMap_Ag_C0_V0.SetBinEntries(2454,14496);
qMap_Ag_C0_V0.SetBinEntries(2455,3);
qMap_Ag_C0_V0.SetBinEntries(2505,14405);
qMap_Ag_C0_V0.SetBinEntries(2506,85997);
qMap_Ag_C0_V0.SetBinEntries(2507,86887);
qMap_Ag_C0_V0.SetBinEntries(2508,14652);
qMap_Ag_C0_V0.SetBinEntries(2509,330);
qMap_Ag_C0_V0.SetBinEntries(2559,13898);
qMap_Ag_C0_V0.SetBinEntries(2560,82256);
qMap_Ag_C0_V0.SetBinEntries(2561,92374);
qMap_Ag_C0_V0.SetBinEntries(2562,14525);
qMap_Ag_C0_V0.SetBinEntries(2563,1);
qMap_Ag_C0_V0.SetBinEntries(2613,1);
qMap_Ag_C0_V0.SetBinEntries(2614,15132);
qMap_Ag_C0_V0.SetBinEntries(2615,17206);
qMap_Ag_C0_V0.SetBinEntries(2616,14498);
qMap_Ag_C0_V0.SetBinEntries(2668,2811);
qMap_Ag_C0_V0.SetBinEntries(2669,5128);
qMap_Ag_C0_V0.SetBinContent(2344,1217);
qMap_Ag_C0_V0.SetBinContent(2345,249696);
qMap_Ag_C0_V0.SetBinContent(2398,1593387);
qMap_Ag_C0_V0.SetBinContent(2399,1609096);
qMap_Ag_C0_V0.SetBinContent(2400,1039430);
qMap_Ag_C0_V0.SetBinContent(2451,810094);
qMap_Ag_C0_V0.SetBinContent(2452,6577174);
qMap_Ag_C0_V0.SetBinContent(2453,6034978);
qMap_Ag_C0_V0.SetBinContent(2454,1633967);
qMap_Ag_C0_V0.SetBinContent(2455,240);
qMap_Ag_C0_V0.SetBinContent(2505,1135827);
qMap_Ag_C0_V0.SetBinContent(2506,1.828997e+07);
qMap_Ag_C0_V0.SetBinContent(2507,2.851462e+07);
qMap_Ag_C0_V0.SetBinContent(2508,2175345);
qMap_Ag_C0_V0.SetBinContent(2509,27517);
qMap_Ag_C0_V0.SetBinContent(2559,1189464);
qMap_Ag_C0_V0.SetBinContent(2560,1.510106e+07);
qMap_Ag_C0_V0.SetBinContent(2561,3.20364e+07);
qMap_Ag_C0_V0.SetBinContent(2562,2030728);
qMap_Ag_C0_V0.SetBinContent(2563,101);
qMap_Ag_C0_V0.SetBinContent(2613,85);
qMap_Ag_C0_V0.SetBinContent(2614,1870582);
qMap_Ag_C0_V0.SetBinContent(2615,2440443);
qMap_Ag_C0_V0.SetBinContent(2616,1281466);
qMap_Ag_C0_V0.SetBinContent(2668,230173);
qMap_Ag_C0_V0.SetBinContent(2669,397530);
qMap_Ag_C0_V0.SetBinError(2344,340.1897);
qMap_Ag_C0_V0.SetBinError(2345,4484.731);
qMap_Ag_C0_V0.SetBinError(2398,13337.84);
qMap_Ag_C0_V0.SetBinError(2399,13485.52);
qMap_Ag_C0_V0.SetBinError(2400,66153.57);
qMap_Ag_C0_V0.SetBinError(2451,6984.873);
qMap_Ag_C0_V0.SetBinError(2452,430311.7);
qMap_Ag_C0_V0.SetBinError(2453,322230.1);
qMap_Ag_C0_V0.SetBinError(2454,13634.97);
qMap_Ag_C0_V0.SetBinError(2455,139.9214);
qMap_Ag_C0_V0.SetBinError(2505,9604.122);
qMap_Ag_C0_V0.SetBinError(2506,531939.9);
qMap_Ag_C0_V0.SetBinError(2507,846602.9);
qMap_Ag_C0_V0.SetBinError(2508,18055.27);
qMap_Ag_C0_V0.SetBinError(2509,1547.359);
qMap_Ag_C0_V0.SetBinError(2559,10232.71);
qMap_Ag_C0_V0.SetBinError(2560,595117.9);
qMap_Ag_C0_V0.SetBinError(2561,981576.4);
qMap_Ag_C0_V0.SetBinError(2562,16931.76);
qMap_Ag_C0_V0.SetBinError(2563,101);
qMap_Ag_C0_V0.SetBinError(2613,85);
qMap_Ag_C0_V0.SetBinError(2614,15433.69);
qMap_Ag_C0_V0.SetBinError(2615,19231.87);
qMap_Ag_C0_V0.SetBinError(2616,10786.81);
qMap_Ag_C0_V0.SetBinError(2668,4413.904);
qMap_Ag_C0_V0.SetBinError(2669,5693.815);
qMap_Ag_C0_V0.SetMinimum(0);
qMap_Ag_C0_V0.SetEntries(595741);
qMap_Ag_C0_V0.SetStats(0);
qMap_Ag_C0_V0.SetContour(20);
qMap_Ag_C0_V0.SetContourLevel(0,0);
qMap_Ag_C0_V0.SetContourLevel(1,17.34059);
qMap_Ag_C0_V0.SetContourLevel(2,34.68119);
qMap_Ag_C0_V0.SetContourLevel(3,52.02178);
qMap_Ag_C0_V0.SetContourLevel(4,69.36237);
qMap_Ag_C0_V0.SetContourLevel(5,86.70297);
qMap_Ag_C0_V0.SetContourLevel(6,104.0436);
qMap_Ag_C0_V0.SetContourLevel(7,121.3842);
qMap_Ag_C0_V0.SetContourLevel(8,138.7247);
qMap_Ag_C0_V0.SetContourLevel(9,156.0653);
qMap_Ag_C0_V0.SetContourLevel(10,173.4059);
qMap_Ag_C0_V0.SetContourLevel(11,190.7465);
qMap_Ag_C0_V0.SetContourLevel(12,208.0871);
qMap_Ag_C0_V0.SetContourLevel(13,225.4277);
qMap_Ag_C0_V0.SetContourLevel(14,242.7683);
qMap_Ag_C0_V0.SetContourLevel(15,260.1089);
qMap_Ag_C0_V0.SetContourLevel(16,277.4495);
qMap_Ag_C0_V0.SetContourLevel(17,294.7901);
qMap_Ag_C0_V0.SetContourLevel(18,312.1307);
qMap_Ag_C0_V0.SetContourLevel(19,329.4713);


ci = root.TColor.GetColor("#000099");
qMap_Ag_C0_V0.SetLineColor(ci);
qMap_Ag_C0_V0.GetXaxis().SetTitle("col");
qMap_Ag_C0_V0.GetXaxis().SetRange(15,30);
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
