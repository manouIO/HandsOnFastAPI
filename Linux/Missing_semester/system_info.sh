#! /usr/bin/bash
echo current date and time "$(date)"
echo free memory
free -h
echo uptime
uptime -p
echo operating system 
uname -o
echo running processes
ps aux > process.txt
