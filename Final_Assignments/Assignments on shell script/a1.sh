if [ $# -eq 00 ]
then
	    echo "no arguments given"
	        exit
fi
rev=0
num1=0
for i in $*
do
	num1=$(( $i % 10 ))
	rev=$(( $rev /* 10 + $sd ))
	n=$(( $i / 10 ))
done
echo $rev
