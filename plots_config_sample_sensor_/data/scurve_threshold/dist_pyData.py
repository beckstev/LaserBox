import ROOT as root

dist = root.TH1D("dist","dist",256,0,256);
dist.SetBinContent(0,2);
dist.SetBinContent(1,3);
dist.SetBinContent(29,2);
dist.SetBinContent(30,1);
dist.SetBinContent(31,4);
dist.SetBinContent(32,6);
dist.SetBinContent(33,10);
dist.SetBinContent(34,247);
dist.SetBinContent(35,1584);
dist.SetBinContent(36,1682);
dist.SetBinContent(37,584);
dist.SetBinContent(38,33);
dist.SetBinContent(39,1);
dist.SetBinContent(40,1);
dist.SetEntries(4160);
dist.SetStats(0);

ci = root.TColor.GetColor("#000099");
dist.SetLineColor(ci);
dist.GetXaxis().SetLabelFont(42);
dist.GetXaxis().SetLabelSize(0.035);
dist.GetXaxis().SetTitleSize(0.035);
dist.GetXaxis().SetTitleFont(42);
dist.GetYaxis().SetLabelFont(42);
dist.GetYaxis().SetLabelSize(0.035);
dist.GetYaxis().SetTitleSize(0.035);
dist.GetYaxis().SetTitleFont(42);
dist.GetZaxis().SetLabelFont(42);
dist.GetZaxis().SetLabelSize(0.035);
dist.GetZaxis().SetTitleSize(0.035);
dist.GetZaxis().SetTitleFont(42);
