#!/bin/bash

echo Hello
echo Please tip the name of the folder into the console

read name_folder

echo Creating folder with the name $name_folder

mkdir ./$name_folder

echo Copy root_6_fit_laser_test_vanilla.c into $name_folder

cp ./root_6_fit_laser_test_vanilla.c ./$name_folder

echo Rename file root_6_fit_laser_test_vanilla.c to "${name_folder}_root_6_fit_laser.c"

mv ./$name_folder/root_6_fit_laser_test_vanilla.c ./$name_folder/"${name_folder}_root_6_fit_laser.c"

echo Finish. Have fun with $name_folder
