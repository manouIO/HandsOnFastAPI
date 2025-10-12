#! /usr/bin/bash
echo the current directory is
pwd
echo list all files in the Document dir
ls /home/maryse/Documents
mkdir my_directory
cd my_directory/
touch info.txt
echo this directory was created by  "$USERNAME" on "$(date)" > info.txt
cd ..
echo the total number of files in the current directory is 
ls -A|wc -l
if [ -d "/home/maryse/Documents/Training/Linux_training/Missing_semester/my_directory" ]; then
	echo "the directory exists"
else
	echo "the directory doesn't exist"
fi
