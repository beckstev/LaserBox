import ROOT as root
import sys
import time
import imp
############ INPUT FILE

sys.path.insert(0, './data/' + 'after_trim_pixelmap' + '/')
import dist_pyData

file_names_list = [ 'after_trim_pixelmap', 'scurve_noise', 'scurve_threshold']

for file_name in file_names_list:
        sys.path.insert(0, './data/' + file_name + '/')
        dist_pyData = imp.reload(dist_pyData)
        from dist_pyData import *

        root.gStyle.SetOptStat('RMe');
        root.gStyle.SetOptTitle(0)

        root.gStyle.SetStatW(0.35);
        root.gStyle.SetStatH(0.2)

        c1 = root.TCanvas('c1','c1',640,480)

        if file_name == 'scurve_noise':
            dist.GetXaxis().SetTitle("Rauschen / vcal");
            dist.GetXaxis().SetRange(20,70)

        else:
            dist.GetXaxis().SetTitle("Aktivierungsschwellwert / vcal");
            dist.GetXaxis().SetRange(24,47);

        dist.SetStats(1)

        dist.GetXaxis().SetLabelSize(0.055);
        dist.GetXaxis().SetTitleSize(0.045);
        dist.GetXaxis().SetTitleOffset(1.1);


        dist.GetYaxis().SetTitle("Anzahl Pixel");
        dist.GetYaxis().SetLabelSize(0.045);
        dist.GetYaxis().SetTitleSize(0.045);
        dist.GetYaxis().SetTitleOffset(1.2);

        dist.Draw()

        c1.SaveAs('./plots/'+ file_name + '_dist.pdf')
        c1.Clear()
