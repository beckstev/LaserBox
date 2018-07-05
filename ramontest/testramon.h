#ifndef PIXTESTRAMON_H
#define PIXTESTRAMON_H

#include "PixTest.hh"

class DLLEXPORT PixTestRamon: public Pixtest {
public:
    PixTestRamon(PixSetup *, std::string);
    PixTestRamon();
    virtual bool setParameter(std::string parName,std::string sval);
    void init();
    void bookHist(std::string);

    void ramonTest();

    void doTest();

private:

    int fParFirstPar;

    ClassDef(PixTestRamon,1)
};