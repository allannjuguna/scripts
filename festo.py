#! /usr/bin/python3
from math import floor
original=length=70  # This is the maximum length of each line
plus="+"
dash="-"
stick="|"
space=" "
header=tail=f"{plus}{(length -2) * dash}{plus}" # we minus 2 from the length to account for the first and last plus

def centerstring(string):
	global original,length
	length=length-2 # Accounting for the first and last stick
	strlen=len(string)
	remlen=length-strlen # Remaining length when we remove the string length (we will fill this space with dashes)
	# Dividing the remaining the length in 2 . The length for the spaces that come before and after the text
	firsthalf=secondhalf=int(floor((remlen / 2)))
	total=((firsthalf * 2) + strlen) # This is the total space allocated by the spaces and text.(Does not account for the 2 sticks that come before and after the text)
	while (total != length):
		if ( total < length):
			secondhalf+=1
			total+=1
		elif (total > length):
			secondhalf-=1
			total-=1
	final=(f"{stick}{space * firsthalf}{string}{space * secondhalf}{stick}")
	length=original # Resetting the length
	print(final)


print(header)
centerstring("charles babbage")
centerstring("is entitled")
print(tail)