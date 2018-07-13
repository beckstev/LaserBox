{
//=========Macro generated from canvas: Canvas_1/Canvas_1
//=========  (Fri Jul 13 16:01:20 2018) by ROOT version5.34/36
   TCanvas *Canvas_1 = new TCanvas("Canvas_1", "Canvas_1",1378,528,538,321);
   gStyle->SetOptStat(0);
   Canvas_1->SetHighLightColor(2);
   Canvas_1->Range(-6.5,-10,58.5,90);
   Canvas_1->SetFillColor(0);
   Canvas_1->SetBorderMode(0);
   Canvas_1->SetBorderSize(2);
   Canvas_1->SetFrameBorderMode(0);
   Canvas_1->SetFrameBorderMode(0);
   
   TProfile2D *qMap_Ag_C0_V0 = new TProfile2D("qMap_Ag_C0_V0","qMap_Ag_C0 (V0)",52,0,52,80,0,80,0,0);
   qMap_Ag_C0_V0->SetBinEntries(2452,17860);
   qMap_Ag_C0_V0->SetBinEntries(2453,4739);
   qMap_Ag_C0_V0->SetBinEntries(2506,118640);
   qMap_Ag_C0_V0->SetBinEntries(2507,80862);
   qMap_Ag_C0_V0->SetBinEntries(2560,127145);
   qMap_Ag_C0_V0->SetBinEntries(2561,89550);
   qMap_Ag_C0_V0->SetBinEntries(2614,40);
   qMap_Ag_C0_V0->SetBinContent(2452,2640159);
   qMap_Ag_C0_V0->SetBinContent(2453,250351);
   qMap_Ag_C0_V0->SetBinContent(2506,1.172519e+08);
   qMap_Ag_C0_V0->SetBinContent(2507,2.13815e+07);
   qMap_Ag_C0_V0->SetBinContent(2560,1.664191e+08);
   qMap_Ag_C0_V0->SetBinContent(2561,2.109096e+07);
   qMap_Ag_C0_V0->SetBinContent(2614,1605);
   qMap_Ag_C0_V0->SetBinError(2452,20969.95);
   qMap_Ag_C0_V0->SetBinError(2453,3735.723);
   qMap_Ag_C0_V0->SetBinError(2506,2418194);
   qMap_Ag_C0_V0->SetBinError(2507,804356.6);
   qMap_Ag_C0_V0->SetBinError(2560,3021759);
   qMap_Ag_C0_V0->SetBinError(2561,601072.5);
   qMap_Ag_C0_V0->SetBinError(2614,259.1428);
   qMap_Ag_C0_V0->SetMinimum(0);
   qMap_Ag_C0_V0->SetEntries(438836);
   qMap_Ag_C0_V0->SetStats(0);
   qMap_Ag_C0_V0->SetContour(20);
   qMap_Ag_C0_V0->SetContourLevel(0,0);
   qMap_Ag_C0_V0->SetContourLevel(1,65.4446);
   qMap_Ag_C0_V0->SetContourLevel(2,130.8892);
   qMap_Ag_C0_V0->SetContourLevel(3,196.3338);
   qMap_Ag_C0_V0->SetContourLevel(4,261.7784);
   qMap_Ag_C0_V0->SetContourLevel(5,327.223);
   qMap_Ag_C0_V0->SetContourLevel(6,392.6676);
   qMap_Ag_C0_V0->SetContourLevel(7,458.1122);
   qMap_Ag_C0_V0->SetContourLevel(8,523.5568);
   qMap_Ag_C0_V0->SetContourLevel(9,589.0014);
   qMap_Ag_C0_V0->SetContourLevel(10,654.446);
   qMap_Ag_C0_V0->SetContourLevel(11,719.8906);
   qMap_Ag_C0_V0->SetContourLevel(12,785.3352);
   qMap_Ag_C0_V0->SetContourLevel(13,850.7798);
   qMap_Ag_C0_V0->SetContourLevel(14,916.2244);
   qMap_Ag_C0_V0->SetContourLevel(15,981.669);
   qMap_Ag_C0_V0->SetContourLevel(16,1047.114);
   qMap_Ag_C0_V0->SetContourLevel(17,1112.558);
   qMap_Ag_C0_V0->SetContourLevel(18,1178.003);
   qMap_Ag_C0_V0->SetContourLevel(19,1243.447);

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
