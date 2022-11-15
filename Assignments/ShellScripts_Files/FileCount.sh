#!/bin/bash


function countFile()
{
local Number_Of_Files=$(ls | wc -l)
echo "Number of files= "$Number_Of_Files
}


countFile
