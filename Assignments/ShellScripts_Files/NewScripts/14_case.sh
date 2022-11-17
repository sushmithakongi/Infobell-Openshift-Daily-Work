#!/bin/bash

pwd > temp.txt

cat temp.txt

tr "[:lower:]" "[:upper:]" < temp.txt > out.txt

cat out.txt
