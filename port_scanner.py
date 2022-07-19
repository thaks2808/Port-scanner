#!/bin/python3
import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])    #!!Translate hostname to IPv4!!
else:
    print("Invalid amount of arguments.")
    print("Syntax:  python3 port_scanner.py <ip address>")
    
    
    
#Add a pretty Banner
print("-" * 50)
print("Scanning target "+target)
print("Time started; "+str(datetime.now()))
print("-" * 50)

try:
    
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET is IPv4 and SOCK_STREAM is Port 
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #Returns an error indicator
        if result == 0:
            print("port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\nExiting Program !!!!!!!!!!!!!!!")
    sys.exit()
          
except socket.gaierror:
    print("Hostname could not be resolved.!!")
    sys.exit() 
          
except socket.error:
    print("Could not connect to server.")
    sys.exit()
