{
//=========Macro generated from canvas: Canvas_1/Canvas_1
//=========  (Wed Jul 18 15:52:02 2018) by ROOT version5.34/36
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
   qMap_Ag_C0_V0->SetBinEntries(3425,5863);
   qMap_Ag_C0_V0->SetBinEntries(3478,14413);
   qMap_Ag_C0_V0->SetBinEntries(3479,111615);
   qMap_Ag_C0_V0->SetBinEntries(3480,3);
   qMap_Ag_C0_V0->SetBinEntries(3532,14429);
   qMap_Ag_C0_V0->SetBinEntries(3533,102646);
   qMap_Ag_C0_V0->SetBinEntries(3587,67);
   qMap_Ag_C0_V0->SetBinContent(3425,321828);
   qMap_Ag_C0_V0->SetBinContent(3478,886358);
   qMap_Ag_C0_V0->SetBinContent(3479,3.807716e+07);
   qMap_Ag_C0_V0->SetBinContent(3480,184);
   qMap_Ag_C0_V0->SetBinContent(3532,1532989);
   qMap_Ag_C0_V0->SetBinContent(3533,3.74638e+07);
   qMap_Ag_C0_V0->SetBinContent(3587,4295);
   qMap_Ag_C0_V0->SetBinError(3425,4348.232);
   qMap_Ag_C0_V0->SetBinError(3478,7792.301);
   qMap_Ag_C0_V0->SetBinError(3479,1245031);
   qMap_Ag_C0_V0->SetBinError(3480,108.2867);
   qMap_Ag_C0_V0->SetBinError(3532,12846.39);
   qMap_Ag_C0_V0->SetBinError(3533,453454.5);
   qMap_Ag_C0_V0->SetBinError(3587,540.0343);
   qMap_Ag_C0_V0->SetMinimum(0);
   qMap_Ag_C0_V0->SetEntries(249036);
   qMap_Ag_C0_V0->SetStats(0);
   qMap_Ag_C0_V0->SetContour(20);
   qMap_Ag_C0_V0->SetContourLevel(0,0);
   qMap_Ag_C0_V0->SetContourLevel(1,18.24903);
   qMap_Ag_C0_V0->SetContourLevel(2,36.49806);
   qMap_Ag_C0_V0->SetContourLevel(3,54.74708);
   qMap_Ag_C0_V0->SetContourLevel(4,72.99611);
   qMap_Ag_C0_V0->SetContourLevel(5,91.24514);
   qMap_Ag_C0_V0->SetContourLevel(6,109.4942);
   qMap_Ag_C0_V0->SetContourLevel(7,127.7432);
   qMap_Ag_C0_V0->SetContourLevel(8,145.9922);
   qMap_Ag_C0_V0->SetContourLevel(9,164.2413);
   qMap_Ag_C0_V0->SetContourLevel(10,182.4903);
   qMap_Ag_C0_V0->SetContourLevel(11,200.7393);
   qMap_Ag_C0_V0->SetContourLevel(12,218.9883);
   qMap_Ag_C0_V0->SetContourLevel(13,237.2374);
   qMap_Ag_C0_V0->SetContourLevel(14,255.4864);
   qMap_Ag_C0_V0->SetContourLevel(15,273.7354);
   qMap_Ag_C0_V0->SetContourLevel(16,291.9845);
   qMap_Ag_C0_V0->SetContourLevel(17,310.2335);
   qMap_Ag_C0_V0->SetContourLevel(18,328.4825);
   qMap_Ag_C0_V0->SetContourLevel(19,346.7315);

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
