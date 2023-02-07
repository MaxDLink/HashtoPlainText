
# Purpose of Program 
Turn HashDigests to their plain text equivalent with a dictionary attack & a brute force attack
# passwordcracker.py 

passwordCracker.py is a program that converts hash digests to their plain text equivalent via a dictionary attack and a brute force attack 
# Included files 
passwordcracker.py - contains code logic for dictionary attack and brute force attack. Reads in hashes.txt line by line. Compares these hashes to words in rockyou.txt list in the dictionary attack method and prints any plaintext that corresponds to the read in hash digest. In the brute force method, the read in hash digest is compared to shuffled words generated from a string that contains the lowercase alphabet and numbers from 0 - 10. Any plaintext found that matches the hash digest is also printed form the brute force attack and if both the dictionary attack and brute force attack fail, then the hash digest is printed without any accompanying plain text. 

salt.txt - contains the salt hash that is read in with passwordcracker.py and concatinated to the end of the hashed plaintext. 

hashes.txt - contains the hashes that passwordcracker.py reads in to crack 

rockyou.txt - contains the word list that passwordcracker.py reads in for the dictionary attack 

cracked.txt - the final output file that all of the found & unfound hashes are written to for user viewing 
## how to compile/run the program 
unzip the file

in passwordcracker.py make sure that the file paths for salt.txt, hashes.txt, rockyou.txt, and cracked.txt are correct 
(should be correct on first run beause passwordcracker.py takes all of the above files as relative paths)

open the terminal and type: python3 passwordcracker.py

The program will print "cracking hashes & writing to file cracked.txt" to let user know that it is writing to file cracked.txt 

The program will print "All results written to cracked.txt" to let user know that it is done writing to file cracked.txt

view the cracked.txt file to see the cracked and uncracked hashes in the form <hash_digest>:<plain text>