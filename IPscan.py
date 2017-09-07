#!/usr/bin/env python
import ipaddress
import sys, time
import os
import subprocess
import socket
from datetime import datetime
import csv

FNULL = open(os.devnull, 'w')

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


print ('Welcome to the IP/Port Scanner and Logger')
address = input('Enter starting IP address: ')
split1 = first,second,third,fourth = str(address).split('.')
start = int(fourth)

host = first+'.'+second+'.'+third+'.'+str(start)
end_address = input('Enter the ending IP address: ')
split2 = first,second,third,fourth = str(end_address).split('.')
end = int(fourth)

network = first+'.'+second+'.'+third+'.'

max_port = 1024
min_port = 1


remoteserver = host
remoteserverIP = socket.gethostbyname(remoteserver)

def port_scan():
    print ('Port scanning function initialized:')
    try:
        for port in range(min_port,max_port):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteserverIP, port))
            if result == 0:
                print ('Port ' + str(port) + ': Open')
            sock.close()
    except KeyboardInterrupt:
        print ("You halted the process")
        sys.exit()

    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print ("Couldn't connect to server")
        sys.exit()

def checkUp():
    for i in range(int(start), int(end)):
        try:
            subprocess.check_call(['ping', '-c', '1', network + str(i)], stdout=FNULL,stderr=FNULL)
        except (OSError, subprocess.CalledProcessError):
            print ("[-] DOWN {}{}".format(network,i))
        else:
            print ("[+] UP {}{}".format(network,i))
            port_scan()



checkUp()

time1 = datetime.now()





##
###Found IPs
##a = str(host)
##b = str(port)

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
        sys.exit()
        break
    else:
        print ('Please enter a yes or no value')

##
###Output File
##csvRow = [a, b]
##csvfile = "scog.csv"
##with open(csvfile, 'a') as fp:
##    wr = csv.writer(fp, dialect='excel')
##    wr.writerow(csvRow)
##    wr.writerow(['a', 'b'])
##
##sys.exit()
##               
