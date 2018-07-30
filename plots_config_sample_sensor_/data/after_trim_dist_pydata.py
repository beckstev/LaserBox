import ROOT as root

dist = root.TH1D("dist","dist",256,0,256);
dist.SetBinContent(1,3);
dist.SetBinContent(29,3);
dist.SetBinContent(31,3);
dist.SetBinContent(32,8);
dist.SetBinContent(33,46);
dist.SetBinContent(34,535);
dist.SetBinContent(35,1566);
dist.SetBinContent(36,1430);
dist.SetBinContent(37,496);
dist.SetBinContent(38,65);
dist.SetBinContent(39,2);
dist.SetBinContent(40,2);
dist.SetBinContent(42,1);
dist.SetEntries(4160);
dist.SetStats(0);

ci = root.TColor.GetColor("#000099");
dist.SetLineColor(ci);
dist.GetXaxis().SetTitle("Aktivierungsschwellwert / vcal");
dist.GetXaxis().SetRange(24,47);
dist.GetXaxis().SetLabelFont(42);
dist.GetXaxis().SetLabelSize(0.045);
dist.GetXaxis().SetTitleSize(0.055);
dist.GetXaxis().SetTitleOffset(0.9);
dist.GetXaxis().SetTitleFont(42);
dist.GetYaxis().SetTitle("Anzahl Pixel");
dist.GetYaxis().SetLabelFont(42);
dist.GetYaxis().SetLabelSize(0.045);
dist.GetYaxis().SetTitleSize(0.055);
dist.GetYaxis().SetTitleOffset(1.4);
dist.GetYaxis().SetTitleFont(42);
dist.GetZaxis().SetLabelFont(42);
dist.GetZaxis().SetLabelSize(0.035);
dist.GetZaxis().SetTitleSize(0.035);
dist.GetZaxis().SetTitleFont(42);
