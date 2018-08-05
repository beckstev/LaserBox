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

        root.gStyle.SetOptStat('e');
        root.gStyle.SetOptTitle(0)
        root.gStyle.SetOptFit(11)
        #root.gStyle.SetName('R', 'TEst')



        root.gStyle.SetStatW(0.35);
        root.gStyle.SetStatH(0.2)

        root.gStyle.SetStatW(0.2)
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


        dist.Fit('gaus')
        fit = dist.GetFunction('gaus')
        fit.SetParName(0,'Amplitude')
        fit.SetParName(2,'Sigma')
        fit.SetParName(1,'Mittelwert')

        dist.SetMaximum(1.2* dist.GetMaximum())


        dist.Draw()
        c1.Update()

        ps = c1.GetPrimitive("stats")
        list_stats = ps.GetListOfLines()

        ps.SetName('mystats')

        number_pixels =  dist.GetEntries()
        test = ps.GetLineWith('Entries')
        name = root.TLatex(0,0, f'Pixelanzahl = {int(number_pixels)}')
        name.SetTextFont(42)
        name.SetTextSize(0.038)

        list_stats.AddFirst(name)


        list_stats.Remove(test)

        dist.SetStats(0)
        c1.Modified()

        print('line',)
        print('List',list_stats.Print(),'\n')


        c1.SaveAs('./plots/'+ file_name + '_dist.pdf')
        c1.Clear()
