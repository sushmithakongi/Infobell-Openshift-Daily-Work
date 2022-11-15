#! /bin/bash
number=1
n=4
for((i=1; i<=n; i++))
do
	for((j=1; j<=i; j++))
        do
		echo -n "$number "
		number=$((number + 1))
	done
	echo
done
			        
