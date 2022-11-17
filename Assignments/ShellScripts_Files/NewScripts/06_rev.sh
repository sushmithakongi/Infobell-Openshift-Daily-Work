#!/bin/bash

echo "Enter any number: "
read n1

rem=0
rev=0

for((i=n1; i>0;))
do 
	rem=$(($i % 10))
	rev=$(($rev * 10 + $rem))
	i=$(($i / 10))
done

echo "Reverse number is" $rev


