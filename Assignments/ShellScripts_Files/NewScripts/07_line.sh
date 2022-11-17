#!/bin/bash

cat file.txt | tr -s "\n" > newFile.txt

cat newFile.txt

rm newFile.txt
