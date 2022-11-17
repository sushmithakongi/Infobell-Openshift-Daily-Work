#!/bin/bash

echo "Enter any two number: "
read n1 n2

sum=`echo $n1+$n2 | bc`
echo "Addition=" $sum
