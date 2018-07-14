{
//=========Macro generated from canvas: Canvas_1_n40/Canvas_1_n40
//=========  (Fri Jul 13 15:54:06 2018) by ROOT version5.34/36
   TCanvas *Canvas_1_n40 = new TCanvas("Canvas_1_n40", "Canvas_1_n40",1378,105,538,321);
   gStyle->SetOptStat(0);
   Canvas_1_n40->SetHighLightColor(2);
   Canvas_1_n40->Range(13.125,25.125,31.875,63.875);
   Canvas_1_n40->SetFillColor(0);
   Canvas_1_n40->SetBorderMode(0);
   Canvas_1_n40->SetBorderSize(2);
   Canvas_1_n40->SetFrameBorderMode(0);
   Canvas_1_n40->SetFrameBorderMode(0);
   
   TProfile2D *qMap_Ag_C0_V0 = new TProfile2D("qMap_Ag_C0_V0","qMap_Ag_C0 (V0)",52,0,52,80,0,80,0,0);
   qMap_Ag_C0_V0->SetBinEntries(2452,14630);
   qMap_Ag_C0_V0->SetBinEntries(2453,10575);
   qMap_Ag_C0_V0->SetBinEntries(2506,94143);
   qMap_Ag_C0_V0->SetBinEntries(2507,58107);
   qMap_Ag_C0_V0->SetBinEntries(2560,122976);
   qMap_Ag_C0_V0->SetBinEntries(2561,34797);
   qMap_Ag_C0_V0->SetBinContent(2452,808604);
   qMap_Ag_C0_V0->SetBinContent(2453,533645);
   qMap_Ag_C0_V0->SetBinContent(2506,3.718655e+07);
   qMap_Ag_C0_V0->SetBinContent(2507,1.236262e+07);
   qMap_Ag_C0_V0->SetBinContent(2560,9.390444e+07);
   qMap_Ag_C0_V0->SetBinContent(2561,4942135);
   qMap_Ag_C0_V0->SetBinError(2452,6929.901);
   qMap_Ag_C0_V0->SetBinError(2453,5384.512);
   qMap_Ag_C0_V0->SetBinError(2506,806193.3);
   qMap_Ag_C0_V0->SetBinError(2507,517870.9);
   qMap_Ag_C0_V0->SetBinError(2560,2121180);
   qMap_Ag_C0_V0->SetBinError(2561,246480.2);
   qMap_Ag_C0_V0->SetMinimum(0);
   qMap_Ag_C0_V0->SetEntries(335228);
   qMap_Ag_C0_V0->SetContour(20);
   qMap_Ag_C0_V0->SetContourLevel(0,0);
   qMap_Ag_C0_V0->SetContourLevel(1,38.17999);
   qMap_Ag_C0_V0->SetContourLevel(2,76.35998);
   qMap_Ag_C0_V0->SetContourLevel(3,114.54);
   qMap_Ag_C0_V0->SetContourLevel(4,152.72);
   qMap_Ag_C0_V0->SetContourLevel(5,190.8999);
   qMap_Ag_C0_V0->SetContourLevel(6,229.0799);
   qMap_Ag_C0_V0->SetContourLevel(7,267.2599);
   qMap_Ag_C0_V0->SetContourLevel(8,305.4399);
   qMap_Ag_C0_V0->SetContourLevel(9,343.6199);
   qMap_Ag_C0_V0->SetContourLevel(10,381.7999);
   qMap_Ag_C0_V0->SetContourLevel(11,419.9799);
   qMap_Ag_C0_V0->SetContourLevel(12,458.1599);
   qMap_Ag_C0_V0->SetContourLevel(13,496.3398);
   qMap_Ag_C0_V0->SetContourLevel(14,534.5198);
   qMap_Ag_C0_V0->SetContourLevel(15,572.6998);
   qMap_Ag_C0_V0->SetContourLevel(16,610.8798);
   qMap_Ag_C0_V0->SetContourLevel(17,649.0598);
   qMap_Ag_C0_V0->SetContourLevel(18,687.2398);
   qMap_Ag_C0_V0->SetContourLevel(19,725.4198);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   qMap_Ag_C0_V0->SetLineColor(ci);
   qMap_Ag_C0_V0->GetXaxis()->SetTitle("col");
   qMap_Ag_C0_V0->GetXaxis()->SetRange(16,30);
   qMap_Ag_C0_V0->GetXaxis()->SetNdivisions(508);
   qMap_Ag_C0_V0->GetXaxis()->SetLabelFont(42);
   qMap_Ag_C0_V0->GetXaxis()->SetLabelSize(0.05);
   qMap_Ag_C0_V0->GetXaxis()->SetTitleSize(0.05);
   qMap_Ag_C0_V0->GetXaxis()->SetTitleOffset(1.1);
   qMap_Ag_C0_V0->GetXaxis()->SetTitleFont(42);
   qMap_Ag_C0_V0->GetYaxis()->SetTitle("row");
   qMap_Ag_C0_V0->GetYaxis()->SetRange(30,60);
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
