#!/bin/bash

echo Hello
echo Please type the name of the folder into the console

read name_folder

echo Creating folder with the name $name_folder

mkdir ./$name_folder

echo Copy root_6_fit_laser_beam.c into $name_folder

cp ./root_6_fit_laser_beam.c ./$name_folder

echo Finish. Have fun with $name_folder
