# ISSUES TO FIX

## 1. Header should not show in output
```
Solution > Header has now been removed
```

## 2. Output should only show PROTOCOL SRC_IP DEST_IP PACKETS BYTES
```
Solution > Unnecessary fields have now been removed
```

## 3. How to run all search on all log files based on one field criteria
```
Solution > Just set the filename to all

Example : 

[*]  Please enter logfile name to analyse or ALL to analyse all files :  
FILENAME : all

[+]  Analysing all log files  
[*]  Please enter a filename to save the results (eg myfile.csv):  
FILENAME : outfile.csv

[+]  Results will be saved to :  output/outfile.csv  
[*]  Please choose one or more field criteria (e.g PROTOCOL=`TCP`) :  
      EXAMPLE : PROTOCOL=`TCP` and SRC IP=`ext` and DEST IP=`10127` and PACKETS > `10` )

Search: PROTOCOL=`TCP` 
```

### 4. How to use -lt,!(-eq),(-eq) comparison operators
Using one field criteria only
```
Solution > 

Example
[*]  Please enter logfile name to analyse or ALL to analyse all files :  
FILENAME : serv_acc_log_21032020.csv

[+]  Analysing file  serv_acc_log_21032020.csv  
[*]  Please enter a filename to save the results (eg myfile.csv):  
FILENAME : something.csv

[+]  Results will be saved to :  output/something.csv  
[*]  Please choose one or more field criteria (e.g PROTOCOL=`TCP`) :  
      EXAMPLE : PROTOCOL=`TCP` and SRC IP=`ext` and DEST IP=`10127` and PACKETS > `10` )

Search: PACKETS -lt `10` 

or 

Search: PACKETS > `10` 

or

Search: PACKETS !(-eq) `10` 

or

Search: PACKETS (-eq) `10` 


```
Using more than one field criteria - Examples
```
	Search : PROTOCOL=`TCP` and DEST IP=`10127` and PACKETS (-eq) `10` 
	Search : PROTOCOL=`TCP` and DEST IP=`10127` and PACKETS !(-eq) `10` 
	Search : PROTOCOL=`TCP` and DEST IP=`10127` and BYTES (-lt) `10` 
	Search : PROTOCOL=`TCP` and DEST IP=`10127` and BYTES (-gt) `10` 
```


## Example output after running the script
```
./script.sh

Available Log Files 
--------------------
 > serv_acc_log_03042020.csv  
 > serv_acc_log_12032020.csv  
 > serv_acc_log_14032020.csv  
 > serv_acc_log_17032020.csv  
 > serv_acc_log_21032020.csv  

[*]  Please enter logfile name to analyse or ALL to analyse all files :  
FILENAME : ALL

[+]  Analysing  ALL log files  
[*]  Please enter a filename to save the results (eg myfile.csv):  
FILENAME : results.csv

[+]  Results will be saved to :  output/results.csv  
[*]  Please choose one or more field criteria (e.g PROTOCOL=`TCP`) :  
      EXAMPLE : PROTOCOL=`TCP` and SRC IP=`ext` and DEST IP=`10127` and PACKETS > `10` )

Search: PROTOCOL=`ICMP` AND PACKETS -lt 20

[+]  2 criterias present  
  [!]  PROTOCOL=`ICMP`  

       23 records  


  [!]  PACKETS -LT 20  

         PACKETS => 23 records found   


[+]  Showing Results


ICMP        10132_69    EXT_SERVER  1           46          
ICMP        EXT_SERVER  10132_69    1           32          
ICMP        EXT_SERVER  10025_123   1           465         
ICMP        EXT_SERVER  10144_34    1           98          
ICMP        EXT_SERVER  10152_94    1           120         
ICMP        10156_89    EXT_SERVER  1           46          
ICMP        EXT_SERVER  10156_89    1           36          
ICMP        EXT_SERVER  10018_14    1           57          
ICMP        EXT_SERVER  10021_235   1           469         
ICMP        EXT_SERVER  10025_123   1           462         
ICMP        EXT_SERVER  10041_1     1           56          
ICMP        EXT_SERVER  10044_53    1           465         
ICMP        EXT_SERVER  10046_8     1           150         
ICMP        EXT_SERVER  10056_250   1           57          
ICMP        EXT_SERVER  10059_133   1           104         
ICMP        EXT_SERVER  10025_123   1           466         
ICMP        EXT_SERVER  10095_221   1           91          
ICMP        EXT_SERVER  10099_127   1           467         
ICMP        EXT_SERVER  10102_193   1           471         
ICMP        EXT_SERVER  10108_168   1           64          
ICMP        10118_90    EXT_SERVER  1           46          
ICMP        EXT_SERVER  10118_90    1           32          
ICMP        EXT_SERVER  10121_62    1           150         
 
23 results  
 
 
[+]  Results written to  output/results.csv 
```