'''
Project: Edit Distance (Dynamic Programming)
Name: Jonathan Argumedo
Class: Data Structures 2302
Instructor: Diego Aguirre
TA: Anindita Nath
Date: December 9, 2018
Update by: (Your name goes here)
'''

#imports
import time


'''
'editDistance' method simply finds the differences in two 
words that are passed as parameters. A better explination can be
found online. 
'''
def editDistance(string, string2, lengthStr, lengthStr2):
    
    # If first string is empty 
    # insert all characters of second string into first 
    if lengthStr == 0:
        return lengthStr2
    
    # If second string is empty 
    # insert all characters of first string into first 
    if lengthStr2 == 0:
        return lengthStr
    
    # If last characters of two strings are same
    # Ignore last characters and get count for 
    # remaining strings. 
    if string[lengthStr - 1] == string2[lengthStr2 -1]:
        return editDistance(string, string2, lengthStr -1, lengthStr2 -1)

    #do all possible cases
    return 1 + min(
                #Insert
                editDistance(string, string2, lengthStr , lengthStr2 - 1),
                #delete
                editDistance(string, string2, lengthStr - 1, lengthStr2),
                #replace
                editDistance(string, string2, lengthStr - 1, lengthStr2 - 1) )

'''
'compute' method takes two strings as parameters and it computes the 
least difference between each word (Edit Distance)
'''
def compute(string, string2):
    print ('-' *20 + "EDIT DISTANCE" + '-' *20)
    print("Words:\t1) %s\n\t2) %s" %(string, string2))
    print("\n\nThe Edit Distance is: %d" % editDistance(string, string2, len(string), len(string2)))
    print ('-' * 53)


def main():
    #You could simply compy past the code from 'compute' method
    #and paste it in this method. Now your code
    #will be able to ask the user for 2 words
    '''
    print('-' *20 + "INPUT WORDS" + '-' *20)
    string = input("Enter the first word: ")
    string2 = input("Enter the second word: ")
    print('-' *51 + "\n\n")
    '''
    
    #LAB 7 (class scenerio)
    #I could of used one file to do comperasions
    #Just felt this would be better for testing
    try:
        name_file = input("Enter the name of the first file (include file extension): ")
        name_file2 = input("Enter the name of the second file (include file extension): ")
        file = open(name_file, "r")
        
        #compare each word in the first file with all the 
        #other words in the second file
        
        #check how long it takes to execute
        #for testing purposes only
        #(small files, small1 file) (big file, big1 file) etc
        start_time = time.time()
        
        for word in file:
            file2 = open(name_file2, "r")
            for compared in file2:
                compute(word, compared)
                
        print("\n\nIt took [%.5f] to find the distance for every possible word" %(time.time() - start_time))
    except FileNotFoundError:
        print("\n\nOops! File not found\nCheck the name and try again")
main()