#include "../steven_test_analyse/Gaus2D.h"
#include <iostream>
#include <vector>
#include <fstream>
#include <iterator>
#include <string>
#include "TMath.h"


using namespace std;

void root_6_fit_laser_test(){

 //----------------------- Please fill in here the data of pxar, starting with TProfile2D ----------------




 //------ end data input ----------------




 //---------------------- Create Fitfunction and set parameters  ---------------------------------------------------

  TF2 *g2D =new TF2("g2d",Gaus2D,0,50,0,80,5);
  g2D -> SetParNames("Amplitude","X_{0}","#sigma_{x}","Y_{0}","#sigma_{y}");
  
  g2D -> SetParameters(200,30,0.75, 46,1);

  //-------------------------------------------------------------------------------------


  //------------------------------ SAVE NAME OF File ----------------------------------------------

    string name;
    cout << '\n' << "Please, enter the name of folder/file: " << name << " \n";

    cin >> name ;
    cout << '\n' << "Name is defined as: " << name << " \n \n";



  //------------------------------ Fit Data -------------------------------------------------

  qMap_Ag_C0_V0 -> Fit("g2d", "N");

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
  fitted_function -> Draw("Surf,same"); // Cont3

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
