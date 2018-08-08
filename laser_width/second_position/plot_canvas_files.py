import ROOT as root
import sys

############ INPUT FILE
try:
    name_of_folder = sys.argv[1]

except IndexError:
    print('No Argument given Or other Index out of Range Er')


sys.path.insert(0, './' + name_of_folder + '/')

############################################
root.gStyle.SetLabelSize(.08, "XY");
root.gStyle.SetTitleSize(.08, "XY");
root.gStyle.SetTitleOffset(1, "XY");
root.gStyle.SetPalette(91)

Canvas_1_n40 = root.TCanvas("Canvas_1_n40", "Test",1378,105,538,321);
root.gStyle.SetOptStat();
Canvas_1_n40.SetHighLightColor(2);
Canvas_1_n40.Range(13.25,51.25,30.75,78.75);
Canvas_1_n40.SetFillColor(0);
Canvas_1_n40.SetBorderMode(0);
Canvas_1_n40.SetBorderSize(2);
Canvas_1_n40.SetFrameBorderMode(0);
Canvas_1_n40.SetFrameBorderMode(0);
Canvas_1_n40.SetGrid();

root.gStyle.SetOptTitle(0)

from pyData import *



qMap_Ag_C0_V0.GetXaxis().SetTitle("Spalten");
qMap_Ag_C0_V0.GetXaxis().SetRange(19,26);

qMap_Ag_C0_V0.GetXaxis().SetNdivisions(10)

qMap_Ag_C0_V0.GetYaxis().SetRange(62,72);
qMap_Ag_C0_V0.GetXaxis().SetTitleOffset(0.8);
qMap_Ag_C0_V0.GetYaxis().SetTitle("Zeilen");
qMap_Ag_C0_V0.GetYaxis().SetTitleOffset(0.75);
qMap_Ag_C0_V0.GetYaxis().SetNdivisions(20)

qMap_Ag_C0_V0.GetXaxis().SetTitleSize(0.06);
qMap_Ag_C0_V0.GetXaxis().SetLabelSize(0.06);
qMap_Ag_C0_V0.GetYaxis().SetTitleSize(0.06);
qMap_Ag_C0_V0.GetYaxis().SetLabelSize(0.06);

qMap_Ag_C0_V0.GetYaxis().SetLabelOffset(.018);
qMap_Ag_C0_V0.GetXaxis().SetLabelOffset(.018);


qMap_Ag_C0_V0.GetZaxis().SetLabelSize(0.055)

qMap_Ag_C0_V0.SetMarkerSize(1.7)



qMap_Ag_C0_V0.Draw("colz text")

list_of_boxes = []
color_number = 37
for i in range(18,26):
    b_1 = root.TBox(i,61.5,i+1,62)
    b_2 = root.TBox(i,71,i+1,71.5)
    b_1.SetFillColor(color_number);
    b_2.SetFillColor(color_number);

    list_of_boxes.append(b_1)
    list_of_boxes.append(b_2)


for i in range(62,71):
    b_3 = root.TBox(18,i,19,i+1)
    b_4 = root.TBox(25,i,26,i+1)
    b_3.SetFillColor(color_number);
    b_4.SetFillColor(color_number);
    list_of_boxes.append(b_3)
    list_of_boxes.append(b_4)

for box in list_of_boxes:
    box.Draw('same')
Canvas_1_n40.SaveAs(f'./measurment_hist_plots/{name_of_folder}_measurment_plot.pdf')
