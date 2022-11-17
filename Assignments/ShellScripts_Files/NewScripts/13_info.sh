#!/bin/bash


echo "Current User: " `whoami`
echo "Current Shell Directory: " `cat /etc/shells`
echo "Home Directory: " `pwd`
echo "Current Host Name: " `hoastnamectl`
echo "Os Info: " `uname -a`
echo "Hard Disk Info: " `df -l`
