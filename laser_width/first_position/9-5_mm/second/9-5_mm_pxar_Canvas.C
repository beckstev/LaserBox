{
//=========Macro generated from canvas: Canvas_1/Canvas_1
//=========  (Fri Jul 13 17:03:25 2018) by ROOT version5.34/36
   TCanvas *Canvas_1 = new TCanvas("Canvas_1", "Canvas_1",1334,317,538,321);
   gStyle->SetOptStat(0);
   Canvas_1->SetHighLightColor(2);
   Canvas_1->Range(-6.5,-10,58.5,90);
   Canvas_1->SetFillColor(0);
   Canvas_1->SetBorderMode(0);
   Canvas_1->SetBorderSize(2);
   Canvas_1->SetFrameBorderMode(0);
   Canvas_1->SetFrameBorderMode(0);
   
   TProfile2D *qMap_Ag_C0_V0 = new TProfile2D("qMap_Ag_C0_V0","qMap_Ag_C0 (V0)",52,0,52,80,0,80,0,0);
   qMap_Ag_C0_V0->SetBinEntries(2452,101849);
   qMap_Ag_C0_V0->SetBinEntries(2453,298);
   qMap_Ag_C0_V0->SetBinEntries(2505,9);
   qMap_Ag_C0_V0->SetBinEntries(2506,81618);
   qMap_Ag_C0_V0->SetBinEntries(2507,14874);
   qMap_Ag_C0_V0->SetBinEntries(2560,44844);
   qMap_Ag_C0_V0->SetBinContent(2452,1.25903e+08);
   qMap_Ag_C0_V0->SetBinContent(2453,16369);
   qMap_Ag_C0_V0->SetBinContent(2505,287);
   qMap_Ag_C0_V0->SetBinContent(2506,3.231088e+07);
   qMap_Ag_C0_V0->SetBinContent(2507,1736318);
   qMap_Ag_C0_V0->SetBinContent(2560,4235552);
   qMap_Ag_C0_V0->SetBinError(2452,2666979);
   qMap_Ag_C0_V0->SetBinError(2453,967.5614);
   qMap_Ag_C0_V0->SetBinError(2505,99.35291);
   qMap_Ag_C0_V0->SetBinError(2506,160867.6);
   qMap_Ag_C0_V0->SetBinError(2507,14363.19);
   qMap_Ag_C0_V0->SetBinError(2560,115756.3);
   qMap_Ag_C0_V0->SetMinimum(0);
   qMap_Ag_C0_V0->SetEntries(243492);
   qMap_Ag_C0_V0->SetStats(0);
   qMap_Ag_C0_V0->SetContour(20);
   qMap_Ag_C0_V0->SetContourLevel(0,0);
   qMap_Ag_C0_V0->SetContourLevel(1,61.80865);
   qMap_Ag_C0_V0->SetContourLevel(2,123.6173);
   qMap_Ag_C0_V0->SetContourLevel(3,185.4259);
   qMap_Ag_C0_V0->SetContourLevel(4,247.2346);
   qMap_Ag_C0_V0->SetContourLevel(5,309.0432);
   qMap_Ag_C0_V0->SetContourLevel(6,370.8519);
   qMap_Ag_C0_V0->SetContourLevel(7,432.6605);
   qMap_Ag_C0_V0->SetContourLevel(8,494.4692);
   qMap_Ag_C0_V0->SetContourLevel(9,556.2778);
   qMap_Ag_C0_V0->SetContourLevel(10,618.0865);
   qMap_Ag_C0_V0->SetContourLevel(11,679.8951);
   qMap_Ag_C0_V0->SetContourLevel(12,741.7038);
   qMap_Ag_C0_V0->SetContourLevel(13,803.5124);
   qMap_Ag_C0_V0->SetContourLevel(14,865.3211);
   qMap_Ag_C0_V0->SetContourLevel(15,927.1297);
   qMap_Ag_C0_V0->SetContourLevel(16,988.9384);
   qMap_Ag_C0_V0->SetContourLevel(17,1050.747);
   qMap_Ag_C0_V0->SetContourLevel(18,1112.556);
   qMap_Ag_C0_V0->SetContourLevel(19,1174.364);

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
