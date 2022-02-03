
#!/bin/bash


# IMPLEMENTED ADVANCED FUNCTIONS
# -----------------------------------------------
# Enable the log tool script to run searches on all available server access logs based on one (1) field criteria input, e.g., find all matches where PROTOCOL=`TCP` in all available log files
# When the PACKETS and/or BYTES fields are used as search criteria, totals for each of these should also be calculated and displayed as the final row of the search results printed to terminal/file


ByteCount=0
PacketCount=0

# Simple function for preparing the standard.standard may be PROTOCAL,PACKETS,BYTES etc
extractcolumn() {
	# Where standard is PROTOCOL=`TCP` OR DEST_IP=EXT_SERVER
	standard=$1
	column=`echo ${standard} | awk -F "=" '{print $1}'`
	# Column can be PROTOCOL,PACKETS,BYTES,DEST_IP etc.
	echo $column
}

# Simple function for preparing the value for a standard. This may be TCP (for protocol),EXT_SERVER (for dest ip)
extractvalue(){
	# Where standard is PROTOCOL=`TCP` OR DEST_IP=EXT_SERVER
	standard=$1
	# Fetching the value from the standard and removing the backticks from the value
	value=`echo ${standard}   | awk -F "=" '{print $2}' | sed s/'\`'/''/g`
	# Value can be TCP,EXT_SERVER etc
	echo $value
}
# This function Deletes a file
removeFile(){
	touch "${1}"
	rm "${1}" 2>/dev/null
}
# This function checks whether the provided file exists
checkfile(){
	if [[ -f $LOG_FILE ]]; then
		LOG_FILE="${1}"
	else
		echo
		echo -e "Entered File '$LOG_FILE' does not exist"
		echo -e " ABORTING"
		exit
	fi

}

# PROGRAM FUNCTIONS

add() {
	total=$(($1 + 1));
}

# Script Execution starts here
echo -e "------------------------ Starting ----------------------------"
echo

# Continue executing until the user terminates
while true;do

	# STAGE ONE ; GETTING AVAILABLE LOG FILES
	logfiles=("Use all available log files")

	# Getting available log files
	for logfile in `ls *.csv`;do
		logfiles+=("$logfile")
	done

	echo "Available Log Files: $((${#logfiles[@]} - 1))."
	echo

	echo
	for index in "${!logfiles[@]}";do
		echo -e " [ $index ] $LIST ${logfiles[index]}" 
	done
	echo


	# STAGE TWO; CHOOSING THE LOG FILE TO USE
	echo -e " Select the file name you wish to search [0,1,2,3,4, or 5] " 
	# option=1
	read -p " OPTION : " option

	if [[ $option =~ [0-9] ]];then
		echo -n ""
	else
		echo -e "Invalid option."
		exit
	fi

	LOG_FILE="${logfiles[$option]}" # This is the log file based on the option selected
	if [[ "${LOG_FILE}" == *"all available"* ]]
	then
		LOG_FILE="*.csv"
		echo -e "Using : all log files "
	else
		echo -e "Using : ${LOG_FILE}"
		checkfile $LOG_FILE
		LOG_FILE="${LOG_FILE}"
	fi
	echo

	# STAGE THREE; CHOOSING THE OUTPUT FILE
	echo -e "Enter CSV Output file to save results : (Eg. output.csv) "
	read -p "LOG_FILE : " CSVFILE
	# CSVFILE="test.csv"
	echo

	if [[ $CSVFILE == *".csv"* ]]
	then
		true
	else
		CSVFILE="${CSVFILE}.csv"
	fi

	outputFolder="outfiles"
	mkdir -p $outputFolder 2>/dev/null #Generating output folder for storing results
	outputFile="$outputFolder/$CSVFILE" #Creating a path using the outFolder and outFile
	tmpOutputFile="$outputFolder/tmpOutputFile.txt" #Creating a temp file to store temporary output
	removeFile $tmpOutputFile # Making sure the temp file does not exist

	if test -f "$outputFile"; then
		echo -e "$outputFile already exists."
		exit
	else
		true # Do nothing 
	fi

	touch $outputFile 2>/dev/null # Creating the outfile
	echo -e "Output File created at  : $outputFile "
	echo

	# Searching log files 
	echo -e " Enter one parameter to Query (Eg. PROTOCOL ICMP or PACKETS -lt 10 ): "
	# echo -e "   Examples : "
	# printf "%-60s%-12s\n" "      PROTOCOL=\`ICMP\`" "-  for one field search" 
	# printf "%-60s%-12s\n" "      PROTOCOL=\`TCP\` and SRC IP=\`ext\` and PACKETS > \`10\`" "-  for multiple field search" 


	Extract="SRC IP=\`EXT_SERVER\` and PROTOCOL=\`TCP\` and BYTES > \`10\` and PACKETS -lt \`10\`" # Example Query
	read -p "Your Query: " Extract # reading the Query

	Extract=`echo $Extract | awk '{print toupper($0)}' | sed s/" AND "/","/g ` # Making the search case insensitive


	
	ExtractStrings (){ # Searching through protocal,destip,srcip
		total=0
		RECORDS=`cat $LOG_FILE | grep -iv "DATE,DURATION,PROTOCOL," | grep -iv "normal"`
		SearchA=$1
		columnNum=$2
		caseSensitive=$3
		column=$(extractcolumn $SearchA)
		value=$(extractvalue $SearchA)

		while read -r string;
		do  
			# Finding the value and removing spaces
			awk="awk -F \",\" '{print \$$columnNum}'"
			outval=`echo $string | eval $awk | sed s/" "/""/g`

			# Checking whether the search should be case sensitive
			if [[ $caseSensitive == "yes" ]]
			then
				if [[ $outval == "$value" ]]
				then
					echo "${string}" >> $outputFile
					add $total
				else
					true # do nothing
				fi
			else
				if [[ $outval == *"$value"* ]]
				then
					echo "${string}" >> $outputFile
					add $total
				else
					true # do nothing
				fi
			fi
		done <<< $RECORDS

		echo>$tmpOutputFile
		mv $outputFile $tmpOutputFile 2>/dev/null
		removeFile $outputFile
		LOG_FILE=$tmpOutputFile # Setting the temporary file as the input file (Using the results from the previous query as the input)
		echo
		echo -e "       $total records "
		echo
		echo
		total=0

	}



	# For performing comparisons in packets and bytes
	ExtractPackets(){
		total=0
		string=""
		RECORDS=`cat $LOG_FILE | grep -iv "DATE,DURATION,PROTOCOL," | grep -iv "normal"`
		criteria=$1
		columnNum=$2
		caseSensitive=$3
		IFS=' ' read -r -a params <<< "$criteria"
		column=`echo "${params[0]}"| sed s/" "/""/g`
		echo
		operator=`echo "${params[1]}"| sed s/" "/""/g | awk '{ print tolower($0) }' ` 
		value=`echo "${params[2]}" | sed s/'\`'/''/g | sed s/" "/""/g `

		# Fetching the sign to use in the comparison
		if [[ $operator == "<" || $operator == *"-lt"* ]]
		then
			sign="-lt"
		elif [[ $operator == ">" || $operator == *"-gt"* ]]
		then
			sign="-gt"
		elif [[ $operator == "=" || $operator == "-eq" || $operator == "(-eq)" ]]
		then
			sign="-eq"
		elif [[ $operator == "!=" || $operator == *"!(-eq)"* || $operator == "-ne" ]]
		then
			sign="-ne"
		else
			echo -e "Please use a valid operator "
			exit 
		fi


	# Reading the results in the file
		while read -r string;
		do  
			awk="awk -F \",\" '{print \$$columnNum}'"
			# Adding the getting the column value and removing spaces - returns packet value
			outval=`echo $string | eval $awk | sed s/" "/""/g`

			# Building a query based on the user input
			query="$outval $sign $value"
			
			# Running the query
			result=`eval 'test $query && echo true || echo false' 2>/dev/null`

			# Fetching the results based on logic
			if [[ $caseSensitive == "yes" ]]
			then
				if [[ $result == "true" ]]
				then
					add $total
					echo "${string}" >> $outputFile

				else
					true # this does nothing
				fi
			else
				if [[ $outval == *"$value"* ]]
				then
					add $total
					echo "${string}" >> $outputFile
				else
					true # this does nothing
				fi
			fi
		done <<< $RECORDS
		string=""
		echo>$tmpOutputFile
		mv $outputFile $tmpOutputFile 2>/dev/null
		removeFile $outputFile
		LOG_FILE=$tmpOutputFile
		echo -e "         $column => $total records found "
		echo
	}

	IFS=',' read -r -a array <<< "$Extract"

	echo

	criteria="${array[0]}"
	SearchA=`echo $criteria | sed s/" "/""/g` # Removing spaces from the criteria
	echo -e "  $COLUMNS $criteria"

	if [[ $SearchA == *"PROTOCOL"* ]]
	then
		ExtractStrings $SearchA 3 no
	elif [[ $SearchA == *"SRCIP"* ]]
	then
		ExtractStrings $SearchA 4 no
	elif [[ $SearchA == *"DESTIP"* ]]
	then
		ExtractStrings $SearchA 6 no
	elif [[ $SearchA == *"PACKETS"* ]]
	then
		ExtractPackets "${criteria}" 8 yes
		PacketCount=$total
	elif [[ $SearchA == *"BYTES"* ]]
	then
		ExtractPackets "${criteria}" 9 yes
		ByteCount=$total
	else
		echo -e "Invalid Field Name"
		exit
	fi
	# done

	echo
	echo
	cat $tmpOutputFile >> $outputFile
	removeFile $tmpOutputFile
	echo "PROTOCOL,SRC IP,DEST IP,PACKETS,BYTES"> $tmpOutputFile


	OrganizeOutput(){
		string=$1
		protocol=`echo $string | awk -F "," '{print $3}'`
		src_ip=`echo $string | awk -F "," '{print $4}'`
		dest_ip=`echo $string | awk -F "," '{print $6}'`
		packets=`echo $string | awk -F "," '{print $8}'`
		bytes=`echo $string | awk -F "," '{print $9}'`
		printf "%-12s%-12s%-12s%-12s%-12s\n" "$protocol" "$src_ip" "$dest_ip" "$packets" "$bytes"
		echo "$protocol,$src_ip,$dest_ip,$packets,$bytes" >> $tmpOutputFile
	}

	echo -e "Printing Results"
	echo
	total=0
	while read -r string;
	do
		add $total
		OrganizeOutput "${string}"
	done <<< `cat $outputFile | grep -iv "PACKETS" || echo `
	echo 
	if [[ $ByteCount -gt 0 ]]
	then	
		echo -e "Total Byte Records found : $ByteCount"
	elif [[ $PacketCount -gt 0 ]]
	then
		echo -e "Total Packet Records found : $PacketCount"
	fi
	echo 
	echo 
	mv $tmpOutputFile $outputFile
	echo -e "Records can be found at : $outputFile"

	echo
	read -p "Run a different search (y/n)?: " run
    case "$run" in 
        n|N) echo "Terminated by the User. Thank you!" && break;;
        y|Y) echo "Begin Next Search. BEGIN";;
        *) echo "invalid input, thank you" && exit 1;;
    esac
done