#!/bin/bash

max=$1

for n in "$@"
do
	if ((n>$max))
	then
		max=$n
	fi
done

echo "Largest element is" $max
