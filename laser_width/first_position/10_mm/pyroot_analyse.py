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
qMap_Ag_C0_V0.SetBinEntries(2452,17860);
qMap_Ag_C0_V0.SetBinEntries(2453,4739);
qMap_Ag_C0_V0.SetBinEntries(2506,118640);
qMap_Ag_C0_V0.SetBinEntries(2507,80862);
qMap_Ag_C0_V0.SetBinEntries(2560,127145);
qMap_Ag_C0_V0.SetBinEntries(2561,89550);
qMap_Ag_C0_V0.SetBinEntries(2614,40);
qMap_Ag_C0_V0.SetBinContent(2452,2640159);
qMap_Ag_C0_V0.SetBinContent(2453,250351);
qMap_Ag_C0_V0.SetBinContent(2506,1.172519e+08);
qMap_Ag_C0_V0.SetBinContent(2507,2.13815e+07);
qMap_Ag_C0_V0.SetBinContent(2560,1.664191e+08);
qMap_Ag_C0_V0.SetBinContent(2561,2.109096e+07);
qMap_Ag_C0_V0.SetBinContent(2614,1605);
qMap_Ag_C0_V0.SetBinError(2452,20969.95);
qMap_Ag_C0_V0.SetBinError(2453,3735.723);
qMap_Ag_C0_V0.SetBinError(2506,2418194);
qMap_Ag_C0_V0.SetBinError(2507,804356.6);
qMap_Ag_C0_V0.SetBinError(2560,3021759);
qMap_Ag_C0_V0.SetBinError(2561,601072.5);
qMap_Ag_C0_V0.SetBinError(2614,259.1428);
qMap_Ag_C0_V0.SetMinimum(0);
qMap_Ag_C0_V0.SetEntries(438836);
qMap_Ag_C0_V0.SetStats(0);
qMap_Ag_C0_V0.SetContour(20);
qMap_Ag_C0_V0.SetContourLevel(0,0);
qMap_Ag_C0_V0.SetContourLevel(1,65.4446);
qMap_Ag_C0_V0.SetContourLevel(2,130.8892);
qMap_Ag_C0_V0.SetContourLevel(3,196.3338);
qMap_Ag_C0_V0.SetContourLevel(4,261.7784);
qMap_Ag_C0_V0.SetContourLevel(5,327.223);
qMap_Ag_C0_V0.SetContourLevel(6,392.6676);
qMap_Ag_C0_V0.SetContourLevel(7,458.1122);
qMap_Ag_C0_V0.SetContourLevel(8,523.5568);
qMap_Ag_C0_V0.SetContourLevel(9,589.0014);
qMap_Ag_C0_V0.SetContourLevel(10,654.446);
qMap_Ag_C0_V0.SetContourLevel(11,719.8906);
qMap_Ag_C0_V0.SetContourLevel(12,785.3352);
qMap_Ag_C0_V0.SetContourLevel(13,850.7798);
qMap_Ag_C0_V0.SetContourLevel(14,916.2244);
qMap_Ag_C0_V0.SetContourLevel(15,981.669);
qMap_Ag_C0_V0.SetContourLevel(16,1047.114);
qMap_Ag_C0_V0.SetContourLevel(17,1112.558);
qMap_Ag_C0_V0.SetContourLevel(18,1178.003);
qMap_Ag_C0_V0.SetContourLevel(19,1243.447);

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
