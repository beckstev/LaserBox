{
//=========Macro generated from canvas: Canvas_1/Canvas_1
//=========  (Wed Jul 18 15:48:19 2018) by ROOT version5.34/36
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
   qMap_Ag_C0_V0->SetBinEntries(3425,175);
   qMap_Ag_C0_V0->SetBinEntries(3478,23848);
   qMap_Ag_C0_V0->SetBinEntries(3479,117646);
   qMap_Ag_C0_V0->SetBinEntries(3532,91668);
   qMap_Ag_C0_V0->SetBinEntries(3533,118917);
   qMap_Ag_C0_V0->SetBinEntries(3586,47);
   qMap_Ag_C0_V0->SetBinEntries(3587,20);
   qMap_Ag_C0_V0->SetBinContent(3425,8254);
   qMap_Ag_C0_V0->SetBinContent(3478,3874714);
   qMap_Ag_C0_V0->SetBinContent(3479,8.834933e+07);
   qMap_Ag_C0_V0->SetBinContent(3532,2.466545e+07);
   qMap_Ag_C0_V0->SetBinContent(3533,4.67109e+07);
   qMap_Ag_C0_V0->SetBinContent(3586,2341);
   qMap_Ag_C0_V0->SetBinContent(3587,1154);
   qMap_Ag_C0_V0->SetBinError(3425,639.0681);
   qMap_Ag_C0_V0->SetBinError(3478,133571.8);
   qMap_Ag_C0_V0->SetBinError(3479,2101135);
   qMap_Ag_C0_V0->SetBinError(3532,907432.6);
   qMap_Ag_C0_V0->SetBinError(3533,916466.8);
   qMap_Ag_C0_V0->SetBinError(3586,347.4032);
   qMap_Ag_C0_V0->SetBinError(3587,264.9566);
   qMap_Ag_C0_V0->SetMinimum(0);
   qMap_Ag_C0_V0->SetEntries(352321);
   qMap_Ag_C0_V0->SetStats(0);
   qMap_Ag_C0_V0->SetContour(20);
   qMap_Ag_C0_V0->SetContourLevel(0,0);
   qMap_Ag_C0_V0->SetContourLevel(1,37.5488);
   qMap_Ag_C0_V0->SetContourLevel(2,75.0976);
   qMap_Ag_C0_V0->SetContourLevel(3,112.6464);
   qMap_Ag_C0_V0->SetContourLevel(4,150.1952);
   qMap_Ag_C0_V0->SetContourLevel(5,187.744);
   qMap_Ag_C0_V0->SetContourLevel(6,225.2928);
   qMap_Ag_C0_V0->SetContourLevel(7,262.8416);
   qMap_Ag_C0_V0->SetContourLevel(8,300.3904);
   qMap_Ag_C0_V0->SetContourLevel(9,337.9392);
   qMap_Ag_C0_V0->SetContourLevel(10,375.488);
   qMap_Ag_C0_V0->SetContourLevel(11,413.0368);
   qMap_Ag_C0_V0->SetContourLevel(12,450.5856);
   qMap_Ag_C0_V0->SetContourLevel(13,488.1344);
   qMap_Ag_C0_V0->SetContourLevel(14,525.6832);
   qMap_Ag_C0_V0->SetContourLevel(15,563.232);
   qMap_Ag_C0_V0->SetContourLevel(16,600.7808);
   qMap_Ag_C0_V0->SetContourLevel(17,638.3296);
   qMap_Ag_C0_V0->SetContourLevel(18,675.8784);
   qMap_Ag_C0_V0->SetContourLevel(19,713.4272);

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
