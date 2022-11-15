if [ "$#" = 0 ]
then
	echo "No arguments passed."
	exit 1
fi
  
MaximumElement=$1
  
for arg in "$@"
do
	if [ "$arg" -gt "$MaximumElement" ]
	then
		MaximumElement=$arg
	fi
done
echo "Largest value from the arguments passed is: $MaximumElement"

