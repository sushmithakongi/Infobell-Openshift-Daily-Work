#!/bin/bash

touch temp1.txt

mv temp1.txt $1 > temp3.txt

cat temp3.txt

rm temp3.txt
