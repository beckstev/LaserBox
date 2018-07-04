#include <Gaus2D.h>
#include <iostream>
#include <vector>

using namespace std;

void twod_fit_root(){

  cout << "Running Skript" << "\n";

  TF2 *g2D=new TF2("g2d",Gaus2D,-10,10,-10,10,5);
  g2D->SetParNames("Const","X_{0}","#sigma_{x}","Y_{0}","#sigma_{y}");
  TH2F *h2= new TH2F ("h2", "TEST", 200, -5., 50., 200, -10., 50.);

  for( int i = 0; i< 20; i = i + 10){
    for ( int j = 0; j <8; j = j + 8){
      cout << i << " - "<< j << "\n";

      g2D->SetParameters(100,i,2,j,1.5);
      h2 -> FillRandom("g2d",3000);
      g2D->SetParameters(10,i-1,15,j+1,15);
      h2 -> FillRandom("g2d",7000);
    }
  }


  vector < float > data_bin;
  vector < pair< int, int> > cor_bin;

  for( int i = 0; i< 200; i++){
    for ( int j = 0; j < 200; j++){
        //cout << h2 -> GetBinContent(i,j)<< "\n";
        data_bin.push_back( h2 -> GetBinContent(i,j) );
        cor_bin.push_back( make_pair( i,j) ) ;
      }
    }
  double max = *max_element(data_bin.begin(), data_bin.end());
  float test_jop =  find(data_bin.begin(),data_bin.end(), max) - data_bin.begin();
  cout << "Hier" << test_jop << "\n";
  //int pos = std::distance( data_bin.begin(), ( find(data_bin.begin(),data_bin.end(), max) ) ) ;
    //int pos = std::distance( data_bin.begin(), data_bin.end() ) ;

  cout << max << " ist am xbin: "  << cor_bin[test_jop].first << " und am ybin: " << cor_bin[test_jop].second;
  h2 -> Fill(52., 35., 30.);

  //for (Int_t i=0;i<h2.GetSize();i++) data_bin[i] = h2[i];

  //cout << data_bin

  //g2D->Draw("surf");



  //h2 -> FillRandom("g2d",500000);


  //h2->Fit("g2d");

  //g2D->Draw("surf");
  h2 -> Draw("lego2, same");
  //gStyle->SetPalette(1);



  return 1;
}
