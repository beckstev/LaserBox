import ROOT as root

qMap_Ag_C0_V0 = root.TProfile2D("qMap_Ag_C0_V0","qMap_Ag_C0 (V0)",52,0,52,80,0,80,0,0);
qMap_Ag_C0_V0->SetBinEntries(3424,30132);
qMap_Ag_C0_V0->SetBinEntries(3425,29845);
qMap_Ag_C0_V0->SetBinEntries(3426,14076);
qMap_Ag_C0_V0->SetBinEntries(3477,14281);
qMap_Ag_C0_V0->SetBinEntries(3478,57223);
qMap_Ag_C0_V0->SetBinEntries(3479,53183);
qMap_Ag_C0_V0->SetBinEntries(3480,16128);
qMap_Ag_C0_V0->SetBinEntries(3531,15063);
qMap_Ag_C0_V0->SetBinEntries(3532,74590);
qMap_Ag_C0_V0->SetBinEntries(3533,70013);
qMap_Ag_C0_V0->SetBinEntries(3534,19970);
qMap_Ag_C0_V0->SetBinEntries(3585,8);
qMap_Ag_C0_V0->SetBinEntries(3586,82393);
qMap_Ag_C0_V0->SetBinEntries(3587,68126);
qMap_Ag_C0_V0->SetBinEntries(3588,17181);
qMap_Ag_C0_V0->SetBinEntries(3640,18236);
qMap_Ag_C0_V0->SetBinEntries(3641,33493);
qMap_Ag_C0_V0->SetBinContent(3424,5232424);
qMap_Ag_C0_V0->SetBinContent(3425,5126408);
qMap_Ag_C0_V0->SetBinContent(3426,1115272);
qMap_Ag_C0_V0->SetBinContent(3477,1310056);
qMap_Ag_C0_V0->SetBinContent(3478,1.573836e+07);
qMap_Ag_C0_V0->SetBinContent(3479,8613179);
qMap_Ag_C0_V0->SetBinContent(3480,2449433);
qMap_Ag_C0_V0->SetBinContent(3531,2156392);
qMap_Ag_C0_V0->SetBinContent(3532,1.976301e+07);
qMap_Ag_C0_V0->SetBinContent(3533,1.330032e+07);
qMap_Ag_C0_V0->SetBinContent(3534,3344335);
qMap_Ag_C0_V0->SetBinContent(3585,531);
qMap_Ag_C0_V0->SetBinContent(3586,3.017181e+07);
qMap_Ag_C0_V0->SetBinContent(3587,1.030219e+07);
qMap_Ag_C0_V0->SetBinContent(3588,2777717);
qMap_Ag_C0_V0->SetBinContent(3640,2959006);
qMap_Ag_C0_V0->SetBinContent(3641,7493997);
qMap_Ag_C0_V0->SetBinError(3424,279288.6);
qMap_Ag_C0_V0->SetBinError(3425,271456.1);
qMap_Ag_C0_V0->SetBinError(3426,9635.639);
qMap_Ag_C0_V0->SetBinError(3477,11005.13);
qMap_Ag_C0_V0->SetBinError(3478,742075.7);
qMap_Ag_C0_V0->SetBinError(3479,335978.6);
qMap_Ag_C0_V0->SetBinError(3480,19621.29);
qMap_Ag_C0_V0->SetBinError(3531,17833.07);
qMap_Ag_C0_V0->SetBinError(3532,790396.1);
qMap_Ag_C0_V0->SetBinError(3533,487849.8);
qMap_Ag_C0_V0->SetBinError(3534,115914);
qMap_Ag_C0_V0->SetBinError(3585,187.9335);
qMap_Ag_C0_V0->SetBinError(3586,1135895);
qMap_Ag_C0_V0->SetBinError(3587,211932);
qMap_Ag_C0_V0->SetBinError(3588,21952.26);
qMap_Ag_C0_V0->SetBinError(3640,132769.8);
qMap_Ag_C0_V0->SetBinError(3641,435575.2);
qMap_Ag_C0_V0->SetMinimum(0);
qMap_Ag_C0_V0->SetEntries(613941);
qMap_Ag_C0_V0->SetStats(0);
qMap_Ag_C0_V0->SetContour(20);
qMap_Ag_C0_V0->SetContourLevel(0,0);
qMap_Ag_C0_V0->SetContourLevel(1,18.30969);
qMap_Ag_C0_V0->SetContourLevel(2,36.61939);
qMap_Ag_C0_V0->SetContourLevel(3,54.92908);
qMap_Ag_C0_V0->SetContourLevel(4,73.23878);
qMap_Ag_C0_V0->SetContourLevel(5,91.54847);
qMap_Ag_C0_V0->SetContourLevel(6,109.8582);
qMap_Ag_C0_V0->SetContourLevel(7,128.1679);
qMap_Ag_C0_V0->SetContourLevel(8,146.4776);
qMap_Ag_C0_V0->SetContourLevel(9,164.7872);
qMap_Ag_C0_V0->SetContourLevel(10,183.0969);
qMap_Ag_C0_V0->SetContourLevel(11,201.4066);
qMap_Ag_C0_V0->SetContourLevel(12,219.7163);
qMap_Ag_C0_V0->SetContourLevel(13,238.026);
qMap_Ag_C0_V0->SetContourLevel(14,256.3357);
qMap_Ag_C0_V0->SetContourLevel(15,274.6454);
qMap_Ag_C0_V0->SetContourLevel(16,292.9551);
qMap_Ag_C0_V0->SetContourLevel(17,311.2648);
qMap_Ag_C0_V0->SetContourLevel(18,329.5745);
qMap_Ag_C0_V0->SetContourLevel(19,347.8842);


ci = root.TColor.GetColor("#000099");
qMap_Ag_C0_V0->SetLineColor(ci);
qMap_Ag_C0_V0->GetXaxis()->SetTitle("col");
qMap_Ag_C0_V0->GetXaxis()->SetRange(15,33);
qMap_Ag_C0_V0->GetXaxis()->SetNdivisions(508);
qMap_Ag_C0_V0->GetXaxis()->SetLabelFont(42);
qMap_Ag_C0_V0->GetXaxis()->SetLabelSize(0.05);
qMap_Ag_C0_V0->GetXaxis()->SetTitleSize(0.05);
qMap_Ag_C0_V0->GetXaxis()->SetTitleOffset(1.1);
qMap_Ag_C0_V0->GetXaxis()->SetTitleFont(42);
qMap_Ag_C0_V0->GetYaxis()->SetTitle("row");
qMap_Ag_C0_V0->GetYaxis()->SetRange(55,76);
qMap_Ag_C0_V0->GetYaxis()->SetLabelFont(42);
qMap_Ag_C0_V0->GetYaxis()->SetLabelSize(0.05);
qMap_Ag_C0_V0->GetYaxis()->SetTitleSize(0.05);
qMap_Ag_C0_V0->GetYaxis()->SetTitleOffset(1.1);
qMap_Ag_C0_V0->GetYaxis()->SetTitleFont(42);
qMap_Ag_C0_V0->GetZaxis()->SetLabelFont(42);
qMap_Ag_C0_V0->GetZaxis()->SetLabelSize(0.035);
qMap_Ag_C0_V0->GetZaxis()->SetTitleSize(0.035);
qMap_Ag_C0_V0->GetZaxis()->SetTitleFont(42);
