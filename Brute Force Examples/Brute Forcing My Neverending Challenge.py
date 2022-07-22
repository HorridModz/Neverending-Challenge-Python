import os.path
from os.path import exists
import io
import sys
import time
import string


def bruteforce():
    #Get path of neverending folder from user
    rootdirectory = input("\n\nEnter the directory of the challenge folder (without quotes):\n")
    print("Brute forcing challenge...")
    #Check that folder exists
    if not exists(rootdirectory):
        sys.exit("Could not find neverending challenge folder at this file path. Make sure you put it without quotes.")
    #Initialize messages list
    messages = []
    messageunique = {}
    #Iterate through all of the subfolders
    for subfolderletter in "abcdefghijklmnopqrstuvwxyz12345678990":
        #The name will always be the "Neverending" then a letter. This is consistent in the sub folders, and the nested folders of the sub folders
        subfoldername = "Neverending" + subfolderletter
        #The sub folder will be in the root directory,  with the name "Neverending" then a letter, as described above
        #Iterate through all the nested folders. The sub folder is included.
        for nestedfoldercount in range(10):
            #The sub folder will be in the root directory,  with the name "Neverending" then a letter, as described above.
            #The nested folders of the sub folder will be the same as the sub folder,
            #but each one will have the name "Neverending" then the same letter as the base folder
            #Because of this, for every layer, we just add on "\Neverending(letter)". To repeat a string, we use the * operator.
            #We need to add one from nestedfoldercount because python indexes start on 0, not 1
            nestedfolderpath = rootdirectory + (("\\" + subfoldername) * (nestedfoldercount + 1))
            #Get the Read This.txt file in the nested folder
            #The file is always called Read This.txt
            filepath = nestedfolderpath + "\\" + "Read This.txt"
            #Get the message of this file
            thismessage = getmessage(filepath)
            #Check if the message already exists or is unique
            if not thismessage in messages:
            #Add this message to the list of messages with the unique flag set to true
            #The unique flag will be set to false if this same message comes up later
                messages.append(thismessage)
                messageunique[thismessage] = True
            else:
                #This message already exists
                #Update this message's unique flag to false
                messageunique[thismessage] = False
    #Iterate through all of the messages until the unique one is found
    for thismessage in messages:
        #Check if the message is unique
        if messageunique[thismessage]:
            #We have found the unique message and cracked the puzzle!
            print("Successfully brute forced the unique message!")
            return(thismessage)
    #Not found - uh-oh!
    return("The unique message could not be found for an unknown reason. You most likely tampered with the folder to cause this.")
        
    
def getmessage(path):
    #Open the file
    file = open(path,"r")
    #Get the content of the file
    filecontent = file.read()
    #Split the file content into lines
    lines = filecontent.splitlines()
    #The last line of the file is the message
    return(lines[len(lines) - 1])

print("This is a simple script by User123456789#8073 to brute force my neverending challenge!\n\n")
print("We brute force assuming we know as little as possible. Here's what we know:\n\n-The challenge folder has a bunch of sub folders.\n-Each subfolder is named \"Neverending\" and a letter from a-z or 1-9\n-Each subfolder has 10 folders nested in side of each other.\n-Each nested folders has the same name as the sub folder\n-Each nested folder contains a file called \"Read This.txt\", which contains a bunch of nonsense and then the message at the last line\n-The file we want has a unique message - the message only appears once. There is only one file with a uniwue message\n\nBased on this information, let's brute force!\nIf you want to see how the brute forcing works, check the code.")
#Brute force and print the unique message
print("Unique message: " + bruteforce())
