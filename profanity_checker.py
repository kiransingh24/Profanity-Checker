import os
import urllib
curr_dir = os.chdir("E:\python_projects")
print (curr_dir)
def read_file():
    file = open('profanity.txt','r')
    contents = file.read()
    print (contents)
    file.close()
    check_profanity(contents)
def check_profanity(text_to_check):
     connection = urllib.urlopen(
         "http://www.purgomalum.com/service/containsprofanity?text="+text_to_check)
     output = connection.read()
     #print output
     connection.close()
     if "true" in output:
         print("Profanity Alert!")
     elif "false" in output:
         print ("Text Document does not have profane words!")
     else:
         print("Could not scan the document")
read_file()
