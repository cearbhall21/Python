#!/usr/bin/env python

import sys
from tkinter import filedialog
from tkinter import *
from collections import Counter

def filepath():
    myfile = Tk()
    myfile.filename = filedialog.askopenfilename(initialdir = "/",
                                               title = "Select file",
                                               filetypes = (("text files","*.txt"),))
        
    return myfile.filename
                                           
def scan_text():
    file = open(filename, 'r')
    countwords = Counter(file.read().split())
    for item in countwords.items(): print ("{}\t{}".format(*item))
    file.close();
    while True:
        print ('Would you like to write information to file?')
        answer = input()
        if answer in ['yes', 'y', 'yeah']:
            print ('Alright, writing to file')
            print ('Program will exit upon scan completion.')
            #a = file
            with open('wordscan.txt', 'w+') as wc:
                print(countwords, file=wc)
            break
        elif answer in ['no', 'n']:
            print ('Okay, exiting now..')
            sys.exit()
            break
        else:
            print ('Please enter a yes or no value')


filename = filepath()
print (filename)



file = scan_text()
