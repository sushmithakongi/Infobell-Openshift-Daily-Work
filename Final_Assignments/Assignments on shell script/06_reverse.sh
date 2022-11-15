#!/bin/bash
n=639872
n1=0
rev=0
while [ $n -gt 0 ]
do
	n1=$(( $n % 10 ))
	rev=$(( $rev * 10 + $n1 ))
	n=$(( $n / 10 ))
done
echo "Reverse number of entered digit is $rev"
