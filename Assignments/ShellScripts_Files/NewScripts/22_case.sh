#!/bin/bash

tr "[:lower:]" "[:upper:]" < $1 > out.txt

cat out.txt

rm out.txt
