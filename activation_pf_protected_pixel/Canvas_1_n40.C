{
//=========Macro generated from canvas: Canvas_1_n40/Canvas_1_n40
//=========  (Fri Jul 13 20:51:12 2018) by ROOT version5.34/36
   TCanvas *Canvas_1_n40 = new TCanvas("Canvas_1_n40", "Canvas_1_n40",323,105,538,321);
   gStyle->SetOptStat(0);
   Canvas_1_n40->SetHighLightColor(2);
   Canvas_1_n40->Range(33,18.75,43,31.25);
   Canvas_1_n40->SetFillColor(0);
   Canvas_1_n40->SetBorderMode(0);
   Canvas_1_n40->SetBorderSize(2);
   Canvas_1_n40->SetFrameBorderMode(0);
   Canvas_1_n40->SetFrameBorderMode(0);
   
   TProfile2D *qMap_Ag_C0_V0 = new TProfile2D("qMap_Ag_C0_V0","qMap_Ag_C0 (V0)",52,0,52,80,0,80,0,0);
   qMap_Ag_C0_V0->SetBinEntries(1388,80159);
   qMap_Ag_C0_V0->SetBinEntries(1389,98309);
   qMap_Ag_C0_V0->SetBinEntries(1442,119399);
   qMap_Ag_C0_V0->SetBinEntries(1443,176591);
   qMap_Ag_C0_V0->SetBinEntries(1496,2674);
   qMap_Ag_C0_V0->SetBinEntries(1497,14121);
   qMap_Ag_C0_V0->SetBinContent(1388,8.757417e+07);
   qMap_Ag_C0_V0->SetBinContent(1389,3.68314e+07);
   qMap_Ag_C0_V0->SetBinContent(1442,2.006045e+08);
   qMap_Ag_C0_V0->SetBinContent(1443,2.404082e+08);
   qMap_Ag_C0_V0->SetBinContent(1496,136360);
   qMap_Ag_C0_V0->SetBinContent(1497,896349);
   qMap_Ag_C0_V0->SetBinError(1388,2272507);
   qMap_Ag_C0_V0->SetBinError(1389,1195475);
   qMap_Ag_C0_V0->SetBinError(1442,3354715);
   qMap_Ag_C0_V0->SetBinError(1443,3627974);
   qMap_Ag_C0_V0->SetBinError(1496,2690.923);
   qMap_Ag_C0_V0->SetBinError(1497,7893.636);
   qMap_Ag_C0_V0->SetMinimum(0);
   qMap_Ag_C0_V0->SetEntries(491253);
   qMap_Ag_C0_V0->SetStats(0);
   qMap_Ag_C0_V0->SetContour(20);
   qMap_Ag_C0_V0->SetContourLevel(0,0);
   qMap_Ag_C0_V0->SetContourLevel(1,84.00592);
   qMap_Ag_C0_V0->SetContourLevel(2,168.0118);
   qMap_Ag_C0_V0->SetContourLevel(3,252.0178);
   qMap_Ag_C0_V0->SetContourLevel(4,336.0237);
   qMap_Ag_C0_V0->SetContourLevel(5,420.0296);
   qMap_Ag_C0_V0->SetContourLevel(6,504.0355);
   qMap_Ag_C0_V0->SetContourLevel(7,588.0414);
   qMap_Ag_C0_V0->SetContourLevel(8,672.0474);
   qMap_Ag_C0_V0->SetContourLevel(9,756.0533);
   qMap_Ag_C0_V0->SetContourLevel(10,840.0592);
   qMap_Ag_C0_V0->SetContourLevel(11,924.0651);
   qMap_Ag_C0_V0->SetContourLevel(12,1008.071);
   qMap_Ag_C0_V0->SetContourLevel(13,1092.077);
   qMap_Ag_C0_V0->SetContourLevel(14,1176.083);
   qMap_Ag_C0_V0->SetContourLevel(15,1260.089);
   qMap_Ag_C0_V0->SetContourLevel(16,1344.095);
   qMap_Ag_C0_V0->SetContourLevel(17,1428.101);
   qMap_Ag_C0_V0->SetContourLevel(18,1512.107);
   qMap_Ag_C0_V0->SetContourLevel(19,1596.112);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   qMap_Ag_C0_V0->SetLineColor(ci);
   qMap_Ag_C0_V0->GetXaxis()->SetTitle("col");
   qMap_Ag_C0_V0->GetXaxis()->SetRange(35,42);
   qMap_Ag_C0_V0->GetXaxis()->SetNdivisions(508);
   qMap_Ag_C0_V0->GetXaxis()->SetLabelFont(42);
   qMap_Ag_C0_V0->GetXaxis()->SetLabelSize(0.05);
   qMap_Ag_C0_V0->GetXaxis()->SetTitleSize(0.05);
   qMap_Ag_C0_V0->GetXaxis()->SetTitleOffset(1.1);
   qMap_Ag_C0_V0->GetXaxis()->SetTitleFont(42);
   qMap_Ag_C0_V0->GetYaxis()->SetTitle("row");
   qMap_Ag_C0_V0->GetYaxis()->SetRange(21,30);
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
