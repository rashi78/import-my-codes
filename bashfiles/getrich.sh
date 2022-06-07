#!bin/bash

echo "What's your name?"
read name 

echo "Enter your age?"
read age

getrich=$((($RANDOM%15) + age))

Echo "Calculating....."
sleep 1
echo "**"
sleep 1
echo "*****"
sleep 1 
echo "********"
echo "Done"
sleep 1
echo "You will be rich when you're $getrich in age!! "

