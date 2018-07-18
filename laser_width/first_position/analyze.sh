#!/bin/bash

NAME=$1

if [ "$NAME" == '' ]

then
	echo 'Compile the whole folder'

	while read folder_name;
	do
			echo Compile folder $folder_name
			python pyroot_analyse.py $folder_name

	done < test.txt


else

	echo Compile folder $NAME
	python pyroot_analyse.py $NAME
	echo Done

fi
