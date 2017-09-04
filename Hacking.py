#!/usr/bin/python

import Image
import time
import os
import socket
import fcntl
import struct
import itertools
import re

#Sleep 1 option
def newline():
    time.sleep(10)
    print '\n'
#Sleep 2 option    
def newline2():
    time.sleep(20)
    print '\n'

#Enter correct Value    
def errorst():
    print ("You must put a yes or no value in")

#Nested Loop for access
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
                    newline()
                    print ('This will allow you to edit and view the contents of a text file on a terminal. In this file you will see the IP address of another web server that you may not have noticed in your Armitage scans. Open the main IP address of the web server to explore what is on it.')
                    newline()
                    print ('Notice that there is a second link for the same web server with "login" as part of the URL, open that URl in your web browser')
                    return
                elif answer in ['no', 'n']:
                    print ('Locate the password dictoinary stored in "home/Desktop/passwords.txt", then open the file by typing "nano /home/Desktop/passwords.txt"')
                    print ('This will allow you to edit and view the contents of a text file on a terminal. In this file you will see the IP address of another web server that you may not have noticed in your Armitage scans. Open the main IP address of the web server to explore what is on it.')
                    newline()
                    print ('Notice that there is a second link for the same web server with "login" as part of the URL, open that URl in your web browser')
                    newline()
                    return
                else:
                    errorst()
#Get IP
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

hostname = "google.com"
response = os.system("ping -c 1 " + hostname)
if response == 0:
    print 'Your computer is able to ping ' + hostname + ' so it appears your Internet connection is up for this exercise, be very careful!'
else:
    print 'Internet appears to be down for this exercise, less caution is needed.'
time.sleep(3)





print '\n'
print ('This appears to be the IP address of your computer: ' + get_ip_address() + ' You will need this information for later, it lets you know what subnet you are on.')
time.sleep(3)
print '\n'

print ('Hello, and welcome to the first three steps of hacking.')
time.sleep(3)
name = raw_input("What is your name? ")
print ("Hi " + name + "! I am Crash Override, and I will be guiding you through this tutorial. Let's begin!")
time.sleep(5)

tutorial = 'yes'
print ('Are you using wireless or a cabled machine?')
while tutorial == 'yes':
    answer = raw_input()
    if answer == str('cabled'):
        print ('Alright, '+ name + '!'' Proceeding to the cabled directions!')
        time.sleep(3)
        break
    elif answer == str('wireless'):
        print ("Aren't you a lucky one. Let's see if there is a wireless network that we can hack into..")
        time.sleep(2)
        print ('The first thing we need to is able enable monitor mode by typing the command "airmong-ng check kill" into a terminal, then type "airmon-ng start wlan0", you can ensure that you are in monitor mode by typing "iwconfig" and seeing what it says your network card is in.')
        print '\n'
        newline2()
        print ('Next, see what access points are available by enetering "airodump-ng wlan0mon" and note down the BSSID and Channel <CH> of the access point you are targeting')
        newline2()
        print ("It's time to capture the 3-way handshake and write that information to a pcap file for later examination. Type the command 'airodump-ng -c<ch> --bssid<bssid> -w<filename> wlan0mon') Where <ch> is the channel the target access point is running on. <bssid> is the MAC address for the target access point. -w writes to file with the name you give it, in this case crackwpa.")
        newline2()
        print ('Please see the opened image for an example')
        print '\n'
        image = Image.open('/root/Desktop/Hack/Terminalwindow.png')
        image.show()
        print ('Now that you are monitoring the target access point only, we need to actually force an authenticated client to disconnect so we can capture that handshake. To do this, take note of the station MAC address from a client on the network, keep your monitoring window open and open a new terminal window. We will then deauthicate a client with the second window')
        newline2()
        image = Image.open('/root/Desktop/Hack/airodump.png')
        image.show()
        print ('In your new window enter "aireplay-ng -0 10 -a <bssid> -c <station> wlan0mon" Where: -0 means deauthentication, 10 is the number of deauth attempts, -a is the MAC address of your target access point, and -c is the client you are kicking off the network"')
        image = Image.open('/root/Desktop/Hack/handshake.jpg')
        newline2()
        print ('Looking back on the first terminal window where we are monitoring the target access point, you will see on the top that it captured a WPA handshake with a string of numbers and letters after it. We now have all that we need to crack the network password!')
        newline2()
        print ('Note, that if you did not capture a handshake, you may need to increase the number of deauths to send in previous step')
        newline2()
        print ('Time to crack the password using your pre-installed Kali wordlist')
        newline2()
        print ("Enter the following: 'aircrack-ng -w 'usr/share/wordlists/<wordlist>.txt -b <bssid> /directory/*.cap'")
        newline2()
        print ('Please see the example image that will open soon')
        image = Image.open('/root/Desktop/Hack/aircrack.png')
        image.show()
        print ('Aircrack will now try to crack the password by matching passwords from your wordlist to the captured handshake. If the password is in the wordlist, it sill say KEY FOUND! [<password>]')
        time.sleep(20)
               
        break
    else:
        print ('Please choose between "wireless" and "cabled"')
      
print ('' + name + ','' do you know the first step in hacking a network?')
while tutorial == 'yes':
    answer = raw_input()
    if answer in ['yes', 'y', 'yeah']:
        print ('Alright,' + name + '! Proceed to step 2, then!')
        break
    elif answer in ['no', 'n']:
        print ('Reconnassaince is first, we need to see what machines are there, try opening Armitage to find the vulnerable machine.')
        newline()
        print ('You will be greeted with the following message, click "Connect" using the default settings')
        newline()
        image = Image.open('/root/Desktop/Hack/armitageopen.png')
        image.show()
        time.sleep(15)
        print ('It may also ask if you want to start Metasploit RPC server as seen in the image that will open, click "Yes".')
        image = Image.open('/root/Desktop/Hack/connect.png')
        image.show()
        time.sleep(10)
        print ('You should now have the following program open.')
        image = Image.open('/root/Desktop/Hack/armitagerun.png')
        image.show()
        newline()
        time.sleep(10)
        print ('Then click "Hosts" at the top, then "Nmap scan"')
        newline()
        print ("In this case we're looking for a vulnerable Linux based machine, but you will see all of the computers on the network. It is helpful to do a 'Quick Scan (OS Detect) so you can ignore the incorrect machines.")
        newline()
        break
    else:
        errorst()
    
print ('' + name + ','' do you know the second step in hacking a network?')
while tutorial == 'yes':
    answer = raw_input()
    if answer in ['yes', 'y', 'yeah']:
        print ('Alright, ' + name + '! Proceed to step 3, then!')
        break
    elif answer in ['no', 'n']:
        print ('Scanning is the next step, in this case we will use Armitage to find the vulnerable machine and its IP address, but there are many other programs that can be used including: Zenmap, arp-scan -l, netdiscover, Sparta, Ettercap, and more ')
        newline()
        print ('Armitage includes many of the aforementioned programs in it, when scanning it will ask for an IP address range that you would like to scan. If you are not certain of the IP address your computer is on, open a terminal and type "iwconfig" then type main router address into the Armitage scan. In the case today, it will be 192.168.97.1/24. Where /24 is a CIDR notation of how the network is configured.')
        newline()
        print ("Once the scan completes, you will see a list of computers on your network with different pictures based on their operating system")
        newline()
        print ("Now it is time to find our available attacks.") 
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
        print ("Gaining access is the third step. With Armitage, right click the target machine, click 'Attacks', the attack you're looking for is: ""'vulnerability=IRC-real'""")
        newline()
        print ("Armitage will then launch a Metasploit console for you, configure your LPORT (Listening port) your LHOST (Listening IP address of your computer) then inject a payload onto that computer to grant you shell access. There will be times where this process will not work and you will have to get a user to open a file to grant you persistant access. We will cover this another time, though.")
        newline()
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
        print (''+ name + 'The hashes will need to be decrypted in order to find out what they are. Today, we will use MD5online.org to decrypt the hashes, but there are also programs on Kali that are built in for this purpose, such as Hashcat, but your computer needs a fairly strong graphics card in order to break the hash in a reasonable amount of time.')       
        newline()
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
print ('' + name + ','' be sure that you only use these new skills for ethical hacking purposes and in controlled settings until you fully understand how they work! These are very powerful pgorams and can cause massive amounts of damage if you are not careful')
image = Image.open('/root/Desktop/Hack/ethicalhack.jpg')
image.show()
print ('This ends the the exercise. The next tutorial will be uploading a Reverse Shell with PHP into the web server to gain Shell access to the vulnerable web server. Until then, goodbye!')
exit


