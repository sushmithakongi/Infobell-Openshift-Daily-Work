echo Executable files
files=$(find lab_solutions -executable -type f)
echo $files
echo
echo List of Directories
dir=$(ls -d )
echo $dir
echo
echo List of zero sized files
zero=$(find -size 0)
echo $zero
