#!/bin/bash

echo Hello
echo Please tip the name of the folder into the console

read name_folder

echo Creating folder with the name $name_folder

mkdir ./$name_folder

echo Copy root_6_fit_laser_test_vanilla into $name_folder

cp ./root_6_fit_laser_test_vanilla.c ./$name_folder

echo Finish. Have fun with $name_folder
