#include<fstream>

void testfit(TString dataname,Double_t height){
    
    //********************************************************************
    //**************************IMPORT DATA*******************************
    //********************************************************************
    
    TString filename = dataname+".root";

    TFile *f = new TFile(filename);

    TCanvas *c = (TCanvas*)f->Get("Canvas_1");
    TProfile2D *h_LaserProfile2D = (TProfile2D*)c->GetPrimitive("qMap_Ag_C0_V0");

    //********************************************************************
    //*************************NORMALIZE DATA*****************************
    //********************************************************************

    TProfile2D *h_NLaserProfile2D=(TProfile2D*)h_LaserProfile2D->Clone();
    h_NLaserProfile2D->SetName("h_NLaserProfile2D");

    Double_t norm=1/h_LaserProfile2D->Integral();

    h_NLaserProfile2D->Scale(norm);

    //********************************************************************
    //***************************PROJECTION*******************************
    //********************************************************************

    TH1D *h_NLaserProfile1DX = h_NLaserProfile2D->ProjectionX();
    h_NLaserProfile1DX->SetName("Column projection");
    h_NLaserProfile1DX->SetTitle(dataname);

    TH1D *h_NLaserProfile1DY = h_NLaserProfile2D->ProjectionY();
    h_NLaserProfile1DY->SetName("Row projection");
    h_NLaserProfile1DY->SetTitle(dataname);
    

    TF1 *g_NLaserProfile1DX = new TF1("g_NLaserProfile1DX","gaus",19,26);
    TF1 *g_NLaserProfile1DY = new TF1("g_NLaserProfile1DY","gaus",40,52);

    g_NLaserProfile1DX->SetNpx(10000);
    g_NLaserProfile1DY->SetNpx(10000);

    //********************************************************************
    //*******************************FIT**********************************
    //********************************************************************

    h_NLaserProfile1DX->Fit("g_NLaserProfile1DX","Q");
    h_NLaserProfile1DY->Fit("g_NLaserProfile1DY","Q");

    //********************************************************************
    //**************************SAVE PARAMETERS***************************
    //********************************************************************

    Double_t parX[3];
    Double_t parY[3];

    g_NLaserProfile1DX->GetParameters(parX);
    g_NLaserProfile1DY->GetParameters(parY);

    Double_t *errparX= new Double_t(3);
    Double_t *errparY= new Double_t(3);

    errparX =(Double_t*) g_NLaserProfile1DX->GetParErrors();
    errparY =(Double_t*) g_NLaserProfile1DY->GetParErrors();

    ofstream sigma("sigma.dat",ofstream::app);

    sigma <<height <<"\t" <<parX[2] <<"\t" <<errparX[2] <<"\t" <<parY[2] <<"\t" <<errparY[2]  <<endl;

    //********************************************************************
    //*****************************DRAWING********************************
    //********************************************************************

    TCanvas *c1 = new TCanvas("c1","c1",200,10,1200,500);

    c1->SetFillColor(38);

    TPad *pad1=new TPad("pad1","Pad with X projection",0.01,0.01,0.49,0.99,0);
    TPad *pad2=new TPad("pad2","Pad with Y projection",0.51,0.01,0.99,0.99,0);

    pad1->Draw();
    pad2->Draw();

    pad1->cd();
    gStyle->SetOptStat(1);
    gStyle->SetOptFit(1);

    TAxis *a_xXProj = h_NLaserProfile1DX->GetXaxis();
    a_xXProj->SetTitle("Column");
    a_xXProj->SetRange(19,26);

    TAxis *a_yXProj = h_NLaserProfile1DX->GetYaxis();
    a_yXProj->SetTitle("Normalized V_{cal}");

    h_NLaserProfile1DX->Draw();

    pad2->cd();
    gStyle->SetOptStat(0);
    gStyle->SetOptFit(1);

    TAxis *a_xYProj = h_NLaserProfile1DY->GetXaxis();
    a_xYProj->SetTitle("Row");
    a_xYProj->SetRange(40,52);

    TAxis *a_yYProj = h_NLaserProfile1DY->GetYaxis();
    a_yYProj->SetTitle("Normalized V_{cal}");

    h_NLaserProfile1DY->Draw();

    c1->Update();

    c1->SaveAs(dataname+".pdf");

}