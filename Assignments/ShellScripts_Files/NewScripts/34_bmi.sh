#!/bin/bash

w1=$1
h1=$2

h1=`echo $h1/100 | bc`
echo $h1

hs=$(($h1**2))
echo $hs

bmi=$(($w1/$hs) | bc)

echo $bmi
