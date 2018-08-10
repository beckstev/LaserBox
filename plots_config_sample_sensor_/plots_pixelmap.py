import ROOT as root
import sys
import time
import imp
############ INPUT FILE

sys.path.insert(0, './data/' + 'after_trim_pixelmap' + '/')
import pyData

file_names_list = [ 'after_trim_pixelmap', 'before_trim_pixelmap', 'pixel_alive', 'scurve_noise', 'scurve_threshold']

for file_name in file_names_list:
        sys.path.insert(0, './data/' + file_name + '/')
        pyData = imp.reload(pyData)
        from pyData import *

        root.gStyle.SetOptStat(0)
        root.gStyle.SetOptTitle(0)
        root.gStyle.SetPalette(1)

        if file_name == 'scurve_noise':
            root.gStyle.SetPadRightMargin(0.13)

        elif file_name == 'before_trim_pixelmap':
            root.gStyle.SetPadRightMargin(0.13)

        else:
            root.gStyle.SetPadRightMargin(0.11)


        #Canvas_1 = root.TCanvas("Canvas_1", "Canvas_1",1281,453,538,321);
        Canvas_1 = root.TCanvas("Canvas_1", "Canvas_1",1281,453,538,538);

        #Canvas_1.SetHighLightColor(2);

        Canvas_1.Range(-6.5,-10,58.5,90);
        Canvas_1.SetFillColor(0);
        Canvas_1.SetBorderMode(0);
        Canvas_1.SetBorderSize(2);
        Canvas_1.SetFrameBorderMode(0);






        pixelmap.GetXaxis().SetTitle("Spalten");
        pixelmap.GetXaxis().SetLabelSize(0.05);
        pixelmap.GetXaxis().SetTitleSize(0.05);
        pixelmap.GetXaxis().SetTitleOffset(0.9);

        pixelmap.GetYaxis().SetTitle("Zeilen");
        pixelmap.GetYaxis().SetLabelSize(0.05);
        pixelmap.GetYaxis().SetTitleSize(0.05);
        pixelmap.GetYaxis().SetTitleOffset(0.98);

        pixelmap.GetZaxis().SetLabelOffset(0.01)
        pixelmap.GetZaxis().SetLabelSize(0.045)

        pixelmap.SetTitle(file_name)
        pixelmap.Draw("colz")


    #qMap_Ag_C0_V0.Draw("colz text")
    #Canvas_1_n40.SaveAs(f'./measurment_hist_plots/{name_of_folder}_measurment_plot.pdf')

        Canvas_1.SaveAs('./plots/' + file_name + '_pixelmap.pdf')
        Canvas_1.Clear()
#qMap_Ag_C0_V0.GetXaxis().SetRange(18,26);
#qMap_Ag_C0_V0.GetYaxis().SetRange(61,72);
#qMap_Ag_C0_V0.GetXaxis().SetTitle("Spalten");
#qMap_Ag_C0_V0.GetXaxis().SetTitleOffset(0.75);
#qMap_Ag_C0_V0.GetYaxis().SetTitle("Zeilen");
#qMap_Ag_C0_V0.GetYaxis().SetTitleOffset(0.75);
#
#qMap_Ag_C0_V0.GetXaxis().SetTitleSize(0.06);
#qMap_Ag_C0_V0.GetXaxis().SetLabelSize(0.06);
#qMap_Ag_C0_V0.GetYaxis().SetTitleSize(0.06);
#qMap_Ag_C0_V0.GetYaxis().SetLabelSize(0.06);
#
#qMap_Ag_C0_V0.SetMarkerSize(1.7)
