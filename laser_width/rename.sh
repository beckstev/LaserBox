#!/bin/bash

echo What is the height?

read height

mv ./$height/Canvas_1.root ./$height/$height"_pxar_data.root"
mv ./$height/Canvas_1.C ./$height/$height"_pxar_Canvas.C"
mv ./$height/Xray-1.pdf ./$height/$height"_hist_pxar.pdf"
mv ./$height/Xray-2.pdf ./$height/$height"_hist_pxar_zoomed.pdf"
mv ./$height/Canvas_1_n40.root ./$height/$height"_pxar_data_zoomed.root"
mv ./$height/Canvas_1_n40.C ./$height/$height"_pxar_Canvas_zoomed.C"

echo Done
