for dir in "$@" ; do
if [ -d "$dir" ] ; then
	echo "Directory: $dir"
	ls "$dir"  
else
	echo "Not a directory: $dir"
fi
done
