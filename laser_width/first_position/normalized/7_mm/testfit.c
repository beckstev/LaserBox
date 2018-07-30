void testfit(TString dataname){
    
    //********************************************************************
    //**************************IMPORT DATA*******************************
    //********************************************************************
    
    TFile *f = new TFile(dataname);

    TString filename = f->GetName();

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
    h_NLaserProfile1DX->SetTitle(filename);

    TH1D *h_NLaserProfile1DY = h_NLaserProfile2D->ProjectionY();
    h_NLaserProfile1DY->SetName("Row projection");
    h_NLaserProfile1DY->SetTitle(filename);
    

    TF1 *g_NLaserProfile1DX = new TF1("g_NLaserProfile1DX","gaus",18,26);
    TF1 *g_NLaserProfile1DY = new TF1("g_NLaserProfile1DY","gaus",40,52);

    g_NLaserProfile1DX->SetNpx(10000);
    g_NLaserProfile1DY->SetNpx(10000);
    //********************************************************************
    //*******************************FIT**********************************
    //********************************************************************

    h_NLaserProfile1DX->Fit("g_NLaserProfile1DX");
    h_NLaserProfile1DY->Fit("g_NLaserProfile1DY");

    //********************************************************************
    //*****************************DRAWING********************************
    //********************************************************************

    TCanvas *c1 = new TCanvas("c1","c1",200,10,1200,500);

    c1->SetFillColor(38);

    TPad *pad1=new TPad("pad1","Pad with X projection",0.03,0.03,0.48,0.97,0);
    TPad *pad2=new TPad("pad2","Pad with Y projection",0.52,0.03,0.97,0.97,0);

    pad1->Draw();
    pad2->Draw();

    pad1->cd();
    gStyle->SetOptStat(0);

    TAxis *a_xXProj = h_NLaserProfile1DX->GetXaxis();
    a_xXProj->SetTitle("Column");

    TAxis *a_yXProj = h_NLaserProfile1DX->GetYaxis();
    a_yXProj->SetTitle("Normalized V_{cal}");

    h_NLaserProfile1DX->Draw();

    pad2->cd();
    gStyle->SetOptStat(0);

    TAxis *a_xYProj = h_NLaserProfile1DY->GetXaxis();
    a_xYProj->SetTitle("Row");

    TAxis *a_yYProj = h_NLaserProfile1DY->GetYaxis();
    a_yYProj->SetTitle("Normalized V_{cal}");

    h_NLaserProfile1DY->Draw();

    c1->Update();

    c1->SaveAs("projectionfit.pdf");

}