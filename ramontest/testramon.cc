#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <fstream>

#include <Tcolor.h>
#include <TStyle.h>
#include <TMarker.h>
#include <TStopwatch.h>
#include <bitset>

#include "PixTestPretest.hh"
#include "PixTestFactory.hh"
#include "timer.h"
#include "log.h"
#include "helper.h"
#include "PixUtil.hh"

using namespace std;
using namespace pxar;

ClassImp(PixTestRamon)

//---------------------------------------------------------------------
PixTestRamon::PixTestRamon(PixSetup *, std::string) : PixTest(a,name),fParFirstPar(1){
    PixTest::init();
    init();
    LOG(logINFO) << "";
    LOG(logDEBUG) << "PixTestRamon ctor(PixSetup &a, string, TGTab *)";
}


//---------------------------------------------------------------------
PixTestRamon::PixTestRamon(): PixTest(){
    LOG(logDEBUG) << "PixTestRamon ctor()";
}


//---------------------------------------------------------------------
bool PixTestRamon::setParameter(std::string parName, std::string sval){
    bool found(false);
    std::transform(parName.begin(),parName.end(),parName.begin(), ::tolower);
    for (unsigned int i =0; i<fParameters.size();++i){
        if (fParameters[i].first == parName){
            found = true;
            if(!parName.compare("firstpar")){
                fParFirstPar = atoi(sval.c_str());
            }
            break;
        }
    }
    return found;
}


//---------------------------------------------------------------------
void PixTestAlive::init(){
    LOG(logDEBUG) << "PixTestRamon::init()";
}


//---------------------------------------------------------------------
void PixTestRamon::doTest(){
    
    TStopwatch t;

    fDirectory->cd();
    PixTest::update();
    
    ramonTest();

    int seconds = t.RealTime();

    LOG(logINFO) << "PixTestRamon::doTest() done, duration: " << seconds << " seconds";

}

//---------------------------------------------------------------------
void PixTestRamon::ramonTest(){
    LOG(logINFO) << "We've entered ramonTest"
}