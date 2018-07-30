{
//=========Macro generated from canvas: Canvas_1_n41/Canvas_1_n41
//=========  (Mon Jul 30 10:23:15 2018) by ROOT version5.34/36
   TCanvas *Canvas_1_n41 = new TCanvas("Canvas_1_n41", "Canvas_1_n41",1378,528,538,321);
   gStyle->SetOptStat(0);
   Canvas_1_n41->SetHighLightColor(2);
   Canvas_1_n41->Range(20,-205.5375,50,1849.838);
   Canvas_1_n41->SetFillColor(0);
   Canvas_1_n41->SetBorderMode(0);
   Canvas_1_n41->SetBorderSize(2);
   Canvas_1_n41->SetFrameBorderMode(0);
   Canvas_1_n41->SetFrameBorderMode(0);
   
   TH1D *dist_thr_TrimThrFinal_vcal_C0_V0 = new TH1D("dist_thr_TrimThrFinal_vcal_C0_V0","dist_thr_TrimThrFinal_vcal_C0_V0",256,0,256);
   dist_thr_TrimThrFinal_vcal_C0_V0->SetBinContent(1,3);
   dist_thr_TrimThrFinal_vcal_C0_V0->SetBinContent(29,3);
   dist_thr_TrimThrFinal_vcal_C0_V0->SetBinContent(31,3);
   dist_thr_TrimThrFinal_vcal_C0_V0->SetBinContent(32,8);
   dist_thr_TrimThrFinal_vcal_C0_V0->SetBinContent(33,46);
   dist_thr_TrimThrFinal_vcal_C0_V0->SetBinContent(34,535);
   dist_thr_TrimThrFinal_vcal_C0_V0->SetBinContent(35,1566);
   dist_thr_TrimThrFinal_vcal_C0_V0->SetBinContent(36,1430);
   dist_thr_TrimThrFinal_vcal_C0_V0->SetBinContent(37,496);
   dist_thr_TrimThrFinal_vcal_C0_V0->SetBinContent(38,65);
   dist_thr_TrimThrFinal_vcal_C0_V0->SetBinContent(39,2);
   dist_thr_TrimThrFinal_vcal_C0_V0->SetBinContent(40,2);
   dist_thr_TrimThrFinal_vcal_C0_V0->SetBinContent(42,1);
   dist_thr_TrimThrFinal_vcal_C0_V0->SetEntries(4160);
   dist_thr_TrimThrFinal_vcal_C0_V0->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   dist_thr_TrimThrFinal_vcal_C0_V0->SetLineColor(ci);
   dist_thr_TrimThrFinal_vcal_C0_V0->GetXaxis()->SetTitle("Aktivierungsschwellwert / vcal");
   dist_thr_TrimThrFinal_vcal_C0_V0->GetXaxis()->SetRange(24,47);
   dist_thr_TrimThrFinal_vcal_C0_V0->GetXaxis()->SetLabelFont(42);
   dist_thr_TrimThrFinal_vcal_C0_V0->GetXaxis()->SetLabelSize(0.045);
   dist_thr_TrimThrFinal_vcal_C0_V0->GetXaxis()->SetTitleSize(0.055);
   dist_thr_TrimThrFinal_vcal_C0_V0->GetXaxis()->SetTitleOffset(0.9);
   dist_thr_TrimThrFinal_vcal_C0_V0->GetXaxis()->SetTitleFont(42);
   dist_thr_TrimThrFinal_vcal_C0_V0->GetYaxis()->SetTitle("Anzahl Pixel");
   dist_thr_TrimThrFinal_vcal_C0_V0->GetYaxis()->SetLabelFont(42);
   dist_thr_TrimThrFinal_vcal_C0_V0->GetYaxis()->SetLabelSize(0.045);
   dist_thr_TrimThrFinal_vcal_C0_V0->GetYaxis()->SetTitleSize(0.055);
   dist_thr_TrimThrFinal_vcal_C0_V0->GetYaxis()->SetTitleOffset(1.4);
   dist_thr_TrimThrFinal_vcal_C0_V0->GetYaxis()->SetTitleFont(42);
   dist_thr_TrimThrFinal_vcal_C0_V0->GetZaxis()->SetLabelFont(42);
   dist_thr_TrimThrFinal_vcal_C0_V0->GetZaxis()->SetLabelSize(0.035);
   dist_thr_TrimThrFinal_vcal_C0_V0->GetZaxis()->SetTitleSize(0.035);
   dist_thr_TrimThrFinal_vcal_C0_V0->GetZaxis()->SetTitleFont(42);
   dist_thr_TrimThrFinal_vcal_C0_V0->Draw("");
   
   TPaveText *pt = new TPaveText(0.2446642,0.9310502,0.7553358,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *text = pt->AddText("dist_thr_TrimThrFinal_vcal_C0_V0");
   pt->Draw();
   Canvas_1_n41->Modified();
   Canvas_1_n41->cd();
   Canvas_1_n41->SetSelected(Canvas_1_n41);
}
