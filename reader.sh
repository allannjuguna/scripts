#! /bin/bash
# Bash script that calculates the sum of the absolute values

# This function returns the absolute of a value
function absolute(){
	num=$1
	if [[ num -lt 0 ]]
	then
		num=$(($num*-1))
	else
		num=$num
	fi
	# echo "New num is $num"
	returnvalue=$num
}

# Getting all the arguments of the program
read -p "Enter your values: " arguments
echo ${arguments}


result=0
for line in $arguments;do 
	absolute $line
	# Adding the absolute value to the result
	result=$(($result+$returnvalue))
done

# Printing the result
echo "Result : $result"


