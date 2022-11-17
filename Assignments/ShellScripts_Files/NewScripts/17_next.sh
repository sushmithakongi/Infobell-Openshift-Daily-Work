#!/bin/bash

n1=$1

for((i=1; i<=$2; i++))
do
	echo "Line" $n1
	n1=$(($n1 + 1))
done
