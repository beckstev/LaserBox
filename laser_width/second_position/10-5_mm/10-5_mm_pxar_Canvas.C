{
//=========Macro generated from canvas: Canvas_1/Canvas_1
//=========  (Mon Jul 16 15:10:31 2018) by ROOT version5.34/36
   TCanvas *Canvas_1 = new TCanvas("Canvas_1", "Canvas_1",323,528,538,321);
   gStyle->SetOptStat(0);
   Canvas_1->SetHighLightColor(2);
   Canvas_1->Range(-6.5,-10,58.5,90);
   Canvas_1->SetFillColor(0);
   Canvas_1->SetBorderMode(0);
   Canvas_1->SetBorderSize(2);
   Canvas_1->SetFrameBorderMode(0);
   Canvas_1->SetFrameBorderMode(0);
   
   TProfile2D *qMap_Ag_C0_V0 = new TProfile2D("qMap_Ag_C0_V0","qMap_Ag_C0 (V0)",52,0,52,80,0,80,0,0);
   qMap_Ag_C0_V0->SetBinEntries(3585,29768);
   qMap_Ag_C0_V0->SetBinEntries(3586,79524);
   qMap_Ag_C0_V0->SetBinEntries(3639,83953);
   qMap_Ag_C0_V0->SetBinEntries(3640,124982);
   qMap_Ag_C0_V0->SetBinEntries(3641,14345);
   qMap_Ag_C0_V0->SetBinEntries(3693,31598);
   qMap_Ag_C0_V0->SetBinEntries(3694,91098);
   qMap_Ag_C0_V0->SetBinContent(3585,3245287);
   qMap_Ag_C0_V0->SetBinContent(3586,1.615629e+07);
   qMap_Ag_C0_V0->SetBinContent(3639,2.731302e+07);
   qMap_Ag_C0_V0->SetBinContent(3640,3.14566e+08);
   qMap_Ag_C0_V0->SetBinContent(3641,1444064);
   qMap_Ag_C0_V0->SetBinContent(3693,3763256);
   qMap_Ag_C0_V0->SetBinContent(3694,2.928397e+07);
   qMap_Ag_C0_V0->SetBinError(3585,174261.7);
   qMap_Ag_C0_V0->SetBinError(3586,278676.5);
   qMap_Ag_C0_V0->SetBinError(3639,960499.6);
   qMap_Ag_C0_V0->SetBinError(3640,4324021);
   qMap_Ag_C0_V0->SetBinError(3641,12124.33);
   qMap_Ag_C0_V0->SetBinError(3693,148045.1);
   qMap_Ag_C0_V0->SetBinError(3694,865776);
   qMap_Ag_C0_V0->SetMinimum(0);
   qMap_Ag_C0_V0->SetEntries(455268);
   qMap_Ag_C0_V0->SetStats(0);
   qMap_Ag_C0_V0->SetContour(20);
   qMap_Ag_C0_V0->SetContourLevel(0,0);
   qMap_Ag_C0_V0->SetContourLevel(1,125.8445);
   qMap_Ag_C0_V0->SetContourLevel(2,251.689);
   qMap_Ag_C0_V0->SetContourLevel(3,377.5335);
   qMap_Ag_C0_V0->SetContourLevel(4,503.3781);
   qMap_Ag_C0_V0->SetContourLevel(5,629.2226);
   qMap_Ag_C0_V0->SetContourLevel(6,755.0671);
   qMap_Ag_C0_V0->SetContourLevel(7,880.9116);
   qMap_Ag_C0_V0->SetContourLevel(8,1006.756);
   qMap_Ag_C0_V0->SetContourLevel(9,1132.601);
   qMap_Ag_C0_V0->SetContourLevel(10,1258.445);
   qMap_Ag_C0_V0->SetContourLevel(11,1384.29);
   qMap_Ag_C0_V0->SetContourLevel(12,1510.134);
   qMap_Ag_C0_V0->SetContourLevel(13,1635.979);
   qMap_Ag_C0_V0->SetContourLevel(14,1761.823);
   qMap_Ag_C0_V0->SetContourLevel(15,1887.668);
   qMap_Ag_C0_V0->SetContourLevel(16,2013.512);
   qMap_Ag_C0_V0->SetContourLevel(17,2139.357);
   qMap_Ag_C0_V0->SetContourLevel(18,2265.201);
   qMap_Ag_C0_V0->SetContourLevel(19,2391.046);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   qMap_Ag_C0_V0->SetLineColor(ci);
   qMap_Ag_C0_V0->GetXaxis()->SetTitle("col");
   qMap_Ag_C0_V0->GetXaxis()->SetRange(1,52);
   qMap_Ag_C0_V0->GetXaxis()->SetNdivisions(508);
   qMap_Ag_C0_V0->GetXaxis()->SetLabelFont(42);
   qMap_Ag_C0_V0->GetXaxis()->SetLabelSize(0.05);
   qMap_Ag_C0_V0->GetXaxis()->SetTitleSize(0.05);
   qMap_Ag_C0_V0->GetXaxis()->SetTitleOffset(1.1);
   qMap_Ag_C0_V0->GetXaxis()->SetTitleFont(42);
   qMap_Ag_C0_V0->GetYaxis()->SetTitle("row");
   qMap_Ag_C0_V0->GetYaxis()->SetRange(1,80);
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
   Canvas_1->Modified();
   Canvas_1->cd();
   Canvas_1->SetSelected(Canvas_1);
}
