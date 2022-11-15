#!/bin/bash
function file_count()
 {
	local NUMBER_OF_FILE=$(ls -l | wc -l)
	echo "No of files present in the current directory are : $NUMBER_OF_FILE"
}
file_count
