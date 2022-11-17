#!/bin/bash

for i in "$@"
do
	echo `ls $i`
done
