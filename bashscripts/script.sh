#! /bin/bash

# COPY ONE

#######################################################################
# NAME :                                                              #
# STUDENT NUMBER                                                      #
#                                                                     #
#######################################################################



white=""
space=""
yellow=": "

fail="${white}[${red}-${white}] " 
success="${white}[${space}+${white}] "
debug="${white}[${space}!${white}] "
input="${white}[${space}*${white}] "
semistage="  ${white}${space}^${white} "
item=" ${white}${yellow}>${white} "
end="$white "


# Simple function for debugging - 
debug(){
	true
	# echo -e "${1}"
}


# Deletes a file or it's contents
clearfile(){
	rm "${1}" 2>/dev/null
}


debug "$success Starting the program $end"]
echo ""

while true;do
	# Shows the available log files
	AVAILABLE_LOGFILES=`ls *.csv`
	echo "Available Log Files "
	echo "--------------------"
	for logfile in $AVAILABLE_LOGFILES;do
		echo -e "$item$logfile $end" 
	done

	# Function to check whether a file exists - If a file does not exist,the program while exit
	ret=0
	function checkfileexists() {
		filename=$1
		if [ -f $filename ]
		then
			ret=1
		else
			ret=0
			echo ""
			echo -e "$fail File '$filename' does not exist $end"
			echo -e "$fail Exitting $end"

			exit
		fi
	}

	# Simple function for preparing the criteria.criteria may be PROTOCAL,PACKETS,BYTES etc
	getfield() {
		criteria=$1
		local field=`echo ${criteria} | awk -F "=" '{print $1}'`
		echo $field
	}

	# Simple function for preparing the value for a criteria. This may be TCP (for protocol),EXT_SERVER (for dest ip)
	getvalue(){
		criteria=$1
		local value=`echo ${criteria}   | awk -F "=" '{print $2}' | sed s/'\`'/''/g`
		echo $value
	}



	# STEP : Prompting the user to choose a log file to analyse e.g serv_acc_log_03042020.csv
	echo ""
	echo -e "$input Please enter logfile name to analyse or ALL to analyse all files : $end" 
	read -p "FILENAME : " FILENAME
	echo ""


	if [[ `echo $FILENAME | awk '{print toupper($0)}'` == "ALL" ]]
	then
		echo -e "$success Analysing $yellow $FILENAME log files $end"
		FILENAME="*.csv"
	else
		checkfileexists $FILENAME
		echo -e "$success Analysing file $yellow $FILENAME $end"
	fi

	# STEP : Prompting the user to enter the outfile
	# Folder to store the outfiles
	OUTFOLDER="output"

	# Creating the folder if it does not exist
	mkdir -p $OUTFOLDER 2>/dev/null

	# Writing the results to a file
	echo -e "$input Please enter a filename to save the results (eg myfile.csv): $end"
	# Example resfile
	read -p "FILENAME : " RESFILE
	echo ""


	if [[ $RESFILE == *".csv"* ]]
	then
		true
	else
		RESFILE="${RESFILE}.csv"
	fi

	OUTFILE="$OUTFOLDER/$RESFILE"
	touch $OUTFILE 2>/dev/null
	TEMPFILE="$OUTFOLDER/tempfile.txt"

	# Making sure the TEMPFILE  and $OUTFILE do not exist (if they exist ,they may interfere with the results)
	clearfile $TEMPFILE 
	clearfile $OUTFILE

	# This header format will be used to create the results file
	HEADER="DATE,DURATION,PROTOCOL,SRC IP,SRC PORT,DEST IP,DEST PORT,PACKETS,BYTES,FLOWS,FLAGS,TOS,CLASS"
	echo -e "$success Results will be saved to : $yellow $OUTFILE $end"


	# ENTERING THE SEARCH CRITERIA (SEARCH STRING)
	EXAMPLE="PROTOCOL=\`TCP\` and SRC IP=\`ext\` and DEST IP=\`10127\` and PACKETS > \`10\`"
	echo -e "$input Please choose one or more field criteria (e.g PROTOCOL=\`TCP\`) : $end"
	echo -e "      EXAMPLE : $EXAMPLE )"
	echo -e ""
	# Fetching the search criteria
	read -p "Search: " SEARCH

	# Displays Raw input - before input sanitization
	debug " $item First : $SEARCH $end"

	# Sanitizing the input
	# Replacing " and " with "," - Helps in determining criteria eg protocol,bytes,packets e.t.c
	SEARCH=`echo $SEARCH | awk '{print toupper($0)}' | sed s/" AND "/","/g `

	# Displays input after input sanitization and minor fixes - like making it case insensitive
	debug " $item Second : $SEARCH $end"

	# First splitting into an array
	IFS=',' read -r -a array <<< "$SEARCH"

	# Counting the number of field criterias/parameters
	criteria_count="${#array[@]}"

	echo ""
	echo -e "$success $criteria_count criterias present $end"

	# SImple function to add one to a counter variable - helps in counting records
	addone() {
		counter=$1
		counter=$(($counter + 1));
	}

	# The search criteria applies for protocal,src ip ,dest ip etc
	searchcriteria (){
		counter=0
		# Reading the input file(s)
		CONTENTS=`cat $FILENAME | grep -iv "DATE,DURATION,PROTOCOL," | grep -i "suspicious"`
		criteria1=$1
		fieldnum=$2
		mustmatch=$3
		field=$(getfield $criteria1)
		value=$(getvalue $criteria1)
		debug ""
		debug " $criteria ($white FIELD=$field,VALUE=$value,Mustmatch=$mustmatch)"
		debug ""
		debug "==============================================================================================="

		# Searching for the params in the file
		# echo ""
		# Reading the file
		while read -r line;
		do  
			awk="awk -F \",\" '{print \$$fieldnum}'"
			resvalue=`echo $line | eval $awk | sed s/" "/""/g`
			if [[ $mustmatch == "match" ]]
			then
				if [[ $resvalue == "$value" ]]
				then

					debug "$resvalue $sign $value => $line"
					echo "$line" >> $OUTFILE
					addone $counter
				else
					true # this does nothing
				fi
			else
				if [[ $resvalue == *"$value"* ]]
				then
					debug "$resvalue $sign $value => $line"
					echo "$line" >> $OUTFILE
					addone $counter
				else
					true # this does nothing
				fi
			fi
		done <<< $CONTENTS

		echo "">$TEMPFILE
		mv $OUTFILE $TEMPFILE 2>/dev/null
		clearfile $OUTFILE
		FILENAME=$TEMPFILE
		echo ""
		echo -e "       $counter records $end"
		echo ""
		echo ""
		debug""
		counter=0

	}



	# This search applies for packets and bytes
	searchpacketscriteria(){
		counter=0

		CONTENTS=`cat $FILENAME | grep -iv "DATE,DURATION,PROTOCOL," | grep -i "suspicious"`
		criteria=$1
		fieldnum=$2
		mustmatch=$3
		IFS=' ' read -r -a params <<< "$criteria"

		field=`echo "${params[0]}"| sed s/" "/""/g`
		echo ""
		# Removing spaces from the operator and converting to lowercase
		operator=`echo "${params[1]}"| sed s/" "/""/g | awk '{ print tolower($0) }' ` 
		value=`echo "${params[2]}" | sed s/'\`'/''/g | sed s/" "/""/g `


		# Finding the operator to use for comparison based on user input
		if [[ $operator == "<" || $operator == *"-lt"* ]]
		then
			sign="-lt"
			# "Less sign detected"

		elif [[ $operator == ">" || $operator == *"-gt"* ]]
		then
			sign="-gt"
			# "Greater sign detected"

		elif [[ $operator == "=" || $operator == "-eq" || $operator == "(-eq)" ]]
		then
			sign="-eq"
			# "Greater sign detected"

		elif [[ $operator == "!=" || $operator == *"!(-eq)"* || $operator == "-ne" ]]
		then
			sign="-ne"
			# "Greater sign detected"

		else
			echo -e "$fail Invalid sign: Make sure the value is in the format \`VALUE_HERE\` $end"
			echo -e "$fail Invalid sign: For bytes and packets : write in the format PACKETS > \`10\` or BYTES > \`10\` $end"
			exit 
		fi

		debug ""
		debug " $criteria ($white FIELD=$field,VALUE=$value,OPERATOR=$operator,SIGN=$sign,Mustmatch=$mustmatch)"
		debug "==============================================================================================="
		debug ""


		while read -r line;
		do  
			awk="awk -F \",\" '{print \$$fieldnum}'"
			# Adding the getting the field value and removing spaces - returns packet value
			resvalue=`echo $line | eval $awk | sed s/" "/""/g`

			# Building a query based on the user input
			query="$resvalue $sign $value"
			
			# Running the query
			result=`eval 'test $query && echo true || echo false' 2>/dev/null`

			# Fetching the results based on logic
			if [[ $mustmatch == "match" ]]
			then
				if [[ $result == "true" ]]
				then
					addone $counter
					debug "$resvalue $sign $value => $line"
					echo "$line" >> $OUTFILE
				else
					true # this does nothing
				fi
			else
				if [[ $resvalue == *"$value"* ]]
				then
					addone $counter
					debug "$resvalue $sign $value => $line"
					echo "$line" >> $OUTFILE
				else
					true # this does nothing
				fi
			fi
		done <<< $CONTENTS
		echo "">$TEMPFILE
		mv $OUTFILE $TEMPFILE 2>/dev/null
		clearfile $OUTFILE
		FILENAME=$TEMPFILE
		echo -e "$space         $field => $counter records found  $end"
		debug ""
		counter=0
	}
	# End of function



	# Running searches on a single server access log of the user’s choice using both two (2) and three (3) field criteria inputs, e.g. find all matches where PROTOCOL=`TCP` and SRC IP=`ext` and PACKETS > `10`
	# Iterating through the array of criterias
	for index in ${!array[@]};do

		criteria="${array[index]}"
		original=$criteria
		criteria1=`echo $criteria | sed s/" "/""/g`
		echo -e "  $debug $criteria $end"
		# echo ""

		# Dealing with the protocal
		if [[ $criteria1 == *"PROTOCOL"* ]]
		then
			searchcriteria $criteria1 3 no

		# Dealing with srcip
		elif [[ $criteria1 == *"SRCIP"* ]]
		then
			searchcriteria $criteria1 4 no

		# Dealing with DEST IP
		elif [[ $criteria1 == *"DESTIP"* ]]
		then
			searchcriteria $criteria1 6 no

		# Dealing with PACKETS
		elif [[ $criteria1 == *"PACKETS"* ]]
		then
			searchpacketscriteria "${criteria}" 8 match

		# Dealing with BYTES
		elif [[ $criteria1 == *"BYTES"* ]]
		then
			searchpacketscriteria "${criteria}" 9 match

		else
			echo -e "$fail Invalid Search string $end"
			exit
		fi
	done

	echo ""

	# Writing the results to a file
	echo ""
	echo $HEADER > $OUTFILE
	cat $TEMPFILE >> $OUTFILE
	clearfile $TEMPFILE
	echo "PROTOCOL,SRC IP,DEST IP,PACKETS,BYTES"> $TEMPFILE


	# FUNCTION TO CREATE COLUMNS
	showcolumns(){
		fmt="%-12s%-12s%-12s%-12s%-12s\n"
		# printf "$fmt" PROTOCOL SRC_IP DEST_IP PACKETS BYTES
		echo ""
	}


	# FUNCTION TO CREATE FIELDS AND VALUES
	formatline(){
		line=$1
		date=`echo $line | awk -F "," '{print $1}'`
		duration=`echo $line | awk -F "," '{print $2}'`
		protocol=`echo $line | awk -F "," '{print $3}'`
		src_ip=`echo $line | awk -F "," '{print $4}'`
		src_port=`echo $line | awk -F "," '{print $5}'`
		dest_ip=`echo $line | awk -F "," '{print $6}'`
		dest_port=`echo $line | awk -F "," '{print $7}'`
		packets=`echo $line | awk -F "," '{print $8}'`
		bytes=`echo $line | awk -F "," '{print $9}'`
		class=`echo $line | awk -F "," '{print $13}'`
		printf "$fmt" "$protocol" "$src_ip" "$dest_ip" "$packets" "$bytes"
		echo "$protocol,$src_ip,$dest_ip,$packets,$bytes" >> $TEMPFILE
	}


	# Reading the results from the output file
	echo -e "$success Showing Results"
	echo ""
	# SHOWING THE COLUMNS FIRST
	showcolumns


	counter=0
	# ITERATING THROUGH THE LINES AND DISPLAYING THEM
	while read -r line;
	do
		addone $counter
		formatline "${line}"

	done <<< `cat $OUTFILE | grep -iv "PACKETS" || echo "" `
	echo " " 
	echo -e "$yellow$counter results $end"
	echo " " 
	echo " " 
	mv $TEMPFILE $OUTFILE
	echo -e "$success Results written to $yellow $OUTFILE $end"
	echo
	echo
	echo
done
