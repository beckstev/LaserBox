{
//=========Macro generated from canvas: Canvas_1_n40/Canvas_1_n40
//=========  (Mon Jul 16 15:07:03 2018) by ROOT version5.34/36
   TCanvas *Canvas_1_n40 = new TCanvas("Canvas_1_n40", "Canvas_1_n40",1378,528,538,321);
   gStyle->SetOptStat(0);
   Canvas_1_n40->SetHighLightColor(2);
   Canvas_1_n40->Range(13.25,51.375,30.75,77.625);
   Canvas_1_n40->SetFillColor(0);
   Canvas_1_n40->SetBorderMode(0);
   Canvas_1_n40->SetBorderSize(2);
   Canvas_1_n40->SetFrameBorderMode(0);
   Canvas_1_n40->SetFrameBorderMode(0);
   
   TProfile2D *qMap_Ag_C0_V0 = new TProfile2D("qMap_Ag_C0_V0","qMap_Ag_C0 (V0)",52,0,52,80,0,80,0,0);
   qMap_Ag_C0_V0->SetBinEntries(3585,59);
   qMap_Ag_C0_V0->SetBinEntries(3586,72412);
   qMap_Ag_C0_V0->SetBinEntries(3639,63557);
   qMap_Ag_C0_V0->SetBinEntries(3640,157117);
   qMap_Ag_C0_V0->SetBinEntries(3641,250);
   qMap_Ag_C0_V0->SetBinEntries(3693,31);
   qMap_Ag_C0_V0->SetBinEntries(3694,60965);
   qMap_Ag_C0_V0->SetBinContent(3585,2558);
   qMap_Ag_C0_V0->SetBinContent(3586,1.797534e+07);
   qMap_Ag_C0_V0->SetBinContent(3639,1.421422e+07);
   qMap_Ag_C0_V0->SetBinContent(3640,1.026189e+08);
   qMap_Ag_C0_V0->SetBinContent(3641,15463);
   qMap_Ag_C0_V0->SetBinContent(3693,1195);
   qMap_Ag_C0_V0->SetBinContent(3694,1.154859e+07);
   qMap_Ag_C0_V0->SetBinError(3585,338.2041);
   qMap_Ag_C0_V0->SetBinError(3586,610334.8);
   qMap_Ag_C0_V0->SetBinError(3639,649814.1);
   qMap_Ag_C0_V0->SetBinError(3640,2121503);
   qMap_Ag_C0_V0->SetBinError(3641,996.4482);
   qMap_Ag_C0_V0->SetBinError(3693,221.804);
   qMap_Ag_C0_V0->SetBinError(3694,411739.2);
   qMap_Ag_C0_V0->SetMinimum(0);
   qMap_Ag_C0_V0->SetEntries(354391);
   qMap_Ag_C0_V0->SetStats(0);
   qMap_Ag_C0_V0->SetContour(20);
   qMap_Ag_C0_V0->SetContourLevel(0,0);
   qMap_Ag_C0_V0->SetContourLevel(1,32.65683);
   qMap_Ag_C0_V0->SetContourLevel(2,65.31366);
   qMap_Ag_C0_V0->SetContourLevel(3,97.97049);
   qMap_Ag_C0_V0->SetContourLevel(4,130.6273);
   qMap_Ag_C0_V0->SetContourLevel(5,163.2842);
   qMap_Ag_C0_V0->SetContourLevel(6,195.941);
   qMap_Ag_C0_V0->SetContourLevel(7,228.5978);
   qMap_Ag_C0_V0->SetContourLevel(8,261.2547);
   qMap_Ag_C0_V0->SetContourLevel(9,293.9115);
   qMap_Ag_C0_V0->SetContourLevel(10,326.5683);
   qMap_Ag_C0_V0->SetContourLevel(11,359.2251);
   qMap_Ag_C0_V0->SetContourLevel(12,391.882);
   qMap_Ag_C0_V0->SetContourLevel(13,424.5388);
   qMap_Ag_C0_V0->SetContourLevel(14,457.1956);
   qMap_Ag_C0_V0->SetContourLevel(15,489.8525);
   qMap_Ag_C0_V0->SetContourLevel(16,522.5093);
   qMap_Ag_C0_V0->SetContourLevel(17,555.1661);
   qMap_Ag_C0_V0->SetContourLevel(18,587.823);
   qMap_Ag_C0_V0->SetContourLevel(19,620.4798);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   qMap_Ag_C0_V0->SetLineColor(ci);
   qMap_Ag_C0_V0->GetXaxis()->SetTitle("col");
   qMap_Ag_C0_V0->GetXaxis()->SetRange(16,29);
   qMap_Ag_C0_V0->GetXaxis()->SetNdivisions(508);
   qMap_Ag_C0_V0->GetXaxis()->SetLabelFont(42);
   qMap_Ag_C0_V0->GetXaxis()->SetLabelSize(0.05);
   qMap_Ag_C0_V0->GetXaxis()->SetTitleSize(0.05);
   qMap_Ag_C0_V0->GetXaxis()->SetTitleOffset(1.1);
   qMap_Ag_C0_V0->GetXaxis()->SetTitleFont(42);
   qMap_Ag_C0_V0->GetYaxis()->SetTitle("row");
   qMap_Ag_C0_V0->GetYaxis()->SetRange(55,75);
   qMap_Ag_C0_V0->GetYaxis()->SetLabelFont(42);
   qMap_Ag_C0_V0->GetYaxis()->SetLabelSize(0.05);
   qMap_Ag_C0_V0->GetYaxis()->SetTitleSize(0.05);
   qMap_Ag_C0_V0->GetYaxis()->SetTitleOffset(1.1);
   qMap_Ag_C0_V0->GetYaxis()->SetTitleFont(42);
   qMap_Ag_C0_V0->GetZaxis()->SetLabelFont(42);
   qMap_Ag_C0_V0->GetZaxis()->SetLabelSize(0.035);
   qMap_Ag_C0_V0->GetZaxis()->SetTitleSize(0.035);
   qMap_Ag_C0_V0->GetZaxis()->SetTitleFont(42);
   qMap_Ag_C0_V0->Draw("");
   
   TPaveText *pt = new TPaveText(0.3631343,0.9310502,0.6368657,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *text = pt->AddText("qMap_Ag_C0 (V0)");
   pt->Draw();
   Canvas_1_n40->Modified();
   Canvas_1_n40->cd();
   Canvas_1_n40->SetSelected(Canvas_1_n40);
}
