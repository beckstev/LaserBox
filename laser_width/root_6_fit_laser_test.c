#include "../steven_test_analyse/Gaus2D.h"
#include <iostream>
#include <vector>
#include <fstream>
#include <iterator>
#include <string>

using namespace std;

void root_6_fit_laser_test(){

  TProfile2D *qMap_Ag_C0_V0 = new TProfile2D("qMap_Ag_C0_V0","qMap_Ag_C0 (V0)",52,0,52,80,0,80,0,0);
   qMap_Ag_C0_V0->SetBinEntries(2400,1805);
   qMap_Ag_C0_V0->SetBinEntries(2401,20038);
   qMap_Ag_C0_V0->SetBinEntries(2453,10035);
   qMap_Ag_C0_V0->SetBinEntries(2454,24380);
   qMap_Ag_C0_V0->SetBinEntries(2455,24829);
   qMap_Ag_C0_V0->SetBinEntries(2507,24281);
   qMap_Ag_C0_V0->SetBinEntries(2508,36796);
   qMap_Ag_C0_V0->SetBinEntries(2509,63999);
   qMap_Ag_C0_V0->SetBinEntries(2510,23506);
   qMap_Ag_C0_V0->SetBinEntries(2560,1138);
   qMap_Ag_C0_V0->SetBinEntries(2561,24327);
   qMap_Ag_C0_V0->SetBinEntries(2562,70785);
   qMap_Ag_C0_V0->SetBinEntries(2563,104072);
   qMap_Ag_C0_V0->SetBinEntries(2564,24321);
   qMap_Ag_C0_V0->SetBinEntries(2614,42);
   qMap_Ag_C0_V0->SetBinEntries(2615,24319);
   qMap_Ag_C0_V0->SetBinEntries(2616,62352);
   qMap_Ag_C0_V0->SetBinEntries(2617,106627);
   qMap_Ag_C0_V0->SetBinEntries(2618,24355);
   qMap_Ag_C0_V0->SetBinEntries(2668,3);
   qMap_Ag_C0_V0->SetBinEntries(2669,24327);
   qMap_Ag_C0_V0->SetBinEntries(2670,29270);
   qMap_Ag_C0_V0->SetBinEntries(2671,63074);
   qMap_Ag_C0_V0->SetBinEntries(2672,24329);
   qMap_Ag_C0_V0->SetBinEntries(2723,23915);
   qMap_Ag_C0_V0->SetBinEntries(2724,24347);
   qMap_Ag_C0_V0->SetBinEntries(2725,32215);
   qMap_Ag_C0_V0->SetBinEntries(2726,662);
   qMap_Ag_C0_V0->SetBinEntries(2778,5648);
   qMap_Ag_C0_V0->SetBinEntries(2779,24118);
   qMap_Ag_C0_V0->SetBinContent(2400,108547);
   qMap_Ag_C0_V0->SetBinContent(2401,1171634);
   qMap_Ag_C0_V0->SetBinContent(2453,466459);
   qMap_Ag_C0_V0->SetBinContent(2454,2485858);
   qMap_Ag_C0_V0->SetBinContent(2455,2822132);
   qMap_Ag_C0_V0->SetBinContent(2507,1722960);
   qMap_Ag_C0_V0->SetBinContent(2508,3832632);
   qMap_Ag_C0_V0->SetBinContent(2509,9201870);
   qMap_Ag_C0_V0->SetBinContent(2510,1569400);
   qMap_Ag_C0_V0->SetBinContent(2560,66070);
   qMap_Ag_C0_V0->SetBinContent(2561,2330156);
   qMap_Ag_C0_V0->SetBinContent(2562,7772975);
   qMap_Ag_C0_V0->SetBinContent(2563,1.659796e+07);
   qMap_Ag_C0_V0->SetBinContent(2564,2552461);
   qMap_Ag_C0_V0->SetBinContent(2614,2659);
   qMap_Ag_C0_V0->SetBinContent(2615,3044190);
   qMap_Ag_C0_V0->SetBinContent(2616,6955588);
   qMap_Ag_C0_V0->SetBinContent(2617,1.480304e+07);
   qMap_Ag_C0_V0->SetBinContent(2618,2604638);
   qMap_Ag_C0_V0->SetBinContent(2668,214);
   qMap_Ag_C0_V0->SetBinContent(2669,2413042);
   qMap_Ag_C0_V0->SetBinContent(2670,3832522);
   qMap_Ag_C0_V0->SetBinContent(2671,8291983);
   qMap_Ag_C0_V0->SetBinContent(2672,2143006);
   qMap_Ag_C0_V0->SetBinContent(2723,1494600);
   qMap_Ag_C0_V0->SetBinContent(2724,2678380);
   qMap_Ag_C0_V0->SetBinContent(2725,3358607);
   qMap_Ag_C0_V0->SetBinContent(2726,43058);
   qMap_Ag_C0_V0->SetBinContent(2778,355545);
   qMap_Ag_C0_V0->SetBinContent(2779,1695288);
   qMap_Ag_C0_V0->SetBinError(2400,2611.385);
   qMap_Ag_C0_V0->SetBinError(2401,8583.431);
   qMap_Ag_C0_V0->SetBinError(2453,4751.195);
   qMap_Ag_C0_V0->SetBinError(2454,15987.9);
   qMap_Ag_C0_V0->SetBinError(2455,18089.16);
   qMap_Ag_C0_V0->SetBinError(2507,11218.38);
   qMap_Ag_C0_V0->SetBinError(2508,21629.83);
   qMap_Ag_C0_V0->SetBinError(2509,430606.7);
   qMap_Ag_C0_V0->SetBinError(2510,10434.99);
   qMap_Ag_C0_V0->SetBinError(2560,1980.61);
   qMap_Ag_C0_V0->SetBinError(2561,15082.32);
   qMap_Ag_C0_V0->SetBinError(2562,163616.3);
   qMap_Ag_C0_V0->SetBinError(2563,616023.4);
   qMap_Ag_C0_V0->SetBinError(2564,16436.87);
   qMap_Ag_C0_V0->SetBinError(2614,413.9456);
   qMap_Ag_C0_V0->SetBinError(2615,197209.6);
   qMap_Ag_C0_V0->SetBinError(2616,246889.8);
   qMap_Ag_C0_V0->SetBinError(2617,384789.7);
   qMap_Ag_C0_V0->SetBinError(2618,16707.57);
   qMap_Ag_C0_V0->SetBinError(2668,123.9597);
   qMap_Ag_C0_V0->SetBinError(2669,15565.95);
   qMap_Ag_C0_V0->SetBinError(2670,23562.08);
   qMap_Ag_C0_V0->SetBinError(2671,279700.9);
   qMap_Ag_C0_V0->SetBinError(2672,13825.93);
   qMap_Ag_C0_V0->SetBinError(2723,10061.1);
   qMap_Ag_C0_V0->SetBinError(2724,17198.4);
   qMap_Ag_C0_V0->SetBinError(2725,20040.93);
   qMap_Ag_C0_V0->SetBinError(2726,1706.672);
   qMap_Ag_C0_V0->SetBinError(2778,4859.088);
   qMap_Ag_C0_V0->SetBinError(2779,11066.54);
   qMap_Ag_C0_V0->SetMinimum(0);
   qMap_Ag_C0_V0->SetEntries(923915);
   qMap_Ag_C0_V0->SetStats(0);
   qMap_Ag_C0_V0->SetContour(20);
   qMap_Ag_C0_V0->SetContourLevel(0,0);
   qMap_Ag_C0_V0->SetContourLevel(1,7.974265);
   qMap_Ag_C0_V0->SetContourLevel(2,15.94853);
   qMap_Ag_C0_V0->SetContourLevel(3,23.9228);
   qMap_Ag_C0_V0->SetContourLevel(4,31.89706);
   qMap_Ag_C0_V0->SetContourLevel(5,39.87133);
   qMap_Ag_C0_V0->SetContourLevel(6,47.84559);
   qMap_Ag_C0_V0->SetContourLevel(7,55.81986);
   qMap_Ag_C0_V0->SetContourLevel(8,63.79412);
   qMap_Ag_C0_V0->SetContourLevel(9,71.76839);
   qMap_Ag_C0_V0->SetContourLevel(10,79.74265);
   qMap_Ag_C0_V0->SetContourLevel(11,87.71692);
   qMap_Ag_C0_V0->SetContourLevel(12,95.69118);
   qMap_Ag_C0_V0->SetContourLevel(13,103.6655);
   qMap_Ag_C0_V0->SetContourLevel(14,111.6397);
   qMap_Ag_C0_V0->SetContourLevel(15,119.614);
   qMap_Ag_C0_V0->SetContourLevel(16,127.5882);
   qMap_Ag_C0_V0->SetContourLevel(17,135.5625);
   qMap_Ag_C0_V0->SetContourLevel(18,143.5368);
   qMap_Ag_C0_V0->SetContourLevel(19,151.511);

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
  g2D -> SetParNames("Amplitude","X_{0}","#sigma_{x}","Y_{0}","#sigma_{y}");
  g2D -> SetParameters(200,24,0.75, 46,1);
  //g2d->SetParLimits(3,0, 2)
  qMap_Ag_C0_V0->Draw("lego2");
  qMap_Ag_C0_V0 -> Fit("g2d");

  string para_name_list[] = {"Const","X_{0}","sigma_{x}","Y_{0}","sigma_{y}"};

  ofstream outFile("my_file.txt");
  for ( int i = 0; i < 5; i++){
      outFile <<  para_name_list[i] << ":  " << g2D -> GetParameter(i) << "  " << g2D -> GetParError(i) << "\n";
  }



  TH1D *projy = qMap_Ag_C0_V0 -> ProjectionY();
  //projy-> Fit("gaus");
  //projy -> Draw();

  TH1D *projx = qMap_Ag_C0_V0 -> ProjectionX();
  //projx-> Fit("gaus");
  //projx -> Draw();




}
