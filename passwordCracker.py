#python file for turning sha256 hash digests into plain text 

#dictionary attack 
from contextlib import nullcontext
import hashlib
from queue import Empty #hash library 

def brute_force(hash_digest, salt):
    #brute force attack 
    #bf_list = ['12345678', 'crystal', 'i']; #Brute force list that contains words to check hash digest against 
    list = 'abcdefghijklmnopqrstuvwxyz1234567890' #list to brute force 
    bf_list = [];
    password_check = False; #password_check starts false because password has not been found yet
    password_plaintext = None; #set password_plaintext to empty at start because no plaintext has been found 
    #logic for brute force attack 
    for current in range(4): 
    #shuffles through list to generate an array a that contains shuffled words with a maximum character length of four characters 
        a = [i for i in list]
        for y in range(current):
            a = [x+i for i in list for x in a]
        bf_list.append(a); #adds shuffled array a to bf_list 

    for word in bf_list: #loops through array a in bf_list 
        for string in word: #loops through shuffled characters in array a 
            #encode word before pass to hashlib function & then pass to hashlib function 
            # concat salt and password, encode to utf-8
            salted_password = (salt + string).encode('utf-8')
            # hash salted password
            hash = hashlib.sha256(salted_password).hexdigest()
            if hash == hash_digest: #checks if found hash in dictionary_list is same as hash_digest from file 
                password_check = True; #hashes match so password has been found 
                password_plaintext = string #word is same as hash_digest from file so record word as password plaintext 
    return password_check, password_plaintext; 

def dictionary_siege(hash_digest, salt): 
    #dictionary attack
    dictionary_list = []; #create empty list 
    with open("rockyou.txt", encoding = "latin-1") as a_file: #opens and reads whole file 
        # /Users/maxlink/Desktop/Info-Sec/Lab3/hashes.txt
        for line in a_file:
         word = line.strip(); #grabs each hash digest line by line & adds salt to hash digest & stores in var hash_digest
         dictionary_list.append(word); 
    a_file.close(); #closes file 
    #logic for brute force attack 
    password_check = False; #password_check starts false because password has not been found yet
    password_plaintext = None; #start as none 
    for word in dictionary_list: 
        # concat salt and password, encode to utf-8
        salted_password = (salt + word).encode('utf-8')
        # hash salted password
        hash = hashlib.sha256(salted_password).hexdigest()
        if hash == hash_digest: #checks if found hash in dictionary_list is same as hash_digest from file 
            password_check = True; #hashes match so password has been found 
            password_plaintext = word #word is same as hash_digest from file so record word as password plaintext  
    #return password_check & password_plaintext 
    return password_check, password_plaintext; 

def writeToFile(dictionaryPasswordCheck, dictionaryplain_text, BFplain_text, bruteForcePasswordCheck, hash_digest): #writes to cracked.txt output file 

    if(dictionaryPasswordCheck == True):#writes this if dictionary attack cracks hash 
        f = open("cracked.txt", "a") #append to the end of cracked.txt file 
        f.write('<' + hash_digest + '>' + ':' + '<' + dictionaryplain_text + '>' + "\n") #writes result to cracked.txt file  
        f.close(); #closes cracked.txt file 
    if(bruteForcePasswordCheck == True and dictionaryPasswordCheck == False):#if dictionary attack fails then checks if brute force attack succeeded in crack 
        f = open("cracked.txt", "a") #append to the end of cracked.txt file 
        f.write('<' + hash_digest + '>' + ':' + '<' + BFplain_text + ">" + "\n") #writes result to cracked.txt file  
        f.close(); #closes cracked.txt file 
    if(dictionaryPasswordCheck == False and bruteForcePasswordCheck == False): #if both failed to crack then omits plaintext 
        f = open("cracked.txt", "a") #append to the end of cracked.txt file 
        f.write('<' + hash_digest + '>' + ":" + "\n") #writes result to cracked.txt file  
        f.close(); #closes cracked.txt file  

def main(): #basic python main method - that drives password cracking 
    outputMatched = [] #fill up with hashes & plaintext that should be written to output 
    outputUnmatched = [] #fill up with hashes 
    global salt;  #makes empty salt global var to store salt hash into 
    with open("salt.txt") as a_file: #opens salt file 
        for line in a_file: 
            salt = line.strip(); #grabs salt line & stores in salt global var 
    a_file.close(); #closes file 

    print("Cracking hashes & writing to file cracked.txt\n")
    with open("hashes.txt", encoding = "latin-1") as a_file: #opens and reads whole file 
        # /Users/maxlink/Desktop/Info-Sec/Lab3/hashes.txt
        for line in a_file:
         hash_digest = line.strip(); #grabs each hash digest line by line & adds salt to hash digest & stores in var hash_digest 

         dictionaryPasswordCheck, dictionaryplain_text = dictionary_siege(hash_digest, salt); #puts hash digest through a dictionary attack 
         bruteForcePasswordCheck, BFplain_text = brute_force(hash_digest, salt); #puts hash digest through a brute force attack 
         writeToFile(dictionaryPasswordCheck, dictionaryplain_text, BFplain_text, bruteForcePasswordCheck, hash_digest); #function to write to file 

    a_file.close(); #closes file 

    print("All results written to cracked.txt\n") #alerts user that results have been written to file 
    
    

if __name__ == "__main__": #calls the main driver 
    main()
