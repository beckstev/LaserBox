#include "../../../steven_test_analyse/Gaus2D.h"
#include <iostream>
#include <vector>
#include <fstream>
#include <iterator>
#include <string>
#include "TMath.h"


using namespace std;

void data_projection(){

 //----------------------- Please fill in here the data of pxar, starting with TProfile2D ----------------
 TProfile2D *qMap_Ag_C0_V0 = new TProfile2D("qMap_Ag_C0_V0","qMap_Ag_C0 (V0)",52,0,52,80,0,80,0,0);
 qMap_Ag_C0_V0->SetBinEntries(2344,13);
 qMap_Ag_C0_V0->SetBinEntries(2345,3259);
 qMap_Ag_C0_V0->SetBinEntries(2398,14432);
 qMap_Ag_C0_V0->SetBinEntries(2399,14421);
 qMap_Ag_C0_V0->SetBinEntries(2400,12126);
 qMap_Ag_C0_V0->SetBinEntries(2451,14054);
 qMap_Ag_C0_V0->SetBinEntries(2452,30380);
 qMap_Ag_C0_V0->SetBinEntries(2453,32456);
 qMap_Ag_C0_V0->SetBinEntries(2454,14496);
 qMap_Ag_C0_V0->SetBinEntries(2455,3);
 qMap_Ag_C0_V0->SetBinEntries(2505,14405);
 qMap_Ag_C0_V0->SetBinEntries(2506,85997);
 qMap_Ag_C0_V0->SetBinEntries(2507,86887);
 qMap_Ag_C0_V0->SetBinEntries(2508,14652);
 qMap_Ag_C0_V0->SetBinEntries(2509,330);
 qMap_Ag_C0_V0->SetBinEntries(2559,13898);
 qMap_Ag_C0_V0->SetBinEntries(2560,82256);
 qMap_Ag_C0_V0->SetBinEntries(2561,92374);
 qMap_Ag_C0_V0->SetBinEntries(2562,14525);
 qMap_Ag_C0_V0->SetBinEntries(2563,1);
 qMap_Ag_C0_V0->SetBinEntries(2613,1);
 qMap_Ag_C0_V0->SetBinEntries(2614,15132);
 qMap_Ag_C0_V0->SetBinEntries(2615,17206);
 qMap_Ag_C0_V0->SetBinEntries(2616,14498);
 qMap_Ag_C0_V0->SetBinEntries(2668,2811);
 qMap_Ag_C0_V0->SetBinEntries(2669,5128);
 qMap_Ag_C0_V0->SetBinContent(2344,1217);
 qMap_Ag_C0_V0->SetBinContent(2345,249696);
 qMap_Ag_C0_V0->SetBinContent(2398,1593387);
 qMap_Ag_C0_V0->SetBinContent(2399,1609096);
 qMap_Ag_C0_V0->SetBinContent(2400,1039430);
 qMap_Ag_C0_V0->SetBinContent(2451,810094);
 qMap_Ag_C0_V0->SetBinContent(2452,6577174);
 qMap_Ag_C0_V0->SetBinContent(2453,6034978);
 qMap_Ag_C0_V0->SetBinContent(2454,1633967);
 qMap_Ag_C0_V0->SetBinContent(2455,240);
 qMap_Ag_C0_V0->SetBinContent(2505,1135827);
 qMap_Ag_C0_V0->SetBinContent(2506,1.828997e+07);
 qMap_Ag_C0_V0->SetBinContent(2507,2.851462e+07);
 qMap_Ag_C0_V0->SetBinContent(2508,2175345);
 qMap_Ag_C0_V0->SetBinContent(2509,27517);
 qMap_Ag_C0_V0->SetBinContent(2559,1189464);
 qMap_Ag_C0_V0->SetBinContent(2560,1.510106e+07);
 qMap_Ag_C0_V0->SetBinContent(2561,3.20364e+07);
 qMap_Ag_C0_V0->SetBinContent(2562,2030728);
 qMap_Ag_C0_V0->SetBinContent(2563,101);
 qMap_Ag_C0_V0->SetBinContent(2613,85);
 qMap_Ag_C0_V0->SetBinContent(2614,1870582);
 qMap_Ag_C0_V0->SetBinContent(2615,2440443);
 qMap_Ag_C0_V0->SetBinContent(2616,1281466);
 qMap_Ag_C0_V0->SetBinContent(2668,230173);
 qMap_Ag_C0_V0->SetBinContent(2669,397530);
 qMap_Ag_C0_V0->SetBinError(2344,340.1897);
 qMap_Ag_C0_V0->SetBinError(2345,4484.731);
 qMap_Ag_C0_V0->SetBinError(2398,13337.84);
 qMap_Ag_C0_V0->SetBinError(2399,13485.52);
 qMap_Ag_C0_V0->SetBinError(2400,66153.57);
 qMap_Ag_C0_V0->SetBinError(2451,6984.873);
 qMap_Ag_C0_V0->SetBinError(2452,430311.7);
 qMap_Ag_C0_V0->SetBinError(2453,322230.1);
 qMap_Ag_C0_V0->SetBinError(2454,13634.97);
 qMap_Ag_C0_V0->SetBinError(2455,139.9214);
 qMap_Ag_C0_V0->SetBinError(2505,9604.122);
 qMap_Ag_C0_V0->SetBinError(2506,531939.9);
 qMap_Ag_C0_V0->SetBinError(2507,846602.9);
 qMap_Ag_C0_V0->SetBinError(2508,18055.27);
 qMap_Ag_C0_V0->SetBinError(2509,1547.359);
 qMap_Ag_C0_V0->SetBinError(2559,10232.71);
 qMap_Ag_C0_V0->SetBinError(2560,595117.9);
 qMap_Ag_C0_V0->SetBinError(2561,981576.4);
 qMap_Ag_C0_V0->SetBinError(2562,16931.76);
 qMap_Ag_C0_V0->SetBinError(2563,101);
 qMap_Ag_C0_V0->SetBinError(2613,85);
 qMap_Ag_C0_V0->SetBinError(2614,15433.69);
 qMap_Ag_C0_V0->SetBinError(2615,19231.87);
 qMap_Ag_C0_V0->SetBinError(2616,10786.81);
 qMap_Ag_C0_V0->SetBinError(2668,4413.904);
 qMap_Ag_C0_V0->SetBinError(2669,5693.815);
 qMap_Ag_C0_V0->SetMinimum(0);
 qMap_Ag_C0_V0->SetEntries(595741);
 qMap_Ag_C0_V0->SetStats(0);
 qMap_Ag_C0_V0->SetContour(20);
 qMap_Ag_C0_V0->SetContourLevel(0,0);
 qMap_Ag_C0_V0->SetContourLevel(1,17.34059);
 qMap_Ag_C0_V0->SetContourLevel(2,34.68119);
 qMap_Ag_C0_V0->SetContourLevel(3,52.02178);
 qMap_Ag_C0_V0->SetContourLevel(4,69.36237);
 qMap_Ag_C0_V0->SetContourLevel(5,86.70297);
 qMap_Ag_C0_V0->SetContourLevel(6,104.0436);
 qMap_Ag_C0_V0->SetContourLevel(7,121.3842);
 qMap_Ag_C0_V0->SetContourLevel(8,138.7247);
 qMap_Ag_C0_V0->SetContourLevel(9,156.0653);
 qMap_Ag_C0_V0->SetContourLevel(10,173.4059);
 qMap_Ag_C0_V0->SetContourLevel(11,190.7465);
 qMap_Ag_C0_V0->SetContourLevel(12,208.0871);
 qMap_Ag_C0_V0->SetContourLevel(13,225.4277);
 qMap_Ag_C0_V0->SetContourLevel(14,242.7683);
 qMap_Ag_C0_V0->SetContourLevel(15,260.1089);
 qMap_Ag_C0_V0->SetContourLevel(16,277.4495);
 qMap_Ag_C0_V0->SetContourLevel(17,294.7901);
 qMap_Ag_C0_V0->SetContourLevel(18,312.1307);
 qMap_Ag_C0_V0->SetContourLevel(19,329.4713);

 Int_t ci;      // for color index setting
 TColor *color; // for color definition with alpha
 ci = TColor::GetColor("#000099");
 qMap_Ag_C0_V0->SetLineColor(ci);
 qMap_Ag_C0_V0->GetXaxis()->SetTitle("col");
 qMap_Ag_C0_V0->GetXaxis()->SetRange(15,31);
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







    string name;
    cout << '\n' << "Please, enter the name of folder/file: " << name << " \n";

    cin >> name ;
    cout << '\n' << "Name is defined as: " << name << " \n \n";


  //------------------------------------Save Fit Params into File: my_file.txt ---------------------------------------------

  string para_name_list[] = {"Const","X_{0}","sigma_{x}","Y_{0}","sigma_{y}"};

  ofstream outFile(name + "_fit_params.txt");
  for ( int i = 0; i < 5; i++){
      outFile <<  para_name_list[i] << ":  " << g2D -> GetParameter(i) << "  " << g2D -> GetParError(i) << "\n";
  }







}
