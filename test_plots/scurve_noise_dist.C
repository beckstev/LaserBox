{
//=========Macro generated from canvas: Canvas_1/Canvas_1
//=========  (Mon Jul 30 10:28:39 2018) by ROOT version5.34/36
   TCanvas *Canvas_1 = new TCanvas("Canvas_1", "Canvas_1",805,156,538,321);
   gStyle->SetOptStat(0);
   Canvas_1->SetHighLightColor(2);
   Canvas_1->Range(-0.7500001,-58.5375,6.75,526.8375);
   Canvas_1->SetFillColor(0);
   Canvas_1->SetBorderMode(0);
   Canvas_1->SetBorderSize(2);
   Canvas_1->SetFrameBorderMode(0);
   Canvas_1->SetFrameBorderMode(0);
   
   TH1D *dist_sig_scurveVcal_Vcal_C0_V0 = new TH1D("dist_sig_scurveVcal_Vcal_C0_V0","dist_sig_scurveVcal_Vcal_C0_V0",100,0,6);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(1,5);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(2,1);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(31,3);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(32,9);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(33,10);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(34,15);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(35,42);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(36,72);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(37,116);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(38,200);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(39,228);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(40,311);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(41,388);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(42,446);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(43,407);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(44,395);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(45,400);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(46,327);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(47,243);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(48,177);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(49,138);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(50,91);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(51,58);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(52,33);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(53,10);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(54,15);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(55,7);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(56,4);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(57,2);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(58,3);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(59,2);
   dist_sig_scurveVcal_Vcal_C0_V0->SetBinContent(62,2);
   dist_sig_scurveVcal_Vcal_C0_V0->SetEntries(4160);
   dist_sig_scurveVcal_Vcal_C0_V0->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   dist_sig_scurveVcal_Vcal_C0_V0->SetLineColor(ci);
   dist_sig_scurveVcal_Vcal_C0_V0->GetXaxis()->SetLabelFont(42);
   dist_sig_scurveVcal_Vcal_C0_V0->GetXaxis()->SetLabelSize(0.035);
   dist_sig_scurveVcal_Vcal_C0_V0->GetXaxis()->SetTitleSize(0.035);
   dist_sig_scurveVcal_Vcal_C0_V0->GetXaxis()->SetTitleFont(42);
   dist_sig_scurveVcal_Vcal_C0_V0->GetYaxis()->SetLabelFont(42);
   dist_sig_scurveVcal_Vcal_C0_V0->GetYaxis()->SetLabelSize(0.035);
   dist_sig_scurveVcal_Vcal_C0_V0->GetYaxis()->SetTitleSize(0.035);
   dist_sig_scurveVcal_Vcal_C0_V0->GetYaxis()->SetTitleFont(42);
   dist_sig_scurveVcal_Vcal_C0_V0->GetZaxis()->SetLabelFont(42);
   dist_sig_scurveVcal_Vcal_C0_V0->GetZaxis()->SetLabelSize(0.035);
   dist_sig_scurveVcal_Vcal_C0_V0->GetZaxis()->SetTitleSize(0.035);
   dist_sig_scurveVcal_Vcal_C0_V0->GetZaxis()->SetTitleFont(42);
   dist_sig_scurveVcal_Vcal_C0_V0->Draw("");
   
   TPaveText *pt = new TPaveText(0.2530597,0.9310502,0.7469403,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *text = pt->AddText("dist_sig_scurveVcal_Vcal_C0_V0");
   pt->Draw();
   Canvas_1->Modified();
   Canvas_1->cd();
   Canvas_1->SetSelected(Canvas_1);
}
