{
//=========Macro generated from canvas: Canvas_1/Canvas_1
//=========  (Fri Jul 13 16:33:38 2018) by ROOT version5.34/36
   TCanvas *Canvas_1 = new TCanvas("Canvas_1", "Canvas_1",1352,105,538,321);
   gStyle->SetOptStat(0);
   Canvas_1->SetHighLightColor(2);
   Canvas_1->Range(-6.5,-10,58.5,90);
   Canvas_1->SetFillColor(0);
   Canvas_1->SetBorderMode(0);
   Canvas_1->SetBorderSize(2);
   Canvas_1->SetFrameBorderMode(0);
   Canvas_1->SetFrameBorderMode(0);
   
   TProfile2D *qMap_Ag_C0_V0 = new TProfile2D("qMap_Ag_C0_V0","qMap_Ag_C0 (V0)",52,0,52,80,0,80,0,0);
   qMap_Ag_C0_V0->SetBinEntries(2452,75288);
   qMap_Ag_C0_V0->SetBinEntries(2453,64282);
   qMap_Ag_C0_V0->SetBinEntries(2506,127191);
   qMap_Ag_C0_V0->SetBinEntries(2507,113872);
   qMap_Ag_C0_V0->SetBinEntries(2560,20225);
   qMap_Ag_C0_V0->SetBinEntries(2561,15144);
   qMap_Ag_C0_V0->SetBinContent(2452,1.253514e+07);
   qMap_Ag_C0_V0->SetBinContent(2453,1.17078e+07);
   qMap_Ag_C0_V0->SetBinContent(2506,4.109927e+07);
   qMap_Ag_C0_V0->SetBinContent(2507,3.839607e+08);
   qMap_Ag_C0_V0->SetBinContent(2560,1959233);
   qMap_Ag_C0_V0->SetBinContent(2561,2159477);
   qMap_Ag_C0_V0->SetBinError(2452,290387.9);
   qMap_Ag_C0_V0->SetBinError(2453,517147.6);
   qMap_Ag_C0_V0->SetBinError(2506,631771.1);
   qMap_Ag_C0_V0->SetBinError(2507,4825338);
   qMap_Ag_C0_V0->SetBinError(2560,67026.04);
   qMap_Ag_C0_V0->SetBinError(2561,17885.33);
   qMap_Ag_C0_V0->SetMinimum(0);
   qMap_Ag_C0_V0->SetEntries(416002);
   qMap_Ag_C0_V0->SetStats(0);
   qMap_Ag_C0_V0->SetContour(20);
   qMap_Ag_C0_V0->SetContourLevel(0,0);
   qMap_Ag_C0_V0->SetContourLevel(1,168.5931);
   qMap_Ag_C0_V0->SetContourLevel(2,337.1862);
   qMap_Ag_C0_V0->SetContourLevel(3,505.7793);
   qMap_Ag_C0_V0->SetContourLevel(4,674.3725);
   qMap_Ag_C0_V0->SetContourLevel(5,842.9656);
   qMap_Ag_C0_V0->SetContourLevel(6,1011.559);
   qMap_Ag_C0_V0->SetContourLevel(7,1180.152);
   qMap_Ag_C0_V0->SetContourLevel(8,1348.745);
   qMap_Ag_C0_V0->SetContourLevel(9,1517.338);
   qMap_Ag_C0_V0->SetContourLevel(10,1685.931);
   qMap_Ag_C0_V0->SetContourLevel(11,1854.524);
   qMap_Ag_C0_V0->SetContourLevel(12,2023.117);
   qMap_Ag_C0_V0->SetContourLevel(13,2191.71);
   qMap_Ag_C0_V0->SetContourLevel(14,2360.304);
   qMap_Ag_C0_V0->SetContourLevel(15,2528.897);
   qMap_Ag_C0_V0->SetContourLevel(16,2697.49);
   qMap_Ag_C0_V0->SetContourLevel(17,2866.083);
   qMap_Ag_C0_V0->SetContourLevel(18,3034.676);
   qMap_Ag_C0_V0->SetContourLevel(19,3203.269);

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
