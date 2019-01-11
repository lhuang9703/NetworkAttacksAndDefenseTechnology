#!/usr/bin/env python
# coding: utf-8

# In[23]:


import socket
import time
import struct
import threading
import argparse
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)
formats = logging.Formatter('%(asctime)s[%(message)]', '%m/%d/%Y %I:%M:%S:%p')
console = logging.StreamHandler()
console.setFormatter(formats)
logger.addHandler(console)

parser = argparse.ArgumentParser()
parser.add_argument('--IP', type=str, default='127.0.0.1',
                   help='IP you want to scan, default:127.0.0.1')
parser.add_argument('--w', type=str, default='all',
                   help='select the way you want to scan:\nall: scan all the ports.\none: scan just one port gave.,default:all')
parser.add_argument('--p', type=int, default=2333,
                   help='the port you want to scan(less than 65536),default:2333')
args = parser.parse_args()


# In[24]:


def udpMessageSender(ip, port):
    while True:
        try:
            sockUdp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sockUdp.sendto("Hello world!", (ip, port))
            sockUdp.close()
            break
        except:
            print("Fail to send the udp message, try again")
            time.sleep(1)
            continue


# In[25]:


def icmpMessageReceiver(ip, port):
    try:
        sockIcmp = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    except:
        print("You should run as root user")
        return
    sockIcmp.settimeout(5)
    while True:
        try:
            packet, addr = sockIcmp.recvfrom(65536)
            icmpHead = packet[20:28]
            headType, code, checksum, packetID, sequence = struct.unpack(
                "bbHHh",icmpHead
            )
            break
        except:
            print("the port:%s on %s is opened" %(port, ip))
            return
    sockIcmp.close()
    if code == 3 and headType == 3 and addr[0] == ip:
        print("the port:%s on %s is closed" %(port, ip))
    elif code in [1, 2, 9, 10, 13] and headType == 3 and addr[0] == ip:
        print("the port:%s on %s is filted" %(port, ip))
    return


# In[26]:


def udpScanPort(ip, port):
    icmpReceiveThread = threading.Thread(target=icmpMessageReceiver, args=(ip, port))
    icmpReceiveThread.daemon = True
    icmpReceiveThread.start()
    
    time.sleep(0.2)
    udpMessageSender(ip, port)
    time.sleep(0.2)
    
    icmpReceiveThread.join()
    return


# In[27]:

if __name__ == '__main__':
    if args.IP and args.w == 'one' and args.p < 65536:
        udpScanPort(args.IP, args.p)
    elif args.IP and args.w == 'all':
        for item in range(130, 141):
            udpScanPort(args.IP, item)


# In[ ]:

