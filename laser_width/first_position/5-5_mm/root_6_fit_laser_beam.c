#include "../../../steven_test_analyse/Gaus2D.h"
#include <iostream>
#include <vector>
#include <fstream>
#include <iterator>
#include <string>
#include "TMath.h"


using namespace std;

void root_6_fit_laser_beam(){

 //----------------------- Please fill in here the data of pxar, starting with TProfile2D ----------------



 TProfile2D *qMap_Ag_C0_V0 = new TProfile2D("qMap_Ag_C0_V0","qMap_Ag_C0 (V0)",52,0,52,80,0,80,0,0);
 qMap_Ag_C0_V0->SetBinEntries(2344,1751);
 qMap_Ag_C0_V0->SetBinEntries(2345,13606);
 qMap_Ag_C0_V0->SetBinEntries(2346,3);
 qMap_Ag_C0_V0->SetBinEntries(2397,83);
 qMap_Ag_C0_V0->SetBinEntries(2398,14436);
 qMap_Ag_C0_V0->SetBinEntries(2399,14317);
 qMap_Ag_C0_V0->SetBinEntries(2400,14371);
 qMap_Ag_C0_V0->SetBinEntries(2451,14518);
 qMap_Ag_C0_V0->SetBinEntries(2452,55056);
 qMap_Ag_C0_V0->SetBinEntries(2453,57458);
 qMap_Ag_C0_V0->SetBinEntries(2454,14335);
 qMap_Ag_C0_V0->SetBinEntries(2455,1413);
 qMap_Ag_C0_V0->SetBinEntries(2505,14452);
 qMap_Ag_C0_V0->SetBinEntries(2506,89375);
 qMap_Ag_C0_V0->SetBinEntries(2507,84660);
 qMap_Ag_C0_V0->SetBinEntries(2508,19176);
 qMap_Ag_C0_V0->SetBinEntries(2509,6654);
 qMap_Ag_C0_V0->SetBinEntries(2559,14521);
 qMap_Ag_C0_V0->SetBinEntries(2560,80034);
 qMap_Ag_C0_V0->SetBinEntries(2561,90658);
 qMap_Ag_C0_V0->SetBinEntries(2562,17511);
 qMap_Ag_C0_V0->SetBinEntries(2563,62);
 qMap_Ag_C0_V0->SetBinEntries(2613,150);
 qMap_Ag_C0_V0->SetBinEntries(2614,17076);
 qMap_Ag_C0_V0->SetBinEntries(2615,36260);
 qMap_Ag_C0_V0->SetBinEntries(2616,14546);
 qMap_Ag_C0_V0->SetBinEntries(2668,10793);
 qMap_Ag_C0_V0->SetBinEntries(2669,13073);
 qMap_Ag_C0_V0->SetBinContent(2344,155344);
 qMap_Ag_C0_V0->SetBinContent(2345,1128042);
 qMap_Ag_C0_V0->SetBinContent(2346,275);
 qMap_Ag_C0_V0->SetBinContent(2397,4606);
 qMap_Ag_C0_V0->SetBinContent(2398,1711722);
 qMap_Ag_C0_V0->SetBinContent(2399,1836729);
 qMap_Ag_C0_V0->SetBinContent(2400,1408068);
 qMap_Ag_C0_V0->SetBinContent(2451,985426);
 qMap_Ag_C0_V0->SetBinContent(2452,6480075);
 qMap_Ag_C0_V0->SetBinContent(2453,9177472);
 qMap_Ag_C0_V0->SetBinContent(2454,1783801);
 qMap_Ag_C0_V0->SetBinContent(2455,114572);
 qMap_Ag_C0_V0->SetBinContent(2505,1367722);
 qMap_Ag_C0_V0->SetBinContent(2506,1.482972e+07);
 qMap_Ag_C0_V0->SetBinContent(2507,4.668824e+07);
 qMap_Ag_C0_V0->SetBinContent(2508,2599669);
 qMap_Ag_C0_V0->SetBinContent(2509,623834);
 qMap_Ag_C0_V0->SetBinContent(2559,1312394);
 qMap_Ag_C0_V0->SetBinContent(2560,1.394541e+07);
 qMap_Ag_C0_V0->SetBinContent(2561,1.95714e+07);
 qMap_Ag_C0_V0->SetBinContent(2562,6382667);
 qMap_Ag_C0_V0->SetBinContent(2563,5933);
 qMap_Ag_C0_V0->SetBinContent(2613,12218);
 qMap_Ag_C0_V0->SetBinContent(2614,2172727);
 qMap_Ag_C0_V0->SetBinContent(2615,3681722);
 qMap_Ag_C0_V0->SetBinContent(2616,1496081);
 qMap_Ag_C0_V0->SetBinContent(2668,829080);
 qMap_Ag_C0_V0->SetBinContent(2669,1165780);
 qMap_Ag_C0_V0->SetBinError(2344,3769.952);
 qMap_Ag_C0_V0->SetBinError(2345,9888.298);
 qMap_Ag_C0_V0->SetBinError(2346,159.54);
 qMap_Ag_C0_V0->SetBinError(2397,516.0407);
 qMap_Ag_C0_V0->SetBinError(2398,14276.88);
 qMap_Ag_C0_V0->SetBinError(2399,15418.18);
 qMap_Ag_C0_V0->SetBinError(2400,11864.88);
 qMap_Ag_C0_V0->SetBinError(2451,8326.981);
 qMap_Ag_C0_V0->SetBinError(2452,117610.6);
 qMap_Ag_C0_V0->SetBinError(2453,366432.5);
 qMap_Ag_C0_V0->SetBinError(2454,14962.44);
 qMap_Ag_C0_V0->SetBinError(2455,3103.91);
 qMap_Ag_C0_V0->SetBinError(2505,11494.87);
 qMap_Ag_C0_V0->SetBinError(2506,225151.8);
 qMap_Ag_C0_V0->SetBinError(2507,1398062);
 qMap_Ag_C0_V0->SetBinError(2508,19570.16);
 qMap_Ag_C0_V0->SetBinError(2509,7760.907);
 qMap_Ag_C0_V0->SetBinError(2559,11063.44);
 qMap_Ag_C0_V0->SetBinError(2560,565151.2);
 qMap_Ag_C0_V0->SetBinError(2561,481702.2);
 qMap_Ag_C0_V0->SetBinError(2562,524473.1);
 qMap_Ag_C0_V0->SetBinError(2563,762.9856);
 qMap_Ag_C0_V0->SetBinError(2613,1020.252);
 qMap_Ag_C0_V0->SetBinError(2614,17352.26);
 qMap_Ag_C0_V0->SetBinError(2615,21992.88);
 qMap_Ag_C0_V0->SetBinError(2616,12498.79);
 qMap_Ag_C0_V0->SetBinError(2668,8216.387);
 qMap_Ag_C0_V0->SetBinError(2669,10342.23);
 qMap_Ag_C0_V0->SetMinimum(0);
 qMap_Ag_C0_V0->SetEntries(710348);
 qMap_Ag_C0_V0->SetStats(0);
 qMap_Ag_C0_V0->SetContour(20);
 qMap_Ag_C0_V0->SetContourLevel(0,0);
 qMap_Ag_C0_V0->SetContourLevel(1,27.57397);
 qMap_Ag_C0_V0->SetContourLevel(2,55.14794);
 qMap_Ag_C0_V0->SetContourLevel(3,82.7219);
 qMap_Ag_C0_V0->SetContourLevel(4,110.2959);
 qMap_Ag_C0_V0->SetContourLevel(5,137.8698);
 qMap_Ag_C0_V0->SetContourLevel(6,165.4438);
 qMap_Ag_C0_V0->SetContourLevel(7,193.0178);
 qMap_Ag_C0_V0->SetContourLevel(8,220.5917);
 qMap_Ag_C0_V0->SetContourLevel(9,248.1657);
 qMap_Ag_C0_V0->SetContourLevel(10,275.7397);
 qMap_Ag_C0_V0->SetContourLevel(11,303.3137);
 qMap_Ag_C0_V0->SetContourLevel(12,330.8876);
 qMap_Ag_C0_V0->SetContourLevel(13,358.4616);
 qMap_Ag_C0_V0->SetContourLevel(14,386.0356);
 qMap_Ag_C0_V0->SetContourLevel(15,413.6095);
 qMap_Ag_C0_V0->SetContourLevel(16,441.1835);
 qMap_Ag_C0_V0->SetContourLevel(17,468.7575);
 qMap_Ag_C0_V0->SetContourLevel(18,496.3314);
 qMap_Ag_C0_V0->SetContourLevel(19,523.9054);

 Int_t ci;      // for color index setting
 TColor *color; // for color definition with alpha
 ci = TColor::GetColor("#000099");
 qMap_Ag_C0_V0->SetLineColor(ci);
 qMap_Ag_C0_V0->GetXaxis()->SetTitle("col");
 qMap_Ag_C0_V0->GetXaxis()->SetRange(16,31);
 qMap_Ag_C0_V0->GetXaxis()->SetNdivisions(508);
 qMap_Ag_C0_V0->GetXaxis()->SetLabelFont(42);
 qMap_Ag_C0_V0->GetXaxis()->SetLabelSize(0.05);
 qMap_Ag_C0_V0->GetXaxis()->SetTitleSize(0.05);
 qMap_Ag_C0_V0->GetXaxis()->SetTitleOffset(1.1);
 qMap_Ag_C0_V0->GetXaxis()->SetTitleFont(42);
 qMap_Ag_C0_V0->GetYaxis()->SetTitle("row");
 qMap_Ag_C0_V0->GetYaxis()->SetRange(30,60);
 qMap_Ag_C0_V0->GetYaxis()->SetLabelFont(42);
 qMap_Ag_C0_V0->GetYaxis()->SetLabelSize(0.05);
 qMap_Ag_C0_V0->GetYaxis()->SetTitleSize(0.05);
 qMap_Ag_C0_V0->GetYaxis()->SetTitleOffset(1.1);
 qMap_Ag_C0_V0->GetYaxis()->SetTitleFont(42);
 qMap_Ag_C0_V0->GetZaxis()->SetLabelFont(42);
 qMap_Ag_C0_V0->GetZaxis()->SetLabelSize(0.035);
 qMap_Ag_C0_V0->GetZaxis()->SetTitleSize(0.035);
 qMap_Ag_C0_V0->GetZaxis()->SetTitleFont(42);
 //------ end data input ----------------




 //---------------------- Create Fitfunction and set parameters  ---------------------------------------------------

  TF2 *g2D =new TF2("g2d",Gaus2D,0,50,0,80,5);
  g2D -> SetParNames("Amplitude","X_{0}","#sigma_{x}","Y_{0}","#sigma_{y}");

  g2D -> SetParameters(200,23,2, 47,2);

  //-------------------------------------------------------------------------------------


  //------------------------------ SAVE NAME OF File ----------------------------------------------

    string name;
    cout << '\n' << "Please, enter the name of folder/file: " << name << " \n";

    cin >> name ;
    cout << '\n' << "Name is defined as: " << name << " \n \n";



  //------------------------------ Fit Data -------------------------------------------------

  qMap_Ag_C0_V0 -> Fit("g2d");

  //-------------------------------------------------------------------------------------



  // ---------------------- Config Plot ------------------------------------------------

  // Z-Axis
  qMap_Ag_C0_V0 -> GetZaxis() -> SetTitle("Mean Vcal");
  qMap_Ag_C0_V0 -> GetZaxis() -> SetTitleOffset(1.2);


  //Y-Axis
  qMap_Ag_C0_V0 -> GetYaxis() -> SetTitleOffset(1.5);
  qMap_Ag_C0_V0 -> GetYaxis() -> SetLabelSize( qMap_Ag_C0_V0 -> GetZaxis() -> GetLabelSize() ); //Y-Axis
  qMap_Ag_C0_V0 -> GetYaxis() -> SetTitleSize( qMap_Ag_C0_V0 -> GetZaxis() -> GetTitleSize() ); //Y-Axis
  qMap_Ag_C0_V0 -> GetYaxis() -> SetRangeUser( g2D -> GetParameter(3) -10, g2D -> GetParameter(3) + 10);

  //X-Axis
  qMap_Ag_C0_V0 -> GetXaxis() -> SetTitleOffset(1.5);
  qMap_Ag_C0_V0 -> GetXaxis() -> SetRangeUser(g2D -> GetParameter(1) - 10, g2D -> GetParameter(1) + 10); // x-Axis
  qMap_Ag_C0_V0 -> GetXaxis() -> SetLabelSize( qMap_Ag_C0_V0 -> GetZaxis() -> GetLabelSize() ); //Y-Axis
  qMap_Ag_C0_V0 -> GetXaxis() -> SetTitleSize( qMap_Ag_C0_V0 -> GetZaxis() -> GetTitleSize() ); //Y-Axis


  // ------------------------------------------------------------------------------------



  //------------------------------------Save Fit Params into File: my_file.txt ---------------------------------------------

  string para_name_list[] = {"Const","X_{0}","sigma_{x}","Y_{0}","sigma_{y}"};

  ofstream outFile(name + "_fit_params.txt");
  for ( int i = 0; i < 5; i++){
      outFile <<  para_name_list[i] << ":  " << g2D -> GetParameter(i) << "  " << g2D -> GetParError(i) << "\n";
  }

  //-------------------------------------------------------------------------------------


  TGraph2D *fitted_function = new TGraph2D();
  double_t P = 6;
  double_t x,y,z;
  TRandom *r = new TRandom();
  cout << "Here I am " <<g2D -> GetParameter(3) << "\n";
  for (Int_t N=0; N < 2000; N++) {

      x = r -> Gaus(g2D -> GetParameter(1),  5 * g2D -> GetParameter(2) );
      y = r -> Gaus(g2D -> GetParameter(3),  5 * g2D -> GetParameter(4) );;
      double x_comp =  ( x -  (  g2D -> GetParameter(1) ) )  / ( TMath::Sqrt(2) *  g2D -> GetParameter(2) );
      double y_comp = ( y - ( g2D -> GetParameter(3) ) ) / ( TMath::Sqrt(2) * ( g2D -> GetParameter(4) ) ) ;

      z = (g2D -> GetParameter(0)) *  TMath::Exp( - ( x_comp * x_comp + y_comp * y_comp) );
      fitted_function -> SetPoint(N,x,y,z);
  }

  //---------------------- Plot ---------------------------------------------------
  TCanvas *c1 = new TCanvas("c1", "c1", 3840, 2160);
  qMap_Ag_C0_V0->Draw("Lego2"); // Cont0
  //fitted_function -> Draw("Surf,same"); // Cont3

  //-------------------------------------------------------------------------------------



  //---------------------- Set Legend ---------------------------------------------------

  auto legend = new TLegend(0.75,0.75,0.98,0.98);
  legend->AddEntry(qMap_Ag_C0_V0,"Pixel","f");
  legend->AddEntry(g2D,"2D Gaussian Fit","f");
  legend -> Draw();

  //-------------------------------------------------------------------------------------
  string plot_name = name + "_plot.pdf";

  c1 -> SaveAs( plot_name.c_str() );
  //fitted_function -> Draw("P,same");






}
