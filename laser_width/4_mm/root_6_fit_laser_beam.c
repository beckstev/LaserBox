#include "../../steven_test_analyse/Gaus2D.h"
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
   qMap_Ag_C0_V0->SetBinEntries(55,24887);
   qMap_Ag_C0_V0->SetBinEntries(56,415);
   qMap_Ag_C0_V0->SetBinEntries(57,265);
   qMap_Ag_C0_V0->SetBinEntries(58,111);
   qMap_Ag_C0_V0->SetBinEntries(59,150);
   qMap_Ag_C0_V0->SetBinEntries(60,111);
   qMap_Ag_C0_V0->SetBinEntries(61,305);
   qMap_Ag_C0_V0->SetBinEntries(62,92);
   qMap_Ag_C0_V0->SetBinEntries(63,102);
   qMap_Ag_C0_V0->SetBinEntries(64,290);
   qMap_Ag_C0_V0->SetBinEntries(65,280);
   qMap_Ag_C0_V0->SetBinEntries(66,182);
   qMap_Ag_C0_V0->SetBinEntries(67,5894);
   qMap_Ag_C0_V0->SetBinEntries(70,130);
   qMap_Ag_C0_V0->SetBinEntries(71,42);
   qMap_Ag_C0_V0->SetBinEntries(72,2);
   qMap_Ag_C0_V0->SetBinEntries(74,75);
   qMap_Ag_C0_V0->SetBinEntries(75,31);
   qMap_Ag_C0_V0->SetBinEntries(76,1);
   qMap_Ag_C0_V0->SetBinEntries(77,22);
   qMap_Ag_C0_V0->SetBinEntries(78,34);
   qMap_Ag_C0_V0->SetBinEntries(79,154);
   qMap_Ag_C0_V0->SetBinEntries(80,56);
   qMap_Ag_C0_V0->SetBinEntries(81,60);
   qMap_Ag_C0_V0->SetBinEntries(82,24);
   qMap_Ag_C0_V0->SetBinEntries(83,27);
   qMap_Ag_C0_V0->SetBinEntries(84,12);
   qMap_Ag_C0_V0->SetBinEntries(85,25);
   qMap_Ag_C0_V0->SetBinEntries(86,23);
   qMap_Ag_C0_V0->SetBinEntries(87,38);
   qMap_Ag_C0_V0->SetBinEntries(88,19);
   qMap_Ag_C0_V0->SetBinEntries(89,10);
   qMap_Ag_C0_V0->SetBinEntries(90,8);
   qMap_Ag_C0_V0->SetBinEntries(91,107);
   qMap_Ag_C0_V0->SetBinEntries(93,202);
   qMap_Ag_C0_V0->SetBinEntries(94,30);
   qMap_Ag_C0_V0->SetBinEntries(95,45);
   qMap_Ag_C0_V0->SetBinEntries(96,32);
   qMap_Ag_C0_V0->SetBinEntries(97,7);
   qMap_Ag_C0_V0->SetBinEntries(98,7);
   qMap_Ag_C0_V0->SetBinEntries(99,3);
   qMap_Ag_C0_V0->SetBinEntries(100,21);
   qMap_Ag_C0_V0->SetBinEntries(101,38);
   qMap_Ag_C0_V0->SetBinEntries(102,10);
   qMap_Ag_C0_V0->SetBinEntries(103,31);
   qMap_Ag_C0_V0->SetBinEntries(104,52);
   qMap_Ag_C0_V0->SetBinEntries(105,25);
   qMap_Ag_C0_V0->SetBinEntries(106,22848);
   qMap_Ag_C0_V0->SetBinEntries(109,116);
   qMap_Ag_C0_V0->SetBinEntries(163,332);
   qMap_Ag_C0_V0->SetBinEntries(217,416);
   qMap_Ag_C0_V0->SetBinEntries(268,43);
   qMap_Ag_C0_V0->SetBinEntries(271,493);
   qMap_Ag_C0_V0->SetBinEntries(322,31);
   qMap_Ag_C0_V0->SetBinEntries(325,187);
   qMap_Ag_C0_V0->SetBinEntries(376,86);
   qMap_Ag_C0_V0->SetBinEntries(379,612);
   qMap_Ag_C0_V0->SetBinEntries(430,79);
   qMap_Ag_C0_V0->SetBinEntries(433,58);
   qMap_Ag_C0_V0->SetBinEntries(484,19);
   qMap_Ag_C0_V0->SetBinEntries(487,106);
   qMap_Ag_C0_V0->SetBinEntries(538,65);
   qMap_Ag_C0_V0->SetBinEntries(541,52);
   qMap_Ag_C0_V0->SetBinEntries(595,140);
   qMap_Ag_C0_V0->SetBinEntries(646,61);
   qMap_Ag_C0_V0->SetBinEntries(649,182);
   qMap_Ag_C0_V0->SetBinEntries(700,92);
   qMap_Ag_C0_V0->SetBinEntries(703,232);
   qMap_Ag_C0_V0->SetBinEntries(754,27);
   qMap_Ag_C0_V0->SetBinEntries(757,259);
   qMap_Ag_C0_V0->SetBinEntries(808,18);
   qMap_Ag_C0_V0->SetBinEntries(811,497);
   qMap_Ag_C0_V0->SetBinEntries(862,97);
   qMap_Ag_C0_V0->SetBinEntries(865,82);
   qMap_Ag_C0_V0->SetBinEntries(916,69);
   qMap_Ag_C0_V0->SetBinEntries(919,5454);
   qMap_Ag_C0_V0->SetBinEntries(970,101);
   qMap_Ag_C0_V0->SetBinEntries(973,716);
   qMap_Ag_C0_V0->SetBinEntries(1024,53);
   qMap_Ag_C0_V0->SetBinEntries(1027,13);
   qMap_Ag_C0_V0->SetBinEntries(1078,72);
   qMap_Ag_C0_V0->SetBinEntries(1081,297);
   qMap_Ag_C0_V0->SetBinEntries(1132,114);
   qMap_Ag_C0_V0->SetBinEntries(1135,171);
   qMap_Ag_C0_V0->SetBinEntries(1186,50);
   qMap_Ag_C0_V0->SetBinEntries(1189,248);
   qMap_Ag_C0_V0->SetBinEntries(1240,9);
   qMap_Ag_C0_V0->SetBinEntries(1243,261);
   qMap_Ag_C0_V0->SetBinEntries(1294,51);
   qMap_Ag_C0_V0->SetBinEntries(1297,409);
   qMap_Ag_C0_V0->SetBinEntries(1348,59);
   qMap_Ag_C0_V0->SetBinEntries(1351,145);
   qMap_Ag_C0_V0->SetBinEntries(1402,33);
   qMap_Ag_C0_V0->SetBinEntries(1405,323);
   qMap_Ag_C0_V0->SetBinEntries(1456,31);
   qMap_Ag_C0_V0->SetBinEntries(1459,330);
   qMap_Ag_C0_V0->SetBinEntries(1510,111);
   qMap_Ag_C0_V0->SetBinEntries(1513,87);
   qMap_Ag_C0_V0->SetBinEntries(1564,193);
   qMap_Ag_C0_V0->SetBinEntries(1567,333);
   qMap_Ag_C0_V0->SetBinEntries(1618,173);
   qMap_Ag_C0_V0->SetBinEntries(1621,165);
   qMap_Ag_C0_V0->SetBinEntries(1672,21);
   qMap_Ag_C0_V0->SetBinEntries(1675,9312);
   qMap_Ag_C0_V0->SetBinEntries(1726,52);
   qMap_Ag_C0_V0->SetBinEntries(1729,184);
   qMap_Ag_C0_V0->SetBinEntries(1780,36);
   qMap_Ag_C0_V0->SetBinEntries(1783,111);
   qMap_Ag_C0_V0->SetBinEntries(1834,26);
   qMap_Ag_C0_V0->SetBinEntries(1837,608);
   qMap_Ag_C0_V0->SetBinEntries(1888,102);
   qMap_Ag_C0_V0->SetBinEntries(1891,476);
   qMap_Ag_C0_V0->SetBinEntries(1942,89);
   qMap_Ag_C0_V0->SetBinEntries(1945,108);
   qMap_Ag_C0_V0->SetBinEntries(1996,24);
   qMap_Ag_C0_V0->SetBinEntries(1999,99);
   qMap_Ag_C0_V0->SetBinEntries(2050,91);
   qMap_Ag_C0_V0->SetBinEntries(2053,127);
   qMap_Ag_C0_V0->SetBinEntries(2104,66);
   qMap_Ag_C0_V0->SetBinEntries(2107,348);
   qMap_Ag_C0_V0->SetBinEntries(2158,21);
   qMap_Ag_C0_V0->SetBinEntries(2161,614);
   qMap_Ag_C0_V0->SetBinEntries(2212,3);
   qMap_Ag_C0_V0->SetBinEntries(2215,410);
   qMap_Ag_C0_V0->SetBinEntries(2266,70);
   qMap_Ag_C0_V0->SetBinEntries(2269,192);
   qMap_Ag_C0_V0->SetBinEntries(2290,129);
   qMap_Ag_C0_V0->SetBinEntries(2291,1);
   qMap_Ag_C0_V0->SetBinEntries(2292,4);
   qMap_Ag_C0_V0->SetBinEntries(2320,40);
   qMap_Ag_C0_V0->SetBinEntries(2323,237);
   qMap_Ag_C0_V0->SetBinEntries(2343,1060);
   qMap_Ag_C0_V0->SetBinEntries(2344,24148);
   qMap_Ag_C0_V0->SetBinEntries(2345,24006);
   qMap_Ag_C0_V0->SetBinEntries(2346,285);
   qMap_Ag_C0_V0->SetBinEntries(2374,173);
   qMap_Ag_C0_V0->SetBinEntries(2377,310);
   qMap_Ag_C0_V0->SetBinEntries(2396,3126);
   qMap_Ag_C0_V0->SetBinEntries(2397,24110);
   qMap_Ag_C0_V0->SetBinEntries(2398,24187);
   qMap_Ag_C0_V0->SetBinEntries(2399,24200);
   qMap_Ag_C0_V0->SetBinEntries(2400,24031);
   qMap_Ag_C0_V0->SetBinEntries(2401,3);
   qMap_Ag_C0_V0->SetBinEntries(2428,79);
   qMap_Ag_C0_V0->SetBinEntries(2431,6225);
   qMap_Ag_C0_V0->SetBinEntries(2450,23562);
   qMap_Ag_C0_V0->SetBinEntries(2451,24050);
   qMap_Ag_C0_V0->SetBinEntries(2452,57420);
   qMap_Ag_C0_V0->SetBinEntries(2453,42983);
   qMap_Ag_C0_V0->SetBinEntries(2454,24135);
   qMap_Ag_C0_V0->SetBinEntries(2455,2615);
   qMap_Ag_C0_V0->SetBinEntries(2482,47);
   qMap_Ag_C0_V0->SetBinEntries(2485,182);
   qMap_Ag_C0_V0->SetBinEntries(2504,24068);
   qMap_Ag_C0_V0->SetBinEntries(2505,24948);
   qMap_Ag_C0_V0->SetBinEntries(2506,80389);
   qMap_Ag_C0_V0->SetBinEntries(2507,65610);
   qMap_Ag_C0_V0->SetBinEntries(2508,24694);
   qMap_Ag_C0_V0->SetBinEntries(2509,20006);
   qMap_Ag_C0_V0->SetBinEntries(2536,18);
   qMap_Ag_C0_V0->SetBinEntries(2539,9437);
   qMap_Ag_C0_V0->SetBinEntries(2558,24079);
   qMap_Ag_C0_V0->SetBinEntries(2559,28345);
   qMap_Ag_C0_V0->SetBinEntries(2560,74306);
   qMap_Ag_C0_V0->SetBinEntries(2561,74589);
   qMap_Ag_C0_V0->SetBinEntries(2562,25309);
   qMap_Ag_C0_V0->SetBinEntries(2563,6682);
   qMap_Ag_C0_V0->SetBinEntries(2590,119);
   qMap_Ag_C0_V0->SetBinEntries(2593,12151);
   qMap_Ag_C0_V0->SetBinEntries(2612,23987);
   qMap_Ag_C0_V0->SetBinEntries(2613,24191);
   qMap_Ag_C0_V0->SetBinEntries(2614,43465);
   qMap_Ag_C0_V0->SetBinEntries(2615,41817);
   qMap_Ag_C0_V0->SetBinEntries(2616,24124);
   qMap_Ag_C0_V0->SetBinEntries(2617,2328);
   qMap_Ag_C0_V0->SetBinEntries(2644,22);
   qMap_Ag_C0_V0->SetBinEntries(2647,88);
   qMap_Ag_C0_V0->SetBinEntries(2666,9836);
   qMap_Ag_C0_V0->SetBinEntries(2667,24063);
   qMap_Ag_C0_V0->SetBinEntries(2668,24179);
   qMap_Ag_C0_V0->SetBinEntries(2669,24215);
   qMap_Ag_C0_V0->SetBinEntries(2670,24077);
   qMap_Ag_C0_V0->SetBinEntries(2671,1);
   qMap_Ag_C0_V0->SetBinEntries(2698,29);
   qMap_Ag_C0_V0->SetBinEntries(2701,437);
   qMap_Ag_C0_V0->SetBinEntries(2720,43);
   qMap_Ag_C0_V0->SetBinEntries(2721,13046);
   qMap_Ag_C0_V0->SetBinEntries(2722,24056);
   qMap_Ag_C0_V0->SetBinEntries(2723,24033);
   qMap_Ag_C0_V0->SetBinEntries(2724,3608);
   qMap_Ag_C0_V0->SetBinEntries(2752,18);
   qMap_Ag_C0_V0->SetBinEntries(2755,320);
   qMap_Ag_C0_V0->SetBinEntries(2776,6);
   qMap_Ag_C0_V0->SetBinEntries(2777,15);
   qMap_Ag_C0_V0->SetBinEntries(2806,27);
   qMap_Ag_C0_V0->SetBinEntries(2809,5837);
   qMap_Ag_C0_V0->SetBinEntries(2860,11);
   qMap_Ag_C0_V0->SetBinEntries(2863,4784);
   qMap_Ag_C0_V0->SetBinEntries(2914,138);
   qMap_Ag_C0_V0->SetBinEntries(2917,303);
   qMap_Ag_C0_V0->SetBinEntries(2968,20);
   qMap_Ag_C0_V0->SetBinEntries(2971,8913);
   qMap_Ag_C0_V0->SetBinEntries(3022,6);
   qMap_Ag_C0_V0->SetBinEntries(3025,1210);
   qMap_Ag_C0_V0->SetBinEntries(3076,64);
   qMap_Ag_C0_V0->SetBinEntries(3079,11716);
   qMap_Ag_C0_V0->SetBinEntries(3130,18);
   qMap_Ag_C0_V0->SetBinEntries(3133,444);
   qMap_Ag_C0_V0->SetBinEntries(3184,31);
   qMap_Ag_C0_V0->SetBinEntries(3187,5423);
   qMap_Ag_C0_V0->SetBinEntries(3238,5);
   qMap_Ag_C0_V0->SetBinEntries(3241,426);
   qMap_Ag_C0_V0->SetBinEntries(3292,2192);
   qMap_Ag_C0_V0->SetBinEntries(3295,7623);
   qMap_Ag_C0_V0->SetBinEntries(3346,2155);
   qMap_Ag_C0_V0->SetBinEntries(3349,1477);
   qMap_Ag_C0_V0->SetBinEntries(3400,124);
   qMap_Ag_C0_V0->SetBinEntries(3403,5579);
   qMap_Ag_C0_V0->SetBinEntries(3454,88);
   qMap_Ag_C0_V0->SetBinEntries(3457,1446);
   qMap_Ag_C0_V0->SetBinEntries(3508,69);
   qMap_Ag_C0_V0->SetBinEntries(3511,415);
   qMap_Ag_C0_V0->SetBinEntries(3562,18);
   qMap_Ag_C0_V0->SetBinEntries(3565,6094);
   qMap_Ag_C0_V0->SetBinEntries(3616,10);
   qMap_Ag_C0_V0->SetBinEntries(3619,642);
   qMap_Ag_C0_V0->SetBinEntries(3670,3087);
   qMap_Ag_C0_V0->SetBinEntries(3673,5609);
   qMap_Ag_C0_V0->SetBinEntries(3724,12);
   qMap_Ag_C0_V0->SetBinEntries(3727,9364);
   qMap_Ag_C0_V0->SetBinEntries(3778,7);
   qMap_Ag_C0_V0->SetBinEntries(3781,1812);
   qMap_Ag_C0_V0->SetBinEntries(3832,1591);
   qMap_Ag_C0_V0->SetBinEntries(3835,7419);
   qMap_Ag_C0_V0->SetBinEntries(3886,35);
   qMap_Ag_C0_V0->SetBinEntries(3889,4928);
   qMap_Ag_C0_V0->SetBinEntries(3940,7);
   qMap_Ag_C0_V0->SetBinEntries(3943,9517);
   qMap_Ag_C0_V0->SetBinEntries(3994,21);
   qMap_Ag_C0_V0->SetBinEntries(3997,585);
   qMap_Ag_C0_V0->SetBinEntries(4048,8);
   qMap_Ag_C0_V0->SetBinEntries(4102,13);
   qMap_Ag_C0_V0->SetBinEntries(4105,1218);
   qMap_Ag_C0_V0->SetBinEntries(4156,102);
   qMap_Ag_C0_V0->SetBinEntries(4159,5594);
   qMap_Ag_C0_V0->SetBinEntries(4210,863);
   qMap_Ag_C0_V0->SetBinEntries(4213,422);
   qMap_Ag_C0_V0->SetBinEntries(4264,24);
   qMap_Ag_C0_V0->SetBinEntries(4267,11763);
   qMap_Ag_C0_V0->SetBinEntries(4318,4);
   qMap_Ag_C0_V0->SetBinEntries(4321,60);
   qMap_Ag_C0_V0->SetBinEntries(4372,5);
   qMap_Ag_C0_V0->SetBinContent(55,2930958);
   qMap_Ag_C0_V0->SetBinContent(56,37664);
   qMap_Ag_C0_V0->SetBinContent(57,31057);
   qMap_Ag_C0_V0->SetBinContent(58,11952);
   qMap_Ag_C0_V0->SetBinContent(59,17626);
   qMap_Ag_C0_V0->SetBinContent(60,12143);
   qMap_Ag_C0_V0->SetBinContent(61,36454);
   qMap_Ag_C0_V0->SetBinContent(62,10168);
   qMap_Ag_C0_V0->SetBinContent(63,12105);
   qMap_Ag_C0_V0->SetBinContent(64,31178);
   qMap_Ag_C0_V0->SetBinContent(65,31374);
   qMap_Ag_C0_V0->SetBinContent(66,19394);
   qMap_Ag_C0_V0->SetBinContent(67,629502);
   qMap_Ag_C0_V0->SetBinContent(70,12838);
   qMap_Ag_C0_V0->SetBinContent(71,4501);
   qMap_Ag_C0_V0->SetBinContent(72,181);
   qMap_Ag_C0_V0->SetBinContent(74,8139);
   qMap_Ag_C0_V0->SetBinContent(75,3210);
   qMap_Ag_C0_V0->SetBinContent(76,81);
   qMap_Ag_C0_V0->SetBinContent(77,2323);
   qMap_Ag_C0_V0->SetBinContent(78,3266);
   qMap_Ag_C0_V0->SetBinContent(79,15776);
   qMap_Ag_C0_V0->SetBinContent(80,5446);
   qMap_Ag_C0_V0->SetBinContent(81,6216);
   qMap_Ag_C0_V0->SetBinContent(82,2574);
   qMap_Ag_C0_V0->SetBinContent(83,2916);
   qMap_Ag_C0_V0->SetBinContent(84,1059);
   qMap_Ag_C0_V0->SetBinContent(85,2653);
   qMap_Ag_C0_V0->SetBinContent(86,2224);
   qMap_Ag_C0_V0->SetBinContent(87,3856);
   qMap_Ag_C0_V0->SetBinContent(88,1731);
   qMap_Ag_C0_V0->SetBinContent(89,951);
   qMap_Ag_C0_V0->SetBinContent(90,813);
   qMap_Ag_C0_V0->SetBinContent(91,9006);
   qMap_Ag_C0_V0->SetBinContent(93,15574);
   qMap_Ag_C0_V0->SetBinContent(94,2801);
   qMap_Ag_C0_V0->SetBinContent(95,3957);
   qMap_Ag_C0_V0->SetBinContent(96,2916);
   qMap_Ag_C0_V0->SetBinContent(97,658);
   qMap_Ag_C0_V0->SetBinContent(98,718);
   qMap_Ag_C0_V0->SetBinContent(99,308);
   qMap_Ag_C0_V0->SetBinContent(100,1775);
   qMap_Ag_C0_V0->SetBinContent(101,3682);
   qMap_Ag_C0_V0->SetBinContent(102,979);
   qMap_Ag_C0_V0->SetBinContent(103,2895);
   qMap_Ag_C0_V0->SetBinContent(104,5040);
   qMap_Ag_C0_V0->SetBinContent(105,2027);
   qMap_Ag_C0_V0->SetBinContent(106,2388918);
   qMap_Ag_C0_V0->SetBinContent(109,8556);
   qMap_Ag_C0_V0->SetBinContent(163,154366);
   qMap_Ag_C0_V0->SetBinContent(217,29211);
   qMap_Ag_C0_V0->SetBinContent(268,3423);
   qMap_Ag_C0_V0->SetBinContent(271,624518);
   qMap_Ag_C0_V0->SetBinContent(322,2193);
   qMap_Ag_C0_V0->SetBinContent(325,79704);
   qMap_Ag_C0_V0->SetBinContent(376,6244);
   qMap_Ag_C0_V0->SetBinContent(379,108030);
   qMap_Ag_C0_V0->SetBinContent(430,71624);
   qMap_Ag_C0_V0->SetBinContent(433,3755);
   qMap_Ag_C0_V0->SetBinContent(484,1617);
   qMap_Ag_C0_V0->SetBinContent(487,7963);
   qMap_Ag_C0_V0->SetBinContent(538,4983);
   qMap_Ag_C0_V0->SetBinContent(541,3844);
   qMap_Ag_C0_V0->SetBinContent(595,76210);
   qMap_Ag_C0_V0->SetBinContent(646,4576);
   qMap_Ag_C0_V0->SetBinContent(649,79578);
   qMap_Ag_C0_V0->SetBinContent(700,6801);
   qMap_Ag_C0_V0->SetBinContent(703,83560);
   qMap_Ag_C0_V0->SetBinContent(754,1798);
   qMap_Ag_C0_V0->SetBinContent(757,84078);
   qMap_Ag_C0_V0->SetBinContent(808,1269);
   qMap_Ag_C0_V0->SetBinContent(811,232998);
   qMap_Ag_C0_V0->SetBinContent(862,6726);
   qMap_Ag_C0_V0->SetBinContent(865,6628);
   qMap_Ag_C0_V0->SetBinContent(916,5330);
   qMap_Ag_C0_V0->SetBinContent(919,811014);
   qMap_Ag_C0_V0->SetBinContent(970,7544);
   qMap_Ag_C0_V0->SetBinContent(973,320162);
   qMap_Ag_C0_V0->SetBinContent(1024,3050);
   qMap_Ag_C0_V0->SetBinContent(1027,1266);
   qMap_Ag_C0_V0->SetBinContent(1078,5135);
   qMap_Ag_C0_V0->SetBinContent(1081,26737);
   qMap_Ag_C0_V0->SetBinContent(1132,8819);
   qMap_Ag_C0_V0->SetBinContent(1135,341478);
   qMap_Ag_C0_V0->SetBinContent(1186,3802);
   qMap_Ag_C0_V0->SetBinContent(1189,88344);
   qMap_Ag_C0_V0->SetBinContent(1240,666);
   qMap_Ag_C0_V0->SetBinContent(1243,284188);
   qMap_Ag_C0_V0->SetBinContent(1294,3481);
   qMap_Ag_C0_V0->SetBinContent(1297,100975);
   qMap_Ag_C0_V0->SetBinContent(1348,4668);
   qMap_Ag_C0_V0->SetBinContent(1351,78026);
   qMap_Ag_C0_V0->SetBinContent(1402,2458);
   qMap_Ag_C0_V0->SetBinContent(1405,91406);
   qMap_Ag_C0_V0->SetBinContent(1456,2331);
   qMap_Ag_C0_V0->SetBinContent(1459,28133);
   qMap_Ag_C0_V0->SetBinContent(1510,8676);
   qMap_Ag_C0_V0->SetBinContent(1513,72947);
   qMap_Ag_C0_V0->SetBinContent(1564,13666);
   qMap_Ag_C0_V0->SetBinContent(1567,27628);
   qMap_Ag_C0_V0->SetBinContent(1618,14030);
   qMap_Ag_C0_V0->SetBinContent(1621,144658);
   qMap_Ag_C0_V0->SetBinContent(1672,1477);
   qMap_Ag_C0_V0->SetBinContent(1675,892766);
   qMap_Ag_C0_V0->SetBinContent(1726,3978);
   qMap_Ag_C0_V0->SetBinContent(1729,15367);
   qMap_Ag_C0_V0->SetBinContent(1780,2649);
   qMap_Ag_C0_V0->SetBinContent(1783,75816);
   qMap_Ag_C0_V0->SetBinContent(1834,2002);
   qMap_Ag_C0_V0->SetBinContent(1837,56379);
   qMap_Ag_C0_V0->SetBinContent(1888,7930);
   qMap_Ag_C0_V0->SetBinContent(1891,303342);
   qMap_Ag_C0_V0->SetBinContent(1942,6619);
   qMap_Ag_C0_V0->SetBinContent(1945,75740);
   qMap_Ag_C0_V0->SetBinContent(1996,2123);
   qMap_Ag_C0_V0->SetBinContent(1999,74068);
   qMap_Ag_C0_V0->SetBinContent(2050,6849);
   qMap_Ag_C0_V0->SetBinContent(2053,11638);
   qMap_Ag_C0_V0->SetBinContent(2104,5510);
   qMap_Ag_C0_V0->SetBinContent(2107,31214);
   qMap_Ag_C0_V0->SetBinContent(2158,1628);
   qMap_Ag_C0_V0->SetBinContent(2161,119281);
   qMap_Ag_C0_V0->SetBinContent(2212,242);
   qMap_Ag_C0_V0->SetBinContent(2215,36593);
   qMap_Ag_C0_V0->SetBinContent(2266,5378);
   qMap_Ag_C0_V0->SetBinContent(2269,16496);
   qMap_Ag_C0_V0->SetBinContent(2290,12404);
   qMap_Ag_C0_V0->SetBinContent(2291,95);
   qMap_Ag_C0_V0->SetBinContent(2292,443);
   qMap_Ag_C0_V0->SetBinContent(2320,2919);
   qMap_Ag_C0_V0->SetBinContent(2323,22104);
   qMap_Ag_C0_V0->SetBinContent(2343,172122);
   qMap_Ag_C0_V0->SetBinContent(2344,3004378);
   qMap_Ag_C0_V0->SetBinContent(2345,2743623);
   qMap_Ag_C0_V0->SetBinContent(2346,30208);
   qMap_Ag_C0_V0->SetBinContent(2374,13770);
   qMap_Ag_C0_V0->SetBinContent(2377,27466);
   qMap_Ag_C0_V0->SetBinContent(2396,346551);
   qMap_Ag_C0_V0->SetBinContent(2397,2934166);
   qMap_Ag_C0_V0->SetBinContent(2398,3423285);
   qMap_Ag_C0_V0->SetBinContent(2399,3403149);
   qMap_Ag_C0_V0->SetBinContent(2400,2872200);
   qMap_Ag_C0_V0->SetBinContent(2401,359);
   qMap_Ag_C0_V0->SetBinContent(2428,6028);
   qMap_Ag_C0_V0->SetBinContent(2431,1443261);
   qMap_Ag_C0_V0->SetBinContent(2450,3231963);
   qMap_Ag_C0_V0->SetBinContent(2451,3766173);
   qMap_Ag_C0_V0->SetBinContent(2452,8301628);
   qMap_Ag_C0_V0->SetBinContent(2453,6031191);
   qMap_Ag_C0_V0->SetBinContent(2454,3026892);
   qMap_Ag_C0_V0->SetBinContent(2455,311195);
   qMap_Ag_C0_V0->SetBinContent(2482,3790);
   qMap_Ag_C0_V0->SetBinContent(2485,16001);
   qMap_Ag_C0_V0->SetBinContent(2504,3395604);
   qMap_Ag_C0_V0->SetBinContent(2505,4290276);
   qMap_Ag_C0_V0->SetBinContent(2506,1.238648e+07);
   qMap_Ag_C0_V0->SetBinContent(2507,1.056158e+07);
   qMap_Ag_C0_V0->SetBinContent(2508,3565770);
   qMap_Ag_C0_V0->SetBinContent(2509,2549861);
   qMap_Ag_C0_V0->SetBinContent(2536,1330);
   qMap_Ag_C0_V0->SetBinContent(2539,1063477);
   qMap_Ag_C0_V0->SetBinContent(2558,3580388);
   qMap_Ag_C0_V0->SetBinContent(2559,4752401);
   qMap_Ag_C0_V0->SetBinContent(2560,1.096443e+07);
   qMap_Ag_C0_V0->SetBinContent(2561,1.311046e+07);
   qMap_Ag_C0_V0->SetBinContent(2562,4014200);
   qMap_Ag_C0_V0->SetBinContent(2563,869358);
   qMap_Ag_C0_V0->SetBinContent(2590,8807);
   qMap_Ag_C0_V0->SetBinContent(2593,5308866);
   qMap_Ag_C0_V0->SetBinContent(2612,2962789);
   qMap_Ag_C0_V0->SetBinContent(2613,3856156);
   qMap_Ag_C0_V0->SetBinContent(2614,6441266);
   qMap_Ag_C0_V0->SetBinContent(2615,5943049);
   qMap_Ag_C0_V0->SetBinContent(2616,3232521);
   qMap_Ag_C0_V0->SetBinContent(2617,297473);
   qMap_Ag_C0_V0->SetBinContent(2644,1762);
   qMap_Ag_C0_V0->SetBinContent(2647,8214);
   qMap_Ag_C0_V0->SetBinContent(2666,1082408);
   qMap_Ag_C0_V0->SetBinContent(2667,2930276);
   qMap_Ag_C0_V0->SetBinContent(2668,3700455);
   qMap_Ag_C0_V0->SetBinContent(2669,3246995);
   qMap_Ag_C0_V0->SetBinContent(2670,2755806);
   qMap_Ag_C0_V0->SetBinContent(2671,166);
   qMap_Ag_C0_V0->SetBinContent(2698,67548);
   qMap_Ag_C0_V0->SetBinContent(2701,236993);
   qMap_Ag_C0_V0->SetBinContent(2720,4323);
   qMap_Ag_C0_V0->SetBinContent(2721,1795894);
   qMap_Ag_C0_V0->SetBinContent(2722,3084303);
   qMap_Ag_C0_V0->SetBinContent(2723,2763256);
   qMap_Ag_C0_V0->SetBinContent(2724,378713);
   qMap_Ag_C0_V0->SetBinContent(2752,1426);
   qMap_Ag_C0_V0->SetBinContent(2755,30021);
   qMap_Ag_C0_V0->SetBinContent(2776,494);
   qMap_Ag_C0_V0->SetBinContent(2777,1535);
   qMap_Ag_C0_V0->SetBinContent(2806,2006);
   qMap_Ag_C0_V0->SetBinContent(2809,846943);
   qMap_Ag_C0_V0->SetBinContent(2860,909);
   qMap_Ag_C0_V0->SetBinContent(2863,673134);
   qMap_Ag_C0_V0->SetBinContent(2914,10754);
   qMap_Ag_C0_V0->SetBinContent(2917,159044);
   qMap_Ag_C0_V0->SetBinContent(2968,1573);
   qMap_Ag_C0_V0->SetBinContent(2971,1901995);
   qMap_Ag_C0_V0->SetBinContent(3022,500);
   qMap_Ag_C0_V0->SetBinContent(3025,1547710);
   qMap_Ag_C0_V0->SetBinContent(3076,4861);
   qMap_Ag_C0_V0->SetBinContent(3079,6757442);
   qMap_Ag_C0_V0->SetBinContent(3130,1503);
   qMap_Ag_C0_V0->SetBinContent(3133,41038);
   qMap_Ag_C0_V0->SetBinContent(3184,2140);
   qMap_Ag_C0_V0->SetBinContent(3187,642564);
   qMap_Ag_C0_V0->SetBinContent(3238,344);
   qMap_Ag_C0_V0->SetBinContent(3241,105791);
   qMap_Ag_C0_V0->SetBinContent(3292,238874);
   qMap_Ag_C0_V0->SetBinContent(3295,806557);
   qMap_Ag_C0_V0->SetBinContent(3346,173766);
   qMap_Ag_C0_V0->SetBinContent(3349,197258);
   qMap_Ag_C0_V0->SetBinContent(3400,9229);
   qMap_Ag_C0_V0->SetBinContent(3403,565122);
   qMap_Ag_C0_V0->SetBinContent(3454,5990);
   qMap_Ag_C0_V0->SetBinContent(3457,401465);
   qMap_Ag_C0_V0->SetBinContent(3508,5199);
   qMap_Ag_C0_V0->SetBinContent(3511,364442);
   qMap_Ag_C0_V0->SetBinContent(3562,1374);
   qMap_Ag_C0_V0->SetBinContent(3565,811424);
   qMap_Ag_C0_V0->SetBinContent(3616,986);
   qMap_Ag_C0_V0->SetBinContent(3619,55629);
   qMap_Ag_C0_V0->SetBinContent(3670,376979);
   qMap_Ag_C0_V0->SetBinContent(3673,574895);
   qMap_Ag_C0_V0->SetBinContent(3724,1071);
   qMap_Ag_C0_V0->SetBinContent(3727,988769);
   qMap_Ag_C0_V0->SetBinContent(3778,521);
   qMap_Ag_C0_V0->SetBinContent(3781,177881);
   qMap_Ag_C0_V0->SetBinContent(3832,130231);
   qMap_Ag_C0_V0->SetBinContent(3835,1288683);
   qMap_Ag_C0_V0->SetBinContent(3886,2998);
   qMap_Ag_C0_V0->SetBinContent(3889,1842798);
   qMap_Ag_C0_V0->SetBinContent(3940,596);
   qMap_Ag_C0_V0->SetBinContent(3943,1988062);
   qMap_Ag_C0_V0->SetBinContent(3994,1701);
   qMap_Ag_C0_V0->SetBinContent(3997,58393);
   qMap_Ag_C0_V0->SetBinContent(4048,872);
   qMap_Ag_C0_V0->SetBinContent(4102,1051);
   qMap_Ag_C0_V0->SetBinContent(4105,313176);
   qMap_Ag_C0_V0->SetBinContent(4156,8614);
   qMap_Ag_C0_V0->SetBinContent(4159,601775);
   qMap_Ag_C0_V0->SetBinContent(4210,72651);
   qMap_Ag_C0_V0->SetBinContent(4213,41515);
   qMap_Ag_C0_V0->SetBinContent(4264,2165);
   qMap_Ag_C0_V0->SetBinContent(4267,1202776);
   qMap_Ag_C0_V0->SetBinContent(4318,421);
   qMap_Ag_C0_V0->SetBinContent(4321,6405);
   qMap_Ag_C0_V0->SetBinContent(4372,366);
   qMap_Ag_C0_V0->SetBinError(55,147489.8);
   qMap_Ag_C0_V0->SetBinError(56,1910.298);
   qMap_Ag_C0_V0->SetBinError(57,1964.919);
   qMap_Ag_C0_V0->SetBinError(58,1180.751);
   qMap_Ag_C0_V0->SetBinError(59,1476.31);
   qMap_Ag_C0_V0->SetBinError(60,1182.373);
   qMap_Ag_C0_V0->SetBinError(61,2129.818);
   qMap_Ag_C0_V0->SetBinError(62,1091.88);
   qMap_Ag_C0_V0->SetBinError(63,1221.337);
   qMap_Ag_C0_V0->SetBinError(64,1876.966);
   qMap_Ag_C0_V0->SetBinError(65,1911.701);
   qMap_Ag_C0_V0->SetBinError(66,1471.094);
   qMap_Ag_C0_V0->SetBinError(67,8389.291);
   qMap_Ag_C0_V0->SetBinError(70,1168.717);
   qMap_Ag_C0_V0->SetBinError(71,718.1817);
   qMap_Ag_C0_V0->SetBinError(72,135.5175);
   qMap_Ag_C0_V0->SetBinError(74,967.3412);
   qMap_Ag_C0_V0->SetBinError(75,605.3115);
   qMap_Ag_C0_V0->SetBinError(76,81);
   qMap_Ag_C0_V0->SetBinError(77,509.7833);
   qMap_Ag_C0_V0->SetBinError(78,576.0295);
   qMap_Ag_C0_V0->SetBinError(79,1312.419);
   qMap_Ag_C0_V0->SetBinError(80,749.4705);
   qMap_Ag_C0_V0->SetBinError(81,827.7306);
   qMap_Ag_C0_V0->SetBinError(82,547.0704);
   qMap_Ag_C0_V0->SetBinError(83,579.3686);
   qMap_Ag_C0_V0->SetBinError(84,321.694);
   qMap_Ag_C0_V0->SetBinError(85,555.5115);
   qMap_Ag_C0_V0->SetBinError(86,475.0116);
   qMap_Ag_C0_V0->SetBinError(87,649.8231);
   qMap_Ag_C0_V0->SetBinError(88,411.2894);
   qMap_Ag_C0_V0->SetBinError(89,310.6912);
   qMap_Ag_C0_V0->SetBinError(90,293.307);
   qMap_Ag_C0_V0->SetBinError(91,900.1067);
   qMap_Ag_C0_V0->SetBinError(93,1155.74);
   qMap_Ag_C0_V0->SetBinError(94,546.6434);
   qMap_Ag_C0_V0->SetBinError(95,601.3094);
   qMap_Ag_C0_V0->SetBinError(96,530.5092);
   qMap_Ag_C0_V0->SetBinError(97,252.1666);
   qMap_Ag_C0_V0->SetBinError(98,283.0724);
   qMap_Ag_C0_V0->SetBinError(99,179.6385);
   qMap_Ag_C0_V0->SetBinError(100,398.3278);
   qMap_Ag_C0_V0->SetBinError(101,621.9341);
   qMap_Ag_C0_V0->SetBinError(102,315.4695);
   qMap_Ag_C0_V0->SetBinError(103,538.7755);
   qMap_Ag_C0_V0->SetBinError(104,723.3685);
   qMap_Ag_C0_V0->SetBinError(105,427.9685);
   qMap_Ag_C0_V0->SetBinError(106,16295.05);
   qMap_Ag_C0_V0->SetBinError(109,908.764);
   qMap_Ag_C0_V0->SetBinError(163,92651.72);
   qMap_Ag_C0_V0->SetBinError(217,1604.94);
   qMap_Ag_C0_V0->SetBinError(268,534.4259);
   qMap_Ag_C0_V0->SetBinError(271,196590.8);
   qMap_Ag_C0_V0->SetBinError(322,410.5837);
   qMap_Ag_C0_V0->SetBinError(325,65542.05);
   qMap_Ag_C0_V0->SetBinError(376,710.9346);
   qMap_Ag_C0_V0->SetBinError(379,65539.43);
   qMap_Ag_C0_V0->SetBinError(430,65538.95);
   qMap_Ag_C0_V0->SetBinError(433,542.8766);
   qMap_Ag_C0_V0->SetBinError(484,388.4804);
   qMap_Ag_C0_V0->SetBinError(487,836.5076);
   qMap_Ag_C0_V0->SetBinError(538,636.1957);
   qMap_Ag_C0_V0->SetBinError(541,592.9907);
   qMap_Ag_C0_V0->SetBinError(595,65540.84);
   qMap_Ag_C0_V0->SetBinError(646,611.4262);
   qMap_Ag_C0_V0->SetBinError(649,65531.43);
   qMap_Ag_C0_V0->SetBinError(700,749.4418);
   qMap_Ag_C0_V0->SetBinError(703,65538);
   qMap_Ag_C0_V0->SetBinError(754,364.9712);
   qMap_Ag_C0_V0->SetBinError(757,65544.76);
   qMap_Ag_C0_V0->SetBinError(808,318.033);
   qMap_Ag_C0_V0->SetBinError(811,113517.3);
   qMap_Ag_C0_V0->SetBinError(862,725.231);
   qMap_Ag_C0_V0->SetBinError(865,793.428);
   qMap_Ag_C0_V0->SetBinError(916,662.3171);
   qMap_Ag_C0_V0->SetBinError(919,146683.7);
   qMap_Ag_C0_V0->SetBinError(970,776.5076);
   qMap_Ag_C0_V0->SetBinError(973,131070.8);
   qMap_Ag_C0_V0->SetBinError(1024,460.3607);
   qMap_Ag_C0_V0->SetBinError(1027,382.5284);
   qMap_Ag_C0_V0->SetBinError(1078,629.6896);
   qMap_Ag_C0_V0->SetBinError(1081,1633.998);
   qMap_Ag_C0_V0->SetBinError(1132,859.5121);
   qMap_Ag_C0_V0->SetBinError(1135,146530.1);
   qMap_Ag_C0_V0->SetBinError(1186,559.9786);
   qMap_Ag_C0_V0->SetBinError(1189,65544.95);
   qMap_Ag_C0_V0->SetBinError(1240,236.5502);
   qMap_Ag_C0_V0->SetBinError(1243,131062.5);
   qMap_Ag_C0_V0->SetBinError(1294,520.2259);
   qMap_Ag_C0_V0->SetBinError(1297,65546.97);
   qMap_Ag_C0_V0->SetBinError(1348,638.7582);
   qMap_Ag_C0_V0->SetBinError(1351,65533.48);
   qMap_Ag_C0_V0->SetBinError(1402,446.3362);
   qMap_Ag_C0_V0->SetBinError(1405,65550.11);
   qMap_Ag_C0_V0->SetBinError(1456,444.2668);
   qMap_Ag_C0_V0->SetBinError(1459,1641.768);
   qMap_Ag_C0_V0->SetBinError(1510,869.9345);
   qMap_Ag_C0_V0->SetBinError(1513,65539.71);
   qMap_Ag_C0_V0->SetBinError(1564,1038.882);
   qMap_Ag_C0_V0->SetBinError(1567,1606.307);
   qMap_Ag_C0_V0->SetBinError(1618,1115.408);
   qMap_Ag_C0_V0->SetBinError(1621,92677.81);
   qMap_Ag_C0_V0->SetBinError(1672,341.4777);
   qMap_Ag_C0_V0->SetBinError(1675,9837.734);
   qMap_Ag_C0_V0->SetBinError(1726,578.6743);
   qMap_Ag_C0_V0->SetBinError(1729,1190.475);
   qMap_Ag_C0_V0->SetBinError(1780,469.0426);
   qMap_Ag_C0_V0->SetBinError(1783,65543.09);
   qMap_Ag_C0_V0->SetBinError(1834,406.0788);
   qMap_Ag_C0_V0->SetBinError(1837,2397.154);
   qMap_Ag_C0_V0->SetBinError(1888,812.3226);
   qMap_Ag_C0_V0->SetBinError(1891,131076.2);
   qMap_Ag_C0_V0->SetBinError(1942,732.5619);
   qMap_Ag_C0_V0->SetBinError(1945,65533.05);
   qMap_Ag_C0_V0->SetBinError(1996,446.0617);
   qMap_Ag_C0_V0->SetBinError(1999,65539.28);
   qMap_Ag_C0_V0->SetBinError(2050,750.8096);
   qMap_Ag_C0_V0->SetBinError(2053,1080.153);
   qMap_Ag_C0_V0->SetBinError(2104,710.929);
   qMap_Ag_C0_V0->SetBinError(2107,1743.866);
   qMap_Ag_C0_V0->SetBinError(2158,370.0297);
   qMap_Ag_C0_V0->SetBinError(2161,65573.39);
   qMap_Ag_C0_V0->SetBinError(2212,141.711);
   qMap_Ag_C0_V0->SetBinError(2215,1906.998);
   qMap_Ag_C0_V0->SetBinError(2266,672.2157);
   qMap_Ag_C0_V0->SetBinError(2269,1258.155);
   qMap_Ag_C0_V0->SetBinError(2290,1123.618);
   qMap_Ag_C0_V0->SetBinError(2291,95);
   qMap_Ag_C0_V0->SetBinError(2292,223.4748);
   qMap_Ag_C0_V0->SetBinError(2320,476.0095);
   qMap_Ag_C0_V0->SetBinError(2323,1510.158);
   qMap_Ag_C0_V0->SetBinError(2343,65621.02);
   qMap_Ag_C0_V0->SetBinError(2344,19589.8);
   qMap_Ag_C0_V0->SetBinError(2345,18016.83);
   qMap_Ag_C0_V0->SetBinError(2346,1827.032);
   qMap_Ag_C0_V0->SetBinError(2374,1091.985);
   qMap_Ag_C0_V0->SetBinError(2377,1639.791);
   qMap_Ag_C0_V0->SetBinError(2396,6376.829);
   qMap_Ag_C0_V0->SetBinError(2397,19229.01);
   qMap_Ag_C0_V0->SetBinError(2398,22247.86);
   qMap_Ag_C0_V0->SetBinError(2399,22110.46);
   qMap_Ag_C0_V0->SetBinError(2400,18810.36);
   qMap_Ag_C0_V0->SetBinError(2401,214.3572);
   qMap_Ag_C0_V0->SetBinError(2428,712.1952);
   qMap_Ag_C0_V0->SetBinError(2431,236414.9);
   qMap_Ag_C0_V0->SetBinError(2450,21433.78);
   qMap_Ag_C0_V0->SetBinError(2451,24588.26);
   qMap_Ag_C0_V0->SetBinError(2452,136124.2);
   qMap_Ag_C0_V0->SetBinError(2453,31795.1);
   qMap_Ag_C0_V0->SetBinError(2454,19770.61);
   qMap_Ag_C0_V0->SetBinError(2455,6202.743);
   qMap_Ag_C0_V0->SetBinError(2482,570.1053);
   qMap_Ag_C0_V0->SetBinError(2485,1262.846);
   qMap_Ag_C0_V0->SetBinError(2504,22061.26);
   qMap_Ag_C0_V0->SetBinError(2505,116520.7);
   qMap_Ag_C0_V0->SetBinError(2506,49847.99);
   qMap_Ag_C0_V0->SetBinError(2507,201326.8);
   qMap_Ag_C0_V0->SetBinError(2508,22949.32);
   qMap_Ag_C0_V0->SetBinError(2509,18316.15);
   qMap_Ag_C0_V0->SetBinError(2536,332.7732);
   qMap_Ag_C0_V0->SetBinError(2539,93214.32);
   qMap_Ag_C0_V0->SetBinError(2558,23320.49);
   qMap_Ag_C0_V0->SetBinError(2559,29267.09);
   qMap_Ag_C0_V0->SetBinError(2560,211859.7);
   qMap_Ag_C0_V0->SetBinError(2561,317816.6);
   qMap_Ag_C0_V0->SetBinError(2562,162163.3);
   qMap_Ag_C0_V0->SetBinError(2563,10784.97);
   qMap_Ag_C0_V0->SetBinError(2590,838.0018);
   qMap_Ag_C0_V0->SetBinError(2593,516147.4);
   qMap_Ag_C0_V0->SetBinError(2612,19608.01);
   qMap_Ag_C0_V0->SetBinError(2613,25017.24);
   qMap_Ag_C0_V0->SetBinError(2614,33964.86);
   qMap_Ag_C0_V0->SetBinError(2615,30979.54);
   qMap_Ag_C0_V0->SetBinError(2616,21072.75);
   qMap_Ag_C0_V0->SetBinError(2617,6255.613);
   qMap_Ag_C0_V0->SetBinError(2644,390.8069);
   qMap_Ag_C0_V0->SetBinError(2647,919.9);
   qMap_Ag_C0_V0->SetBinError(2666,66401.74);
   qMap_Ag_C0_V0->SetBinError(2667,19139.15);
   qMap_Ag_C0_V0->SetBinError(2668,24060.36);
   qMap_Ag_C0_V0->SetBinError(2669,21119.81);
   qMap_Ag_C0_V0->SetBinError(2670,18071.09);
   qMap_Ag_C0_V0->SetBinError(2671,166);
   qMap_Ag_C0_V0->SetBinError(2698,65535.2);
   qMap_Ag_C0_V0->SetBinError(2701,113514);
   qMap_Ag_C0_V0->SetBinError(2720,702.5475);
   qMap_Ag_C0_V0->SetBinError(2721,161031.3);
   qMap_Ag_C0_V0->SetBinError(2722,20115.24);
   qMap_Ag_C0_V0->SetBinError(2723,18116.99);
   qMap_Ag_C0_V0->SetBinError(2724,6480.771);
   qMap_Ag_C0_V0->SetBinError(2752,350.0543);
   qMap_Ag_C0_V0->SetBinError(2755,1753.593);
   qMap_Ag_C0_V0->SetBinError(2776,205.5724);
   qMap_Ag_C0_V0->SetBinError(2777,413.0508);
   qMap_Ag_C0_V0->SetBinError(2806,408.3969);
   qMap_Ag_C0_V0->SetBinError(2809,131289.5);
   qMap_Ag_C0_V0->SetBinError(2860,287.1428);
   qMap_Ag_C0_V0->SetBinError(2863,113733.8);
   qMap_Ag_C0_V0->SetBinError(2914,952.2794);
   qMap_Ag_C0_V0->SetBinError(2917,92690.23);
   qMap_Ag_C0_V0->SetBinError(2968,368.5064);
   qMap_Ag_C0_V0->SetBinError(2971,262262.4);
   qMap_Ag_C0_V0->SetBinError(3022,212.8051);
   qMap_Ag_C0_V0->SetBinError(3025,307396.9);
   qMap_Ag_C0_V0->SetBinError(3076,635.2078);
   qMap_Ag_C0_V0->SetBinError(3079,604286.5);
   qMap_Ag_C0_V0->SetBinError(3130,372.654);
   qMap_Ag_C0_V0->SetBinError(3133,2029.192);
   qMap_Ag_C0_V0->SetBinError(3184,397.467);
   qMap_Ag_C0_V0->SetBinError(3187,92940.65);
   qMap_Ag_C0_V0->SetBinError(3238,158.3982);
   qMap_Ag_C0_V0->SetBinError(3241,65559.82);
   qMap_Ag_C0_V0->SetBinError(3292,65649.35);
   qMap_Ag_C0_V0->SetBinError(3295,66117.76);
   qMap_Ag_C0_V0->SetBinError(3346,3884.139);
   qMap_Ag_C0_V0->SetBinError(3349,65625.38);
   qMap_Ag_C0_V0->SetBinError(3400,874.2603);
   qMap_Ag_C0_V0->SetBinError(3403,7866.008);
   qMap_Ag_C0_V0->SetBinError(3454,664.7466);
   qMap_Ag_C0_V0->SetBinError(3457,131092.3);
   qMap_Ag_C0_V0->SetBinError(3508,650.917);
   qMap_Ag_C0_V0->SetBinError(3511,146540.7);
   qMap_Ag_C0_V0->SetBinError(3562,331.2884);
   qMap_Ag_C0_V0->SetBinError(3565,113796.9);
   qMap_Ag_C0_V0->SetBinError(3616,327.5729);
   qMap_Ag_C0_V0->SetBinError(3619,2293.153);
   qMap_Ag_C0_V0->SetBinError(3670,92759);
   qMap_Ag_C0_V0->SetBinError(3673,7911.745);
   qMap_Ag_C0_V0->SetBinError(3724,320.6603);
   qMap_Ag_C0_V0->SetBinError(3727,66277.31);
   qMap_Ag_C0_V0->SetBinError(3778,201.9084);
   qMap_Ag_C0_V0->SetBinError(3781,4346.633);
   qMap_Ag_C0_V0->SetBinError(3832,3391.517);
   qMap_Ag_C0_V0->SetBinError(3835,185558.6);
   qMap_Ag_C0_V0->SetBinError(3886,520.4748);
   qMap_Ag_C0_V0->SetBinError(3889,300378.8);
   qMap_Ag_C0_V0->SetBinError(3940,227.0242);
   qMap_Ag_C0_V0->SetBinError(3943,254040.8);
   qMap_Ag_C0_V0->SetBinError(3994,390.7058);
   qMap_Ag_C0_V0->SetBinError(3997,2495.258);
   qMap_Ag_C0_V0->SetBinError(4048,311.9038);
   qMap_Ag_C0_V0->SetBinError(4102,301.01);
   qMap_Ag_C0_V0->SetBinError(4105,113562.4);
   qMap_Ag_C0_V0->SetBinError(4156,901.0139);
   qMap_Ag_C0_V0->SetBinError(4159,8311.657);
   qMap_Ag_C0_V0->SetBinError(4210,2574.061);
   qMap_Ag_C0_V0->SetBinError(4213,2089.526);
   qMap_Ag_C0_V0->SetBinError(4264,464.7935);
   qMap_Ag_C0_V0->SetBinError(4267,11521.31);
   qMap_Ag_C0_V0->SetBinError(4318,224.4259);
   qMap_Ag_C0_V0->SetBinError(4321,846.5997);
   qMap_Ag_C0_V0->SetBinError(4372,170.4171);
   qMap_Ag_C0_V0->SetMinimum(0);
   qMap_Ag_C0_V0->SetEntries(1374458);
   qMap_Ag_C0_V0->SetStats(0);
   qMap_Ag_C0_V0->SetContour(20);
   qMap_Ag_C0_V0->SetContourLevel(0,0);
   qMap_Ag_C0_V0->SetContourLevel(1,8.788465);
   qMap_Ag_C0_V0->SetContourLevel(2,17.57693);
   qMap_Ag_C0_V0->SetContourLevel(3,26.36539);
   qMap_Ag_C0_V0->SetContourLevel(4,35.15386);
   qMap_Ag_C0_V0->SetContourLevel(5,43.94232);
   qMap_Ag_C0_V0->SetContourLevel(6,52.73079);
   qMap_Ag_C0_V0->SetContourLevel(7,61.51925);
   qMap_Ag_C0_V0->SetContourLevel(8,70.30772);
   qMap_Ag_C0_V0->SetContourLevel(9,79.09618);
   qMap_Ag_C0_V0->SetContourLevel(10,87.88465);
   qMap_Ag_C0_V0->SetContourLevel(11,96.67311);
   qMap_Ag_C0_V0->SetContourLevel(12,105.4616);
   qMap_Ag_C0_V0->SetContourLevel(13,114.25);
   qMap_Ag_C0_V0->SetContourLevel(14,123.0385);
   qMap_Ag_C0_V0->SetContourLevel(15,131.827);
   qMap_Ag_C0_V0->SetContourLevel(16,140.6154);
   qMap_Ag_C0_V0->SetContourLevel(17,149.4039);
   qMap_Ag_C0_V0->SetContourLevel(18,158.1924);
   qMap_Ag_C0_V0->SetContourLevel(19,166.9808);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   qMap_Ag_C0_V0->SetLineColor(ci);
   qMap_Ag_C0_V0->GetXaxis()->SetTitle("col");
   qMap_Ag_C0_V0->GetXaxis()->SetRange(10,36);
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

  g2D -> SetParameters(200,25,2, 45,2);

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
  //qMap_Ag_C0_V0 -> GetYaxis() -> SetRangeUser( g2D -> GetParameter(3) -10, g2D -> GetParameter(3) + 10);

  //X-Axis
  qMap_Ag_C0_V0 -> GetXaxis() -> SetTitleOffset(1.5);
  qMap_Ag_C0_V0 -> GetXaxis() -> SetRangeUser(g2D -> GetParameter(1) - 10, g2D -> GetParameter(1) + 10); // x-Axis
  qMap_Ag_C0_V0 -> GetXaxis() -> SetLabelSize( qMap_Ag_C0_V0 -> GetZaxis() -> GetLabelSize() ); //Y-Axis
  //qMap_Ag_C0_V0 -> GetXaxis() -> SetTitleSize( qMap_Ag_C0_V0 -> GetZaxis() -> GetTitleSize() ); //Y-Axis


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
  qMap_Ag_C0_V0->GetXaxis()->SetRange(10,34);

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
