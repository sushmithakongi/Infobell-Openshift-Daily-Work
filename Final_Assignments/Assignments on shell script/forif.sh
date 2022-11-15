#!/bin/bash    
  
for ((i=1; i<=20; i++));  
do  
	if [[ $i -gt 5 && $i -lt 16 ]];  
	then  
		continue  
	fi  
	echo $i  
done  

