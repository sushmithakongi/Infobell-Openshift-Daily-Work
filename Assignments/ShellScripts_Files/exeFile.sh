#!/bin/bash

echo "Enter directory path: "
read path


ls $path>temp.txt
for file in `cat temp.txt`
	do
	if [ -x $file ];
	then
		echo $file
	fi
	done

rm temp.txt
