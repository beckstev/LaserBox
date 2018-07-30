{
//=========Macro generated from canvas: Canvas_1/Canvas_1
//=========  (Mon Jul 30 10:28:20 2018) by ROOT version5.34/36
   TCanvas *Canvas_1 = new TCanvas("Canvas_1", "Canvas_1",805,156,538,321);
   gStyle->SetOptStat(0);
   Canvas_1->SetHighLightColor(2);
   Canvas_1->Range(-32,-220.7625,288,1986.863);
   Canvas_1->SetFillColor(0);
   Canvas_1->SetBorderMode(0);
   Canvas_1->SetBorderSize(2);
   Canvas_1->SetFrameBorderMode(0);
   Canvas_1->SetFrameBorderMode(0);
   
   TH1D *dist_thr_scurveVcal_Vcal_C0_V0 = new TH1D("dist_thr_scurveVcal_Vcal_C0_V0","dist_thr_scurveVcal_Vcal_C0_V0",256,0,256);
   dist_thr_scurveVcal_Vcal_C0_V0->SetBinContent(0,2);
   dist_thr_scurveVcal_Vcal_C0_V0->SetBinContent(1,3);
   dist_thr_scurveVcal_Vcal_C0_V0->SetBinContent(29,2);
   dist_thr_scurveVcal_Vcal_C0_V0->SetBinContent(30,1);
   dist_thr_scurveVcal_Vcal_C0_V0->SetBinContent(31,4);
   dist_thr_scurveVcal_Vcal_C0_V0->SetBinContent(32,6);
   dist_thr_scurveVcal_Vcal_C0_V0->SetBinContent(33,10);
   dist_thr_scurveVcal_Vcal_C0_V0->SetBinContent(34,247);
   dist_thr_scurveVcal_Vcal_C0_V0->SetBinContent(35,1584);
   dist_thr_scurveVcal_Vcal_C0_V0->SetBinContent(36,1682);
   dist_thr_scurveVcal_Vcal_C0_V0->SetBinContent(37,584);
   dist_thr_scurveVcal_Vcal_C0_V0->SetBinContent(38,33);
   dist_thr_scurveVcal_Vcal_C0_V0->SetBinContent(39,1);
   dist_thr_scurveVcal_Vcal_C0_V0->SetBinContent(40,1);
   dist_thr_scurveVcal_Vcal_C0_V0->SetEntries(4160);
   dist_thr_scurveVcal_Vcal_C0_V0->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   dist_thr_scurveVcal_Vcal_C0_V0->SetLineColor(ci);
   dist_thr_scurveVcal_Vcal_C0_V0->GetXaxis()->SetLabelFont(42);
   dist_thr_scurveVcal_Vcal_C0_V0->GetXaxis()->SetLabelSize(0.035);
   dist_thr_scurveVcal_Vcal_C0_V0->GetXaxis()->SetTitleSize(0.035);
   dist_thr_scurveVcal_Vcal_C0_V0->GetXaxis()->SetTitleFont(42);
   dist_thr_scurveVcal_Vcal_C0_V0->GetYaxis()->SetLabelFont(42);
   dist_thr_scurveVcal_Vcal_C0_V0->GetYaxis()->SetLabelSize(0.035);
   dist_thr_scurveVcal_Vcal_C0_V0->GetYaxis()->SetTitleSize(0.035);
   dist_thr_scurveVcal_Vcal_C0_V0->GetYaxis()->SetTitleFont(42);
   dist_thr_scurveVcal_Vcal_C0_V0->GetZaxis()->SetLabelFont(42);
   dist_thr_scurveVcal_Vcal_C0_V0->GetZaxis()->SetLabelSize(0.035);
   dist_thr_scurveVcal_Vcal_C0_V0->GetZaxis()->SetTitleSize(0.035);
   dist_thr_scurveVcal_Vcal_C0_V0->GetZaxis()->SetTitleFont(42);
   dist_thr_scurveVcal_Vcal_C0_V0->Draw("");
   
   TPaveText *pt = new TPaveText(0.2549254,0.9310502,0.7450746,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *text = pt->AddText("dist_thr_scurveVcal_Vcal_C0_V0");
   pt->Draw();
   Canvas_1->Modified();
   Canvas_1->cd();
   Canvas_1->SetSelected(Canvas_1);
}
