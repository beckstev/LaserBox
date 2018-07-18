{
//=========Macro generated from canvas: Canvas_1/Canvas_1
//=========  (Wed Jul 18 15:44:19 2018) by ROOT version5.34/36
   TCanvas *Canvas_1 = new TCanvas("Canvas_1", "Canvas_1",323,105,538,321);
   gStyle->SetOptStat(0);
   Canvas_1->SetHighLightColor(2);
   Canvas_1->Range(-6.5,-10,58.5,90);
   Canvas_1->SetFillColor(0);
   Canvas_1->SetBorderMode(0);
   Canvas_1->SetBorderSize(2);
   Canvas_1->SetFrameBorderMode(0);
   Canvas_1->SetFrameBorderMode(0);
   
   TProfile2D *qMap_Ag_C0_V0 = new TProfile2D("qMap_Ag_C0_V0","qMap_Ag_C0 (V0)",52,0,52,80,0,80,0,0);
   qMap_Ag_C0_V0->SetBinEntries(3478,81275);
   qMap_Ag_C0_V0->SetBinEntries(3479,122609);
   qMap_Ag_C0_V0->SetBinEntries(3532,116591);
   qMap_Ag_C0_V0->SetBinEntries(3533,162912);
   qMap_Ag_C0_V0->SetBinEntries(3586,13662);
   qMap_Ag_C0_V0->SetBinEntries(3587,33316);
   qMap_Ag_C0_V0->SetBinContent(3478,2.450108e+07);
   qMap_Ag_C0_V0->SetBinContent(3479,5.874212e+07);
   qMap_Ag_C0_V0->SetBinContent(3532,7.348653e+07);
   qMap_Ag_C0_V0->SetBinContent(3533,1.412881e+08);
   qMap_Ag_C0_V0->SetBinContent(3586,848479);
   qMap_Ag_C0_V0->SetBinContent(3587,5917797);
   qMap_Ag_C0_V0->SetBinError(3478,946134.8);
   qMap_Ag_C0_V0->SetBinError(3479,1540283);
   qMap_Ag_C0_V0->SetBinError(3532,1914152);
   qMap_Ag_C0_V0->SetBinError(3533,2646036);
   qMap_Ag_C0_V0->SetBinError(3586,7438.767);
   qMap_Ag_C0_V0->SetBinError(3587,219897.5);
   qMap_Ag_C0_V0->SetMinimum(0);
   qMap_Ag_C0_V0->SetEntries(530365);
   qMap_Ag_C0_V0->SetStats(0);
   qMap_Ag_C0_V0->SetContour(20);
   qMap_Ag_C0_V0->SetContourLevel(0,0);
   qMap_Ag_C0_V0->SetContourLevel(1,43.36333);
   qMap_Ag_C0_V0->SetContourLevel(2,86.72665);
   qMap_Ag_C0_V0->SetContourLevel(3,130.09);
   qMap_Ag_C0_V0->SetContourLevel(4,173.4533);
   qMap_Ag_C0_V0->SetContourLevel(5,216.8166);
   qMap_Ag_C0_V0->SetContourLevel(6,260.18);
   qMap_Ag_C0_V0->SetContourLevel(7,303.5433);
   qMap_Ag_C0_V0->SetContourLevel(8,346.9066);
   qMap_Ag_C0_V0->SetContourLevel(9,390.2699);
   qMap_Ag_C0_V0->SetContourLevel(10,433.6333);
   qMap_Ag_C0_V0->SetContourLevel(11,476.9966);
   qMap_Ag_C0_V0->SetContourLevel(12,520.3599);
   qMap_Ag_C0_V0->SetContourLevel(13,563.7232);
   qMap_Ag_C0_V0->SetContourLevel(14,607.0866);
   qMap_Ag_C0_V0->SetContourLevel(15,650.4499);
   qMap_Ag_C0_V0->SetContourLevel(16,693.8132);
   qMap_Ag_C0_V0->SetContourLevel(17,737.1766);
   qMap_Ag_C0_V0->SetContourLevel(18,780.5399);
   qMap_Ag_C0_V0->SetContourLevel(19,823.9032);

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
