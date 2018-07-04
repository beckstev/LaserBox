#include <Gaus2D.h>
#include <iostream>
#include <vector>

using namespace std;

void test(){

  cout << "Running Skript" << "\n";

  TF2 *g2D=new TF2("g2d",Gaus2D,-10,10,-10,10,5);
  g2D->SetParNames("Const","X_{0}","#sigma_{x}","Y_{0}","#sigma_{y}");
  TH2F *h2= new TH2F ("h2", "TEST", 75 , 0., 10., 75, 0., 10.);

  for( int i = 0; i< 10; i = i + 5){
    for ( int j = 0; j <10; j = j + 5){
      cout << i << " - "<< j << "\n";

      g2D->SetParameters(50,i,1,j,0.5);
      h2 -> FillRandom("g2d",300);
      g2D->SetParameters(10,i-1,10,j+1,100);
      h2 -> FillRandom("g2d",300);
    }
  }


  vector < float > data_bin;
  vector < pair< int, int> > cor_bin;

  for( int i = 0; i< 75; i++){
    for ( int j = 0; j < 75; j++){
        //cout << h2 -> GetBinContent(i,j)<< "\n";
        data_bin.push_back( h2 -> GetBinContent(i,j) );
        cor_bin.push_back( make_pair( i,j) ) ;
        cout << "Inhalt: " <<  h2 ->GetBinContent(i,j) << " in der bin " << i << " , " << j << "\n";

      }
    }
  double max = *max_element(data_bin.begin(), data_bin.end());
  float test_jop =  find(data_bin.begin(),data_bin.end(), max) - data_bin.begin();
  float test_bin =  *find(data_bin.begin(),data_bin.end(), max);

  cout << "Hier" << test_jop << "TESTBIN" << test_bin << "\n";
  //int pos = std::distance( data_bin.begin(), ( find(data_bin.begin(),data_bin.end(), max) ) ) ;
    //int pos = std::distance( data_bin.begin(), data_bin.end() ) ;

  cout << max << " ist am xbin: "  << cor_bin[test_jop].first << " und am ybin: " << cor_bin[test_jop].second;
  h2 -> AddBinContent(test_bin, 15.);

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
