#include <Gaus2D.h>
#include <iostream>
#include <vector>

using namespace std;

void fit_laser_test(){

  TProfile2D *qMap_Ag_C0_V0 = new TProfile2D("qMap_Ag_C0_V0","qMap_Ag_C0 (V0)",52,0,52,80,0,80,0,0);
   qMap_Ag_C0_V0->SetBinEntries(2400,733);
   qMap_Ag_C0_V0->SetBinEntries(2401,7105);
   qMap_Ag_C0_V0->SetBinEntries(2453,5096);
   qMap_Ag_C0_V0->SetBinEntries(2454,9717);
   qMap_Ag_C0_V0->SetBinEntries(2455,9837);
   qMap_Ag_C0_V0->SetBinEntries(2507,9598);
   qMap_Ag_C0_V0->SetBinEntries(2508,11848);
   qMap_Ag_C0_V0->SetBinEntries(2509,20808);
   qMap_Ag_C0_V0->SetBinEntries(2510,9432);
   qMap_Ag_C0_V0->SetBinEntries(2560,853);
   qMap_Ag_C0_V0->SetBinEntries(2561,9785);
   qMap_Ag_C0_V0->SetBinEntries(2562,23462);
   qMap_Ag_C0_V0->SetBinEntries(2563,28394);
   qMap_Ag_C0_V0->SetBinEntries(2564,9716);
   qMap_Ag_C0_V0->SetBinEntries(2614,77);
   qMap_Ag_C0_V0->SetBinEntries(2615,9804);
   qMap_Ag_C0_V0->SetBinEntries(2616,22888);
   qMap_Ag_C0_V0->SetBinEntries(2617,29393);
   qMap_Ag_C0_V0->SetBinEntries(2618,9758);
   qMap_Ag_C0_V0->SetBinEntries(2668,5);
   qMap_Ag_C0_V0->SetBinEntries(2669,9712);
   qMap_Ag_C0_V0->SetBinEntries(2670,16749);
   qMap_Ag_C0_V0->SetBinEntries(2671,22220);
   qMap_Ag_C0_V0->SetBinEntries(2672,9610);
   qMap_Ag_C0_V0->SetBinEntries(2723,9538);
   qMap_Ag_C0_V0->SetBinEntries(2724,9788);
   qMap_Ag_C0_V0->SetBinEntries(2725,11084);
   qMap_Ag_C0_V0->SetBinEntries(2726,456);
   qMap_Ag_C0_V0->SetBinEntries(2778,3305);
   qMap_Ag_C0_V0->SetBinEntries(2779,9663);
   qMap_Ag_C0_V0->SetBinContent(2400,47862);
   qMap_Ag_C0_V0->SetBinContent(2401,438725);
   qMap_Ag_C0_V0->SetBinContent(2453,249594);
   qMap_Ag_C0_V0->SetBinContent(2454,1029442);
   qMap_Ag_C0_V0->SetBinContent(2455,1166986);
   qMap_Ag_C0_V0->SetBinContent(2507,714096);
   qMap_Ag_C0_V0->SetBinContent(2508,1549574);
   qMap_Ag_C0_V0->SetBinContent(2509,6444888);
   qMap_Ag_C0_V0->SetBinContent(2510,752772);
   qMap_Ag_C0_V0->SetBinContent(2560,49971);
   qMap_Ag_C0_V0->SetBinContent(2561,994347);
   qMap_Ag_C0_V0->SetBinContent(2562,3040452);
   qMap_Ag_C0_V0->SetBinContent(2563,1.094218e+07);
   qMap_Ag_C0_V0->SetBinContent(2564,1053058);
   qMap_Ag_C0_V0->SetBinContent(2614,4694);
   qMap_Ag_C0_V0->SetBinContent(2615,1041323);
   qMap_Ag_C0_V0->SetBinContent(2616,2721717);
   qMap_Ag_C0_V0->SetBinContent(2617,6269610);
   qMap_Ag_C0_V0->SetBinContent(2618,1065000);
   qMap_Ag_C0_V0->SetBinContent(2668,332);
   qMap_Ag_C0_V0->SetBinContent(2669,1008653);
   qMap_Ag_C0_V0->SetBinContent(2670,1813859);
   qMap_Ag_C0_V0->SetBinContent(2671,2868931);
   qMap_Ag_C0_V0->SetBinContent(2672,875766);
   qMap_Ag_C0_V0->SetBinContent(2723,674394);
   qMap_Ag_C0_V0->SetBinContent(2724,1122058);
   qMap_Ag_C0_V0->SetBinContent(2725,1397723);
   qMap_Ag_C0_V0->SetBinContent(2726,31430);
   qMap_Ag_C0_V0->SetBinContent(2778,221381);
   qMap_Ag_C0_V0->SetBinContent(2779,707946);
   qMap_Ag_C0_V0->SetBinError(2400,1806.116);
   qMap_Ag_C0_V0->SetBinError(2401,5376.694);
   qMap_Ag_C0_V0->SetBinError(2453,3621.021);
   qMap_Ag_C0_V0->SetBinError(2454,10483.87);
   qMap_Ag_C0_V0->SetBinError(2455,11856.83);
   qMap_Ag_C0_V0->SetBinError(2507,7402.717);
   qMap_Ag_C0_V0->SetBinError(2508,14697.92);
   qMap_Ag_C0_V0->SetBinError(2509,520307.8);
   qMap_Ag_C0_V0->SetBinError(2510,65919.97);
   qMap_Ag_C0_V0->SetBinError(2560,1748.791);
   qMap_Ag_C0_V0->SetBinError(2561,10148.99);
   qMap_Ag_C0_V0->SetBinError(2562,68900.29);
   qMap_Ag_C0_V0->SetBinError(2563,681426);
   qMap_Ag_C0_V0->SetBinError(2564,10722.43);
   qMap_Ag_C0_V0->SetBinError(2614,542.5643);
   qMap_Ag_C0_V0->SetBinError(2615,10601.38);
   qMap_Ag_C0_V0->SetBinError(2616,94741.69);
   qMap_Ag_C0_V0->SetBinError(2617,354059.4);
   qMap_Ag_C0_V0->SetBinError(2618,10795.46);
   qMap_Ag_C0_V0->SetBinError(2668,156.5056);
   qMap_Ag_C0_V0->SetBinError(2669,10295.15);
   qMap_Ag_C0_V0->SetBinError(2670,15963.3);
   qMap_Ag_C0_V0->SetBinError(2671,21055.23);
   qMap_Ag_C0_V0->SetBinError(2672,8982.085);
   qMap_Ag_C0_V0->SetBinError(2723,7207.981);
   qMap_Ag_C0_V0->SetBinError(2724,11372.22);
   qMap_Ag_C0_V0->SetBinError(2725,13629.01);
   qMap_Ag_C0_V0->SetBinError(2726,1497.774);
   qMap_Ag_C0_V0->SetBinError(2778,3972.776);
   qMap_Ag_C0_V0->SetBinError(2779,7329.19);
   qMap_Ag_C0_V0->SetMinimum(0);
   qMap_Ag_C0_V0->SetEntries(330434);
   qMap_Ag_C0_V0->SetStats(0);
   qMap_Ag_C0_V0->SetContour(20);
   qMap_Ag_C0_V0->SetContourLevel(0,0);
   qMap_Ag_C0_V0->SetContourLevel(1,19.26848);
   qMap_Ag_C0_V0->SetContourLevel(2,38.53696);
   qMap_Ag_C0_V0->SetContourLevel(3,57.80544);
   qMap_Ag_C0_V0->SetContourLevel(4,77.07392);
   qMap_Ag_C0_V0->SetContourLevel(5,96.34241);
   qMap_Ag_C0_V0->SetContourLevel(6,115.6109);
   qMap_Ag_C0_V0->SetContourLevel(7,134.8794);
   qMap_Ag_C0_V0->SetContourLevel(8,154.1478);
   qMap_Ag_C0_V0->SetContourLevel(9,173.4163);
   qMap_Ag_C0_V0->SetContourLevel(10,192.6848);
   qMap_Ag_C0_V0->SetContourLevel(11,211.9533);
   qMap_Ag_C0_V0->SetContourLevel(12,231.2218);
   qMap_Ag_C0_V0->SetContourLevel(13,250.4903);
   qMap_Ag_C0_V0->SetContourLevel(14,269.7587);
   qMap_Ag_C0_V0->SetContourLevel(15,289.0272);
   qMap_Ag_C0_V0->SetContourLevel(16,308.2957);
   qMap_Ag_C0_V0->SetContourLevel(17,327.5642);
   qMap_Ag_C0_V0->SetContourLevel(18,346.8327);
   qMap_Ag_C0_V0->SetContourLevel(19,366.1011);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   qMap_Ag_C0_V0->SetLineColor(ci);
   qMap_Ag_C0_V0->GetXaxis()->SetTitle("col");
   qMap_Ag_C0_V0->GetXaxis()->SetNdivisions(508);
   qMap_Ag_C0_V0->GetXaxis()->SetLabelFont(42);
   qMap_Ag_C0_V0->GetXaxis()->SetLabelSize(0.05);
   qMap_Ag_C0_V0->GetXaxis()->SetTitleSize(0.05);
   qMap_Ag_C0_V0->GetXaxis()->SetTitleOffset(1.1);
   qMap_Ag_C0_V0->GetXaxis()->SetTitleFont(42);
   qMap_Ag_C0_V0->GetYaxis()->SetTitle("row");
   qMap_Ag_C0_V0->GetYaxis()->SetLabelFont(42);
   qMap_Ag_C0_V0->GetYaxis()->SetLabelSize(0.05);
   qMap_Ag_C0_V0->GetYaxis()->SetTitleSize(0.05);
   qMap_Ag_C0_V0->GetYaxis()->SetTitleOffset(1.1);
   qMap_Ag_C0_V0->GetYaxis()->SetTitleFont(42);
   qMap_Ag_C0_V0->GetZaxis()->SetLabelFont(42);
   qMap_Ag_C0_V0->GetZaxis()->SetLabelSize(0.035);
   qMap_Ag_C0_V0->GetZaxis()->SetTitleSize(0.035);
   qMap_Ag_C0_V0->GetZaxis()->SetTitleFont(42);

  TF2 *g2D =new TF2("g2d",Gaus2D,0,50,0,80,5);
  g2D->SetParNames("Const","X_{0}","#sigma_{x}","Y_{0}","#sigma_{y}");
  g2d -> SetParameters(300,24,0.75, 46,1);
  //qMap_Ag_C0_V0 -> Fit("g2d");

  qMap_Ag_C0_V0 -> Fit("g2d" );

  //qMap_Ag_C0_V0->Draw("lego2");
  //g2D->Draw("surf,same");

  TH1D *projy = qMap_Ag_C0_V0 -> ProjectionY();
  //projy -> Draw();

  TH1D *projx = qMap_Ag_C0_V0 -> ProjectionX();
  Th1D -> Fit("gaus");
  projx -> Draw();




}
