#!/bin/bash

arr="$@"
declare temp=0
declare length=${#arr}
echo $length

for((i=0; i<=$length; i++))
do
	for((j=0; j<$length; j++))
	do
		if(($i > $j))
		then
			temp = ${arr[$j]}
			arr[$j] = ${arr[$((j+1))]}
			arr[$((j+1))] = $temp
		fi
	done
done

echo ${arr[*]}
