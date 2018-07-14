{
//=========Macro generated from canvas: Canvas_1/Canvas_1
//=========  (Fri Jul 13 16:13:12 2018) by ROOT version5.34/36
   TCanvas *Canvas_1 = new TCanvas("Canvas_1", "Canvas_1",1378,105,538,321);
   gStyle->SetOptStat(0);
   Canvas_1->SetHighLightColor(2);
   Canvas_1->Range(-6.5,-10,58.5,90);
   Canvas_1->SetFillColor(0);
   Canvas_1->SetBorderMode(0);
   Canvas_1->SetBorderSize(2);
   Canvas_1->SetFrameBorderMode(0);
   Canvas_1->SetFrameBorderMode(0);
   
   TProfile2D *qMap_Ag_C0_V0 = new TProfile2D("qMap_Ag_C0_V0","qMap_Ag_C0 (V0)",52,0,52,80,0,80,0,0);
   qMap_Ag_C0_V0->SetBinEntries(2452,19290);
   qMap_Ag_C0_V0->SetBinEntries(2453,31796);
   qMap_Ag_C0_V0->SetBinEntries(2506,152945);
   qMap_Ag_C0_V0->SetBinEntries(2507,114595);
   qMap_Ag_C0_V0->SetBinEntries(2560,78957);
   qMap_Ag_C0_V0->SetBinEntries(2561,82510);
   qMap_Ag_C0_V0->SetBinContent(2452,2453704);
   qMap_Ag_C0_V0->SetBinContent(2453,3128671);
   qMap_Ag_C0_V0->SetBinContent(2506,8.315548e+07);
   qMap_Ag_C0_V0->SetBinContent(2507,3.144251e+08);
   qMap_Ag_C0_V0->SetBinContent(2560,1.26811e+07);
   qMap_Ag_C0_V0->SetBinContent(2561,1.668271e+07);
   qMap_Ag_C0_V0->SetBinError(2452,19053.56);
   qMap_Ag_C0_V0->SetBinError(2453,19418.29);
   qMap_Ag_C0_V0->SetBinError(2506,1800047);
   qMap_Ag_C0_V0->SetBinError(2507,4330962);
   qMap_Ag_C0_V0->SetBinError(2560,181946.3);
   qMap_Ag_C0_V0->SetBinError(2561,148772.7);
   qMap_Ag_C0_V0->SetMinimum(0);
   qMap_Ag_C0_V0->SetEntries(480093);
   qMap_Ag_C0_V0->SetStats(0);
   qMap_Ag_C0_V0->SetContour(20);
   qMap_Ag_C0_V0->SetContourLevel(0,0);
   qMap_Ag_C0_V0->SetContourLevel(1,137.1897);
   qMap_Ag_C0_V0->SetContourLevel(2,274.3794);
   qMap_Ag_C0_V0->SetContourLevel(3,411.5692);
   qMap_Ag_C0_V0->SetContourLevel(4,548.7589);
   qMap_Ag_C0_V0->SetContourLevel(5,685.9486);
   qMap_Ag_C0_V0->SetContourLevel(6,823.1383);
   qMap_Ag_C0_V0->SetContourLevel(7,960.3281);
   qMap_Ag_C0_V0->SetContourLevel(8,1097.518);
   qMap_Ag_C0_V0->SetContourLevel(9,1234.708);
   qMap_Ag_C0_V0->SetContourLevel(10,1371.897);
   qMap_Ag_C0_V0->SetContourLevel(11,1509.087);
   qMap_Ag_C0_V0->SetContourLevel(12,1646.277);
   qMap_Ag_C0_V0->SetContourLevel(13,1783.466);
   qMap_Ag_C0_V0->SetContourLevel(14,1920.656);
   qMap_Ag_C0_V0->SetContourLevel(15,2057.846);
   qMap_Ag_C0_V0->SetContourLevel(16,2195.036);
   qMap_Ag_C0_V0->SetContourLevel(17,2332.225);
   qMap_Ag_C0_V0->SetContourLevel(18,2469.415);
   qMap_Ag_C0_V0->SetContourLevel(19,2606.605);

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
