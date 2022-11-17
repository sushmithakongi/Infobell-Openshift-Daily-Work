#!/bin/bash

for i in "$@"
do 
	length=${#i}
	echo "Length of string is" $length
done
