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
qMap_Ag_C0_V0.SetBinEntries(2290,173);
qMap_Ag_C0_V0.SetBinEntries(2291,1032);
qMap_Ag_C0_V0.SetBinEntries(2292,2970);
qMap_Ag_C0_V0.SetBinEntries(2343,346);
qMap_Ag_C0_V0.SetBinEntries(2344,13862);
qMap_Ag_C0_V0.SetBinEntries(2345,14000);
qMap_Ag_C0_V0.SetBinEntries(2346,13238);
qMap_Ag_C0_V0.SetBinEntries(2347,1379);
qMap_Ag_C0_V0.SetBinEntries(2396,204);
qMap_Ag_C0_V0.SetBinEntries(2397,13960);
qMap_Ag_C0_V0.SetBinEntries(2398,13857);
qMap_Ag_C0_V0.SetBinEntries(2399,13765);
qMap_Ag_C0_V0.SetBinEntries(2400,13788);
qMap_Ag_C0_V0.SetBinEntries(2401,13930);
qMap_Ag_C0_V0.SetBinEntries(2450,10929);
qMap_Ag_C0_V0.SetBinEntries(2451,13612);
qMap_Ag_C0_V0.SetBinEntries(2452,13795);
qMap_Ag_C0_V0.SetBinEntries(2453,13751);
qMap_Ag_C0_V0.SetBinEntries(2454,13741);
qMap_Ag_C0_V0.SetBinEntries(2455,13806);
qMap_Ag_C0_V0.SetBinEntries(2504,14236);
qMap_Ag_C0_V0.SetBinEntries(2505,13830);
qMap_Ag_C0_V0.SetBinEntries(2506,14213);
qMap_Ag_C0_V0.SetBinEntries(2507,13884);
qMap_Ag_C0_V0.SetBinEntries(2508,13836);
qMap_Ag_C0_V0.SetBinEntries(2509,13778);
qMap_Ag_C0_V0.SetBinEntries(2558,13993);
qMap_Ag_C0_V0.SetBinEntries(2559,13763);
qMap_Ag_C0_V0.SetBinEntries(2560,14394);
qMap_Ag_C0_V0.SetBinEntries(2561,27417);
qMap_Ag_C0_V0.SetBinEntries(2562,15655);
qMap_Ag_C0_V0.SetBinEntries(2563,13788);
qMap_Ag_C0_V0.SetBinEntries(2612,14078);
qMap_Ag_C0_V0.SetBinEntries(2613,13739);
qMap_Ag_C0_V0.SetBinEntries(2614,16119);
qMap_Ag_C0_V0.SetBinEntries(2615,14810);
qMap_Ag_C0_V0.SetBinEntries(2616,15274);
qMap_Ag_C0_V0.SetBinEntries(2617,13807);
qMap_Ag_C0_V0.SetBinEntries(2666,14175);
qMap_Ag_C0_V0.SetBinEntries(2667,13655);
qMap_Ag_C0_V0.SetBinEntries(2668,13983);
qMap_Ag_C0_V0.SetBinEntries(2669,13862);
qMap_Ag_C0_V0.SetBinEntries(2670,13869);
qMap_Ag_C0_V0.SetBinEntries(2671,13832);
qMap_Ag_C0_V0.SetBinEntries(2720,129);
qMap_Ag_C0_V0.SetBinEntries(2721,13890);
qMap_Ag_C0_V0.SetBinEntries(2722,13737);
qMap_Ag_C0_V0.SetBinEntries(2723,13746);
qMap_Ag_C0_V0.SetBinEntries(2724,13835);
qMap_Ag_C0_V0.SetBinEntries(2725,13766);
qMap_Ag_C0_V0.SetBinEntries(2775,71);
qMap_Ag_C0_V0.SetBinEntries(2776,1727);
qMap_Ag_C0_V0.SetBinEntries(2777,13225);
qMap_Ag_C0_V0.SetBinEntries(2778,1348);
qMap_Ag_C0_V0.SetBinEntries(2779,36);
qMap_Ag_C0_V0.SetBinContent(2290,10835);
qMap_Ag_C0_V0.SetBinContent(2291,128605);
qMap_Ag_C0_V0.SetBinContent(2292,367735);
qMap_Ag_C0_V0.SetBinContent(2343,20853);
qMap_Ag_C0_V0.SetBinContent(2344,995672);
qMap_Ag_C0_V0.SetBinContent(2345,1116976);
qMap_Ag_C0_V0.SetBinContent(2346,878119);
qMap_Ag_C0_V0.SetBinContent(2347,91624);
qMap_Ag_C0_V0.SetBinContent(2396,14547);
qMap_Ag_C0_V0.SetBinContent(2397,856179);
qMap_Ag_C0_V0.SetBinContent(2398,1225048);
qMap_Ag_C0_V0.SetBinContent(2399,1477362);
qMap_Ag_C0_V0.SetBinContent(2400,1208875);
qMap_Ag_C0_V0.SetBinContent(2401,1131106);
qMap_Ag_C0_V0.SetBinContent(2450,915247);
qMap_Ag_C0_V0.SetBinContent(2451,1367700);
qMap_Ag_C0_V0.SetBinContent(2452,1553247);
qMap_Ag_C0_V0.SetBinContent(2453,1734556);
qMap_Ag_C0_V0.SetBinContent(2454,1442354);
qMap_Ag_C0_V0.SetBinContent(2455,1579344);
qMap_Ag_C0_V0.SetBinContent(2504,1427999);
qMap_Ag_C0_V0.SetBinContent(2505,1585278);
qMap_Ag_C0_V0.SetBinContent(2506,1813589);
qMap_Ag_C0_V0.SetBinContent(2507,2009598);
qMap_Ag_C0_V0.SetBinContent(2508,1748652);
qMap_Ag_C0_V0.SetBinContent(2509,1711749);
qMap_Ag_C0_V0.SetBinContent(2558,1583539);
qMap_Ag_C0_V0.SetBinContent(2559,1745567);
qMap_Ag_C0_V0.SetBinContent(2560,1792309);
qMap_Ag_C0_V0.SetBinContent(2561,3689934);
qMap_Ag_C0_V0.SetBinContent(2562,5209131);
qMap_Ag_C0_V0.SetBinContent(2563,1728179);
qMap_Ag_C0_V0.SetBinContent(2612,1498127);
qMap_Ag_C0_V0.SetBinContent(2613,1662347);
qMap_Ag_C0_V0.SetBinContent(2614,2048170);
qMap_Ag_C0_V0.SetBinContent(2615,2142687);
qMap_Ag_C0_V0.SetBinContent(2616,2112558);
qMap_Ag_C0_V0.SetBinContent(2617,1747006);
qMap_Ag_C0_V0.SetBinContent(2666,1110810);
qMap_Ag_C0_V0.SetBinContent(2667,1488366);
qMap_Ag_C0_V0.SetBinContent(2668,1805532);
qMap_Ag_C0_V0.SetBinContent(2669,1785809);
qMap_Ag_C0_V0.SetBinContent(2670,1760934);
qMap_Ag_C0_V0.SetBinContent(2671,1616687);
qMap_Ag_C0_V0.SetBinContent(2720,7736);
qMap_Ag_C0_V0.SetBinContent(2721,1266278);
qMap_Ag_C0_V0.SetBinContent(2722,1645078);
qMap_Ag_C0_V0.SetBinContent(2723,1623869);
qMap_Ag_C0_V0.SetBinContent(2724,1524571);
qMap_Ag_C0_V0.SetBinContent(2725,1515531);
qMap_Ag_C0_V0.SetBinContent(2775,4177);
qMap_Ag_C0_V0.SetBinContent(2776,163922);
qMap_Ag_C0_V0.SetBinContent(2777,1251858);
qMap_Ag_C0_V0.SetBinContent(2778,84748);
qMap_Ag_C0_V0.SetBinContent(2779,2336);
qMap_Ag_C0_V0.SetBinError(2290,853.668);
qMap_Ag_C0_V0.SetBinError(2291,65563.77);
qMap_Ag_C0_V0.SetBinError(2292,113549);
qMap_Ag_C0_V0.SetBinError(2343,1174.197);
qMap_Ag_C0_V0.SetBinError(2344,8598.805);
qMap_Ag_C0_V0.SetBinError(2345,9624.478);
qMap_Ag_C0_V0.SetBinError(2346,7759.646);
qMap_Ag_C0_V0.SetBinError(2347,2558.618);
qMap_Ag_C0_V0.SetBinError(2396,1044.225);
qMap_Ag_C0_V0.SetBinError(2397,7539.7);
qMap_Ag_C0_V0.SetBinError(2398,10477.01);
qMap_Ag_C0_V0.SetBinError(2399,12835.74);
qMap_Ag_C0_V0.SetBinError(2400,10369.58);
qMap_Ag_C0_V0.SetBinError(2401,9745.22);
qMap_Ag_C0_V0.SetBinError(2450,9032.874);
qMap_Ag_C0_V0.SetBinError(2451,11902.09);
qMap_Ag_C0_V0.SetBinError(2452,13322.63);
qMap_Ag_C0_V0.SetBinError(2453,14899.37);
qMap_Ag_C0_V0.SetBinError(2454,12324.24);
qMap_Ag_C0_V0.SetBinError(2455,13527.78);
qMap_Ag_C0_V0.SetBinError(2504,12099.52);
qMap_Ag_C0_V0.SetBinError(2505,13609.03);
qMap_Ag_C0_V0.SetBinError(2506,15392.52);
qMap_Ag_C0_V0.SetBinError(2507,17130.98);
qMap_Ag_C0_V0.SetBinError(2508,14936.95);
qMap_Ag_C0_V0.SetBinError(2509,14637.61);
qMap_Ag_C0_V0.SetBinError(2558,13506.55);
qMap_Ag_C0_V0.SetBinError(2559,15003.53);
qMap_Ag_C0_V0.SetBinError(2560,15181.85);
qMap_Ag_C0_V0.SetBinError(2561,218349);
qMap_Ag_C0_V0.SetBinError(2562,454280.9);
qMap_Ag_C0_V0.SetBinError(2563,14760.69);
qMap_Ag_C0_V0.SetBinError(2612,12777.36);
qMap_Ag_C0_V0.SetBinError(2613,14280.77);
qMap_Ag_C0_V0.SetBinError(2614,16829.72);
qMap_Ag_C0_V0.SetBinError(2615,17834.02);
qMap_Ag_C0_V0.SetBinError(2616,17506.28);
qMap_Ag_C0_V0.SetBinError(2617,14916.59);
qMap_Ag_C0_V0.SetBinError(2666,9434.379);
qMap_Ag_C0_V0.SetBinError(2667,12819.96);
qMap_Ag_C0_V0.SetBinError(2668,15380.58);
qMap_Ag_C0_V0.SetBinError(2669,15230.59);
qMap_Ag_C0_V0.SetBinError(2670,15054.73);
qMap_Ag_C0_V0.SetBinError(2671,13796.73);
qMap_Ag_C0_V0.SetBinError(2720,697.7879);
qMap_Ag_C0_V0.SetBinError(2721,10903.75);
qMap_Ag_C0_V0.SetBinError(2722,14116.36);
qMap_Ag_C0_V0.SetBinError(2723,13937.67);
qMap_Ag_C0_V0.SetBinError(2724,13037.23);
qMap_Ag_C0_V0.SetBinError(2725,12970.37);
qMap_Ag_C0_V0.SetBinError(2775,510.2421);
qMap_Ag_C0_V0.SetBinError(2776,65569.29);
qMap_Ag_C0_V0.SetBinError(2777,173512.6);
qMap_Ag_C0_V0.SetBinError(2778,2372.259);
qMap_Ag_C0_V0.SetBinError(2779,398.2813);
qMap_Ag_C0_V0.SetMinimum(0);
qMap_Ag_C0_V0.SetEntries(635638);
qMap_Ag_C0_V0.SetStats(0);
qMap_Ag_C0_V0.SetContour(20);
qMap_Ag_C0_V0.SetContourLevel(0,0);
qMap_Ag_C0_V0.SetContourLevel(1,16.63728);
qMap_Ag_C0_V0.SetContourLevel(2,33.27455);
qMap_Ag_C0_V0.SetContourLevel(3,49.91183);
qMap_Ag_C0_V0.SetContourLevel(4,66.5491);
qMap_Ag_C0_V0.SetContourLevel(5,83.18638);
qMap_Ag_C0_V0.SetContourLevel(6,99.82365);
qMap_Ag_C0_V0.SetContourLevel(7,116.4609);
qMap_Ag_C0_V0.SetContourLevel(8,133.0982);
qMap_Ag_C0_V0.SetContourLevel(9,149.7355);
qMap_Ag_C0_V0.SetContourLevel(10,166.3728);
qMap_Ag_C0_V0.SetContourLevel(11,183.01);
qMap_Ag_C0_V0.SetContourLevel(12,199.6473);
qMap_Ag_C0_V0.SetContourLevel(13,216.2846);
qMap_Ag_C0_V0.SetContourLevel(14,232.9219);
qMap_Ag_C0_V0.SetContourLevel(15,249.5591);
qMap_Ag_C0_V0.SetContourLevel(16,266.1964);
qMap_Ag_C0_V0.SetContourLevel(17,282.8337);
qMap_Ag_C0_V0.SetContourLevel(18,299.471);
qMap_Ag_C0_V0.SetContourLevel(19,316.1082);

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
qMap_Ag_C0_V0.GetYaxis().SetRange(31,60);
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
