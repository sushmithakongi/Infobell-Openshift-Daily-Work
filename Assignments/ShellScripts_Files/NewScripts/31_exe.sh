#!/bin/bash

ls $1 > temp.txt

for i in `cat temp.txt`
do
	if [ -x $i ]
	then
		echo $i
	fi
done

echo "Total Files:" ` wc -l temp.txt `

rm temp.txt
