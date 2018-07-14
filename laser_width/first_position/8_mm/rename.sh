#!/bin/bash

echo What is the height?

read height

mv ./Canvas_1.root ./$height"_pxar_data.root"
mv ./Canvas_1.C ./$height"_pxar_Canvas.C"
mv ./Xray-1.pdf ./$height"_hist_pxar.pdf"
mv ./Xray-2.pdf ./$height"_hist_pxar_zoomed.root"
mv ./Canvas_1_n40.root ./$height"_pxar_data_zoomed.root"
mv ./Canvas_1_n40.C ./$height"_pxar_Canvas_zoomed.C"

echo Done
