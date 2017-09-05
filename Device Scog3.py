#!/usr/bin/env python

import ipaddress
import sys, time
import os
import subprocess
from socket import *
from datetime import datetime
import csv

max_port = 1024
min_port = 1

max_ip = 254
min_ip = 1

def scan_host(host, port, portresult = 1):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        code = s.connect_ex((host,port))

        if code == 0:
            portresult = code
        s.close()
    except Exception:
        pass
    return portresult

time1 = datetime.now()


def verifyIPUP():
    while True:
        global host
        host = input("Enter target IP address: ")
        response1 = os.system("ping -c 1 " + host)
        if response1 == 0:
            print ("Ping to", host, "successful")
            break
        elif response1 == 2:
            print ("No response from ", host)
        else:
            print ("Ping to ", host, "failed, please enter a valid IP")
    return host

def checkActive():
    while True:
        global address
        address = os.system("ping -c 1 " + srange)
        print (srange)
        if address == 0:
            print ('IP address' + srange + 'active.')
            break
        else:
            d = float(srange) ++1
            srange = d
            print ("Ping to", str(srange), ", no response.")        
    return address



print ('Welcome to the SCOG Port/IP Scanner and Logger')

verifyIPUP()

##iprange = first, second, third, fourth = str(host).split('.')
##c = int(fourth) ++ 1
##srange = first+'.'+second+'.'+third+'.'+str(c)


print ('Port scanning function initialized: for ' + host)
time.sleep(2)

hostip = gethostbyname(host)



for port in range(min_port, max_port):
    try:
        response = scan_host(host, port)
        if response == 0:           
            print("The following port is open:", port)
    except Exception:
        pass
    except KeyboardInterrupt:
        print('You decided to stop the program, shutting down')
        sys.exit(1)



#checkActive()

time2 = datetime.now()
scantime = time2-time1
print ('Scan completed in: ', scantime)


while True:
    print ('Would you like to write information to file?')
    answer = input()
    if answer in ['yes', 'y', 'yeah']:
        print ('Alright, writing to file')
        print ('Program will exit upon scan completion.')
        break
    elif answer in ['no', 'n']:
        print ('Okay, exiting now..')
        break
    else:
        print ('Please enter a yes or no value')


#Found IPs
a = str(host)
b = str(port)

#Output File
csvRow = [a, b]
csvfile = "scog.csv"
with open(csvfile, 'a') as fp:
    wr = csv.writer(fp, dialect='excel')
    wr.writerow(csvRow)
    wr.writerow(['a', 'b'])

sys.exit()
                            
