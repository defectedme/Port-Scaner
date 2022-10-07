
import socket
from IPy import IP

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(time)
        sock.connect((ipaddress, port))
        print('Port' + str(port1) + 'is open')

    except:
        print('Port' +str(port1) + 'is close')

ipaddress = input('enter target ot scan:')
port1 = int(input("from:"))
port2 = int(input("to:"))
time = float(input('time from 0 to 100 also 0.1 to 99.9:   '))
#port3 = port1 and port2
while port1 < port2:
    scan_port(ipaddress, port1)
    #print(port1)
    port1 = port1 + 1
    #for port in range(port1, port2):


    #print(port1)
