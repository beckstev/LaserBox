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
qMap_Ag_C0_V0.SetBinEntries(2345,1);
qMap_Ag_C0_V0.SetBinEntries(2398,14628);
qMap_Ag_C0_V0.SetBinEntries(2399,14480);
qMap_Ag_C0_V0.SetBinEntries(2451,13146);
qMap_Ag_C0_V0.SetBinEntries(2452,56859);
qMap_Ag_C0_V0.SetBinEntries(2453,45921);
qMap_Ag_C0_V0.SetBinEntries(2454,10482);
qMap_Ag_C0_V0.SetBinEntries(2505,14645);
qMap_Ag_C0_V0.SetBinEntries(2506,144387);
qMap_Ag_C0_V0.SetBinEntries(2507,89747);
qMap_Ag_C0_V0.SetBinEntries(2508,14505);
qMap_Ag_C0_V0.SetBinEntries(2559,470);
qMap_Ag_C0_V0.SetBinEntries(2560,90404);
qMap_Ag_C0_V0.SetBinEntries(2561,63400);
qMap_Ag_C0_V0.SetBinEntries(2562,5074);
qMap_Ag_C0_V0.SetBinEntries(2614,14657);
qMap_Ag_C0_V0.SetBinEntries(2615,14285);
qMap_Ag_C0_V0.SetBinContent(2345,89);
qMap_Ag_C0_V0.SetBinContent(2398,1499022);
qMap_Ag_C0_V0.SetBinContent(2399,1279581);
qMap_Ag_C0_V0.SetBinContent(2451,776764);
qMap_Ag_C0_V0.SetBinContent(2452,9492774);
qMap_Ag_C0_V0.SetBinContent(2453,5036156);
qMap_Ag_C0_V0.SetBinContent(2454,916118);
qMap_Ag_C0_V0.SetBinContent(2505,1076333);
qMap_Ag_C0_V0.SetBinContent(2506,5.208083e+07);
qMap_Ag_C0_V0.SetBinContent(2507,4.197776e+07);
qMap_Ag_C0_V0.SetBinContent(2508,1462464);
qMap_Ag_C0_V0.SetBinContent(2559,39063);
qMap_Ag_C0_V0.SetBinContent(2560,1.088624e+07);
qMap_Ag_C0_V0.SetBinContent(2561,9917064);
qMap_Ag_C0_V0.SetBinContent(2562,397610);
qMap_Ag_C0_V0.SetBinContent(2614,1490885);
qMap_Ag_C0_V0.SetBinContent(2615,1202723);
qMap_Ag_C0_V0.SetBinError(2345,89);
qMap_Ag_C0_V0.SetBinError(2398,12484.77);
qMap_Ag_C0_V0.SetBinError(2399,10716.67);
qMap_Ag_C0_V0.SetBinError(2451,6927.153);
qMap_Ag_C0_V0.SetBinError(2452,394722.2);
qMap_Ag_C0_V0.SetBinError(2453,175124.6);
qMap_Ag_C0_V0.SetBinError(2454,9107.791);
qMap_Ag_C0_V0.SetBinError(2505,9074.18);
qMap_Ag_C0_V0.SetBinError(2506,1070245);
qMap_Ag_C0_V0.SetBinError(2507,1269670);
qMap_Ag_C0_V0.SetBinError(2508,12216.89);
qMap_Ag_C0_V0.SetBinError(2559,1829.499);
qMap_Ag_C0_V0.SetBinError(2560,240290);
qMap_Ag_C0_V0.SetBinError(2561,265107.6);
qMap_Ag_C0_V0.SetBinError(2562,5706.877);
qMap_Ag_C0_V0.SetBinError(2614,12370.39);
qMap_Ag_C0_V0.SetBinError(2615,10193.58);
qMap_Ag_C0_V0.SetMinimum(0);
qMap_Ag_C0_V0.SetEntries(607091);
qMap_Ag_C0_V0.SetStats(0);
qMap_Ag_C0_V0.SetContour(20);
qMap_Ag_C0_V0.SetContourLevel(0,0);
qMap_Ag_C0_V0.SetContourLevel(1,23.38672);
qMap_Ag_C0_V0.SetContourLevel(2,46.77344);
qMap_Ag_C0_V0.SetContourLevel(3,70.16016);
qMap_Ag_C0_V0.SetContourLevel(4,93.54688);
qMap_Ag_C0_V0.SetContourLevel(5,116.9336);
qMap_Ag_C0_V0.SetContourLevel(6,140.3203);
qMap_Ag_C0_V0.SetContourLevel(7,163.707);
qMap_Ag_C0_V0.SetContourLevel(8,187.0938);
qMap_Ag_C0_V0.SetContourLevel(9,210.4805);
qMap_Ag_C0_V0.SetContourLevel(10,233.8672);
qMap_Ag_C0_V0.SetContourLevel(11,257.2539);
qMap_Ag_C0_V0.SetContourLevel(12,280.6406);
qMap_Ag_C0_V0.SetContourLevel(13,304.0274);
qMap_Ag_C0_V0.SetContourLevel(14,327.4141);
qMap_Ag_C0_V0.SetContourLevel(15,350.8008);
qMap_Ag_C0_V0.SetContourLevel(16,374.1875);
qMap_Ag_C0_V0.SetContourLevel(17,397.5742);
qMap_Ag_C0_V0.SetContourLevel(18,420.961);
qMap_Ag_C0_V0.SetContourLevel(19,444.3477);


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

root.gStyle.SetOptTitle(0)
root.gStyle.SetOptFit(1)
##################################################### Insert Data above line #############################




############################### Get name of folder #################################

name_of_folder = os.path.basename( os.getcwd() )


############################### Save Data in list #######################################

mean_value_col_list = []
mean_error_col_list = []
x_value = []
x_error = []


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
    x_error.append(0.5)

    for j in range(ymin,ymax): # going thru all rows

        if qMap_Ag_C0_V0.GetBinContent(i,j) != 0:
            content.append( qMap_Ag_C0_V0.GetBinContent(i,j))
            error.append( qMap_Ag_C0_V0.GetBinError(i,j) ) # Is this the real error

        else:
            pass
    print(content)
    print(error)
    content_bin = unp.uarray( content, error)
    mean_content_col = content_bin.sum() # mean value of each bin in the col

    print('\n','Mean Content', mean_content_col,'\n' )
    # Saving values in lists
    mean_value_col_list.append( noms(mean_content_col))
    mean_error_col_list.append( stds(mean_content_col))


########################### Create errorbar plot #####################################

errorbar_plot_col = root.TGraphErrors( len(x_value), array( 'f', x_value), array( 'f', mean_value_col_list), array( 'f', x_error), array( 'f', mean_error_col_list) )

############################## Set axis label of errobar plot ##################################

errorbar_plot_col.GetXaxis().SetTitle("Col")
errorbar_plot_col.GetYaxis().SetTitle("Mean Hit / Vcal")

####################### create Canvas ##########################################

c1 = root.TCanvas("c1", "c1", 1980, 1080)
errorbar_plot_col.Fit('gaus',"", "", 20,25 )
errorbar_plot_col.SetMinimum(0)
errorbar_plot_col.SetMaximum(1200)

errorbar_plot_col.Draw("ap")


name_params = [ "amplitude/[MeanVcal]", "mean/[Col]", "sigma/[Col]"]

############################### Create legend ####################################
gaus_fit_col = errorbar_plot_col.GetFunction('gaus')
#legend = root.TLegend(0.75,0.75,0.98,0.98)
#legend.AddEntry(errorbar_plot_col,"Coloumn mean hit value","lep")
#legend.AddEntry( gaus_fit_col,"Gaussian Fit","l")
#legend.Draw()

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
#legend = root.TLegend(0.75,0.75,0.98,0.98)
#legend.AddEntry(errorbar_plot_rows,"Mean Mean Vcal of each row","lep")
#legend.AddEntry( gaus_fit_row,"Gaussian Fit","l")
#legend.Draw()

########################################### saveplot and fit params ########################################
with open( f'../fit_params/{name_of_folder}_fit_parameters_row_yaxis.txt', 'w') as file:
    for i in range(0,3):
        file.write( name_params[i] + ' ' + str( gaus_fit_row.GetParameter(i) ) + ' ' + str(gaus_fit_row.GetParError(i)) + '\n')

with open( f'../sigma_row_yaxis.txt', 'a') as file:
        file.write( name_params[i] +'_' + name_of_folder + ' ' + str( gaus_fit_row.GetParameter(2) ) + ' ' + str(gaus_fit_row.GetParError(2)) + '\n')


c2.SaveAs(f'../plots/{name_of_folder}_erorbar_plot_row.pdf')
