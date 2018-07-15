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
qMap_Ag_C0_V0.SetBinEntries(551,1);
qMap_Ag_C0_V0.SetBinEntries(2290,296);
qMap_Ag_C0_V0.SetBinEntries(2291,11516);
qMap_Ag_C0_V0.SetBinEntries(2292,13257);
qMap_Ag_C0_V0.SetBinEntries(2344,14058);
qMap_Ag_C0_V0.SetBinEntries(2345,14441);
qMap_Ag_C0_V0.SetBinEntries(2346,14136);
qMap_Ag_C0_V0.SetBinEntries(2347,7751);
qMap_Ag_C0_V0.SetBinEntries(2397,14308);
qMap_Ag_C0_V0.SetBinEntries(2398,14543);
qMap_Ag_C0_V0.SetBinEntries(2399,14557);
qMap_Ag_C0_V0.SetBinEntries(2400,14535);
qMap_Ag_C0_V0.SetBinEntries(2401,14418);
qMap_Ag_C0_V0.SetBinEntries(2451,14703);
qMap_Ag_C0_V0.SetBinEntries(2452,20843);
qMap_Ag_C0_V0.SetBinEntries(2453,16003);
qMap_Ag_C0_V0.SetBinEntries(2454,14867);
qMap_Ag_C0_V0.SetBinEntries(2455,14496);
qMap_Ag_C0_V0.SetBinEntries(2504,3395);
qMap_Ag_C0_V0.SetBinEntries(2505,18049);
qMap_Ag_C0_V0.SetBinEntries(2506,28473);
qMap_Ag_C0_V0.SetBinEntries(2507,28076);
qMap_Ag_C0_V0.SetBinEntries(2508,18557);
qMap_Ag_C0_V0.SetBinEntries(2509,14718);
qMap_Ag_C0_V0.SetBinEntries(2558,6221);
qMap_Ag_C0_V0.SetBinEntries(2559,17322);
qMap_Ag_C0_V0.SetBinEntries(2560,30343);
qMap_Ag_C0_V0.SetBinEntries(2561,48207);
qMap_Ag_C0_V0.SetBinEntries(2562,30684);
qMap_Ag_C0_V0.SetBinEntries(2563,14600);
qMap_Ag_C0_V0.SetBinEntries(2613,20328);
qMap_Ag_C0_V0.SetBinEntries(2614,35133);
qMap_Ag_C0_V0.SetBinEntries(2615,32859);
qMap_Ag_C0_V0.SetBinEntries(2616,31753);
qMap_Ag_C0_V0.SetBinEntries(2617,14638);
qMap_Ag_C0_V0.SetBinEntries(2667,14543);
qMap_Ag_C0_V0.SetBinEntries(2668,25639);
qMap_Ag_C0_V0.SetBinEntries(2669,16710);
qMap_Ag_C0_V0.SetBinEntries(2670,15717);
qMap_Ag_C0_V0.SetBinEntries(2671,14563);
qMap_Ag_C0_V0.SetBinEntries(2721,5050);
qMap_Ag_C0_V0.SetBinEntries(2722,19145);
qMap_Ag_C0_V0.SetBinEntries(2723,18796);
qMap_Ag_C0_V0.SetBinEntries(2724,14833);
qMap_Ag_C0_V0.SetBinEntries(2725,14465);
qMap_Ag_C0_V0.SetBinEntries(2776,12076);
qMap_Ag_C0_V0.SetBinEntries(2777,14189);
qMap_Ag_C0_V0.SetBinEntries(2778,12515);
qMap_Ag_C0_V0.SetBinEntries(2779,2388);
qMap_Ag_C0_V0.SetBinContent(551,65);
qMap_Ag_C0_V0.SetBinContent(2290,21889);
qMap_Ag_C0_V0.SetBinContent(2291,1106098);
qMap_Ag_C0_V0.SetBinContent(2292,997927);
qMap_Ag_C0_V0.SetBinContent(2344,1184971);
qMap_Ag_C0_V0.SetBinContent(2345,1415761);
qMap_Ag_C0_V0.SetBinContent(2346,1201895);
qMap_Ag_C0_V0.SetBinContent(2347,619179);
qMap_Ag_C0_V0.SetBinContent(2397,908237);
qMap_Ag_C0_V0.SetBinContent(2398,1568165);
qMap_Ag_C0_V0.SetBinContent(2399,1766743);
qMap_Ag_C0_V0.SetBinContent(2400,1487965);
qMap_Ag_C0_V0.SetBinContent(2401,1358005);
qMap_Ag_C0_V0.SetBinContent(2451,1834930);
qMap_Ag_C0_V0.SetBinContent(2452,2900970);
qMap_Ag_C0_V0.SetBinContent(2453,2196505);
qMap_Ag_C0_V0.SetBinContent(2454,1748498);
qMap_Ag_C0_V0.SetBinContent(2455,1728056);
qMap_Ag_C0_V0.SetBinContent(2504,323537);
qMap_Ag_C0_V0.SetBinContent(2505,3269289);
qMap_Ag_C0_V0.SetBinContent(2506,3238915);
qMap_Ag_C0_V0.SetBinContent(2507,3381789);
qMap_Ag_C0_V0.SetBinContent(2508,2536932);
qMap_Ag_C0_V0.SetBinContent(2509,1879747);
qMap_Ag_C0_V0.SetBinContent(2558,565137);
qMap_Ag_C0_V0.SetBinContent(2559,2184291);
qMap_Ag_C0_V0.SetBinContent(2560,3270171);
qMap_Ag_C0_V0.SetBinContent(2561,5394814);
qMap_Ag_C0_V0.SetBinContent(2562,5497492);
qMap_Ag_C0_V0.SetBinContent(2563,1920073);
qMap_Ag_C0_V0.SetBinContent(2613,2296772);
qMap_Ag_C0_V0.SetBinContent(2614,3697347);
qMap_Ag_C0_V0.SetBinContent(2615,3806954);
qMap_Ag_C0_V0.SetBinContent(2616,3677856);
qMap_Ag_C0_V0.SetBinContent(2617,1929287);
qMap_Ag_C0_V0.SetBinContent(2667,1718146);
qMap_Ag_C0_V0.SetBinContent(2668,2806715);
qMap_Ag_C0_V0.SetBinContent(2669,2278746);
qMap_Ag_C0_V0.SetBinContent(2670,2119668);
qMap_Ag_C0_V0.SetBinContent(2671,1717617);
qMap_Ag_C0_V0.SetBinContent(2721,405374);
qMap_Ag_C0_V0.SetBinContent(2722,2305173);
qMap_Ag_C0_V0.SetBinContent(2723,2187765);
qMap_Ag_C0_V0.SetBinContent(2724,1713964);
qMap_Ag_C0_V0.SetBinContent(2725,1682890);
qMap_Ag_C0_V0.SetBinContent(2776,868882);
qMap_Ag_C0_V0.SetBinContent(2777,1095437);
qMap_Ag_C0_V0.SetBinContent(2778,959645);
qMap_Ag_C0_V0.SetBinContent(2779,185761);
qMap_Ag_C0_V0.SetBinError(551,65);
qMap_Ag_C0_V0.SetBinError(2290,1285.797);
qMap_Ag_C0_V0.SetBinError(2291,146722);
qMap_Ag_C0_V0.SetBinError(2292,92980.8);
qMap_Ag_C0_V0.SetBinError(2344,10185.8);
qMap_Ag_C0_V0.SetBinError(2345,11908.22);
qMap_Ag_C0_V0.SetBinError(2346,10214.62);
qMap_Ag_C0_V0.SetBinError(2347,7205.312);
qMap_Ag_C0_V0.SetBinError(2397,7940.398);
qMap_Ag_C0_V0.SetBinError(2398,13062.24);
qMap_Ag_C0_V0.SetBinError(2399,14790.43);
qMap_Ag_C0_V0.SetBinError(2400,12398.42);
qMap_Ag_C0_V0.SetBinError(2401,11414.15);
qMap_Ag_C0_V0.SetBinError(2451,93753.69);
qMap_Ag_C0_V0.SetBinError(2452,197295.4);
qMap_Ag_C0_V0.SetBinError(2453,17739.12);
qMap_Ag_C0_V0.SetBinError(2454,14444.42);
qMap_Ag_C0_V0.SetBinError(2455,14420.48);
qMap_Ag_C0_V0.SetBinError(2504,5652.305);
qMap_Ag_C0_V0.SetBinError(2505,278523.3);
qMap_Ag_C0_V0.SetBinError(2506,20437.44);
qMap_Ag_C0_V0.SetBinError(2507,22237.77);
qMap_Ag_C0_V0.SetBinError(2508,19133.75);
qMap_Ag_C0_V0.SetBinError(2509,15565.04);
qMap_Ag_C0_V0.SetBinError(2558,7279.413);
qMap_Ag_C0_V0.SetBinError(2559,17349.12);
qMap_Ag_C0_V0.SetBinError(2560,20327.51);
qMap_Ag_C0_V0.SetBinError(2561,148920.3);
qMap_Ag_C0_V0.SetBinError(2562,365462.2);
qMap_Ag_C0_V0.SetBinError(2563,15944.27);
qMap_Ag_C0_V0.SetBinError(2613,17338);
qMap_Ag_C0_V0.SetBinError(2614,21894.6);
qMap_Ag_C0_V0.SetBinError(2615,22857.41);
qMap_Ag_C0_V0.SetBinError(2616,22189);
qMap_Ag_C0_V0.SetBinError(2617,16000.67);
qMap_Ag_C0_V0.SetBinError(2667,14319.81);
qMap_Ag_C0_V0.SetBinError(2668,19036.01);
qMap_Ag_C0_V0.SetBinError(2669,18078.16);
qMap_Ag_C0_V0.SetBinError(2670,17169.86);
qMap_Ag_C0_V0.SetBinError(2671,14282.56);
qMap_Ag_C0_V0.SetBinError(2721,65723.52);
qMap_Ag_C0_V0.SetBinError(2722,94135.73);
qMap_Ag_C0_V0.SetBinError(2723,16524.23);
qMap_Ag_C0_V0.SetBinError(2724,14182.35);
qMap_Ag_C0_V0.SetBinError(2725,14040.21);
qMap_Ag_C0_V0.SetBinError(2776,65975.17);
qMap_Ag_C0_V0.SetBinError(2777,9363.315);
qMap_Ag_C0_V0.SetBinError(2778,8718.091);
qMap_Ag_C0_V0.SetBinError(2779,3877.215);
qMap_Ag_C0_V0.SetMinimum(0);
qMap_Ag_C0_V0.SetEntries(822714);
qMap_Ag_C0_V0.SetStats(0);
qMap_Ag_C0_V0.SetContour(20);
qMap_Ag_C0_V0.SetContourLevel(0,0);
qMap_Ag_C0_V0.SetContourLevel(1,9.056704);
qMap_Ag_C0_V0.SetContourLevel(2,18.11341);
qMap_Ag_C0_V0.SetContourLevel(3,27.17011);
qMap_Ag_C0_V0.SetContourLevel(4,36.22682);
qMap_Ag_C0_V0.SetContourLevel(5,45.28352);
qMap_Ag_C0_V0.SetContourLevel(6,54.34022);
qMap_Ag_C0_V0.SetContourLevel(7,63.39693);
qMap_Ag_C0_V0.SetContourLevel(8,72.45363);
qMap_Ag_C0_V0.SetContourLevel(9,81.51034);
qMap_Ag_C0_V0.SetContourLevel(10,90.56704);
qMap_Ag_C0_V0.SetContourLevel(11,99.62374);
qMap_Ag_C0_V0.SetContourLevel(12,108.6804);
qMap_Ag_C0_V0.SetContourLevel(13,117.7372);
qMap_Ag_C0_V0.SetContourLevel(14,126.7939);
qMap_Ag_C0_V0.SetContourLevel(15,135.8506);
qMap_Ag_C0_V0.SetContourLevel(16,144.9073);
qMap_Ag_C0_V0.SetContourLevel(17,153.964);
qMap_Ag_C0_V0.SetContourLevel(18,163.0207);
qMap_Ag_C0_V0.SetContourLevel(19,172.0774);


ci = root.TColor.GetColor("#000099");
qMap_Ag_C0_V0.SetLineColor(ci);
qMap_Ag_C0_V0.GetXaxis().SetTitle("col");
qMap_Ag_C0_V0.GetXaxis().SetRange(16,32);
qMap_Ag_C0_V0.GetXaxis().SetNdivisions(508);
qMap_Ag_C0_V0.GetXaxis().SetLabelFont(42);
qMap_Ag_C0_V0.GetXaxis().SetLabelSize(0.05);
qMap_Ag_C0_V0.GetXaxis().SetTitleSize(0.05);
qMap_Ag_C0_V0.GetXaxis().SetTitleOffset(1.1);
qMap_Ag_C0_V0.GetXaxis().SetTitleFont(42);
qMap_Ag_C0_V0.GetYaxis().SetTitle("row");
qMap_Ag_C0_V0.GetYaxis().SetRange(31,59);
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
