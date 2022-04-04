import random

fi = input("input the file : ")
vocab = input("enter the text : ")
try:
    with open(fi,"r") as files:
        alltext = files.read()
        words = list(map(str, alltext.split()))
    
        if vocab or vocab.capitalize in words:
            print("yes")
        else:
            print("no")
            
except:
    print("file is bad")