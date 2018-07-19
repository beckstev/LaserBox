#!/bin/bash

NAME=$1
STYLE=$2
if  [ "$NAME" == "thesis" ]
then

	echo 'Compile the whole folder in thesis style'

	while read folder_name;
	do
			echo Compile folder $folder_name

			python pyroot_analyse.py $folder_name $NAME

	done < folder_name_list.txt

elif [ "$NAME" == '' ]
then

	echo 'Compile the whole folder '

	while read folder_name;
	do
			echo Compile folder $folder_name

			python pyroot_analyse.py $folder_name

	done < folder_name_list.txt

else

	echo Compile folder $NAME
	python pyroot_analyse.py $NAME $STYLE
	echo Done

fi
