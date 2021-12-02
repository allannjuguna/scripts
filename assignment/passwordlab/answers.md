# ANSWERS 
### 2 (d) What command did you use to view the content in the file hash.txt?
```
cat hash.txt
```

### 3 (a) What command should be used for an md5 hash?
```
-m stands for hashmode
The hashmode for md5 is 0

hashcat -a 0 -m 0 hash.txt dict1.txt --status --force
```

### 3 (a)  What command should be used for the attack mode of combination?
```
-a stands for attack mode
The attack mode for combination is 1
hashcat -a 1 -m 0 hash.txt dict1.txt --status --force
```


### 3 (c) What as the recovered password from the md5 hash?
```
tiger02
``` 


### 3 (c) What was the status?
```
Status: cracked
```

### 3 (c) How long did it take?
```
4 seconds
```

### 3 Part 2 : 1. What tools can be used to determine  what type of hash a particular hash value is ?
```
hash-identifier
hashid
```

### 3 Part 2 : 2. What was the possible hash value that was identified through the hash-identifier tool?
```
MD5
```

### 3 Part 2 : 2. What Kali Linux password tool can be used to creak Windos passwords using rainbow tables?
```
RainbowCrack - RainbowCrack is a general propose implementation of Philippe Oechslin’s faster time-memory trade-off technique. It crack hashes with rainbow tables.
```
### 3 Part 2 : 2. What Kali Linux cracking tool can be used to retrieve the syskey and extract Windows password hashes from Windows?
```
samdump2 - This tool is designed to dump Windows password hashes from a SAM file, using the syskey bootkey from the system hive.
```
