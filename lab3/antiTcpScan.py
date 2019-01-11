#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 lhuang <lhuang9703@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import socket
import time
import struct


def checkSum(data):
    s = 0
    for i in range(0, len(data), 2):
        s += (data[i + 1]) + (data[i] << 8)
    s = (s & 0xFFFF) + (s >> 16)
    s = ~s & 0xFFFF
    
    return s


def createIpHeader(sourceAddress, destAddress):
    ipVersion = 4
    ipIhl = 5
    ipTos = 0
    ipLenth = 0
    ipId = 23333
    ipFlag = 0
    ipOffset = 0
    ipTtl = 255
    ipProtocol = socket.IPPROTO_TCP
    ipCheckSum = 0
    ipSrcAddress = socket.inet_aton(sourceAddress)
    ipDestAddress = socket.inet_aton(destAddress)
    ipVerIhl = (ipVersion << 4) + ipIhl
    ipFlagOffset = (ipFlag << 13) + ipOffset
    ipHead = struct.pack('!BBHHHBBH4s4s',
                    ipVerIhl,
                    ipTos,
                    ipLenth,
                    ipId,
                    ipFlagOffset,
                    ipTtl,
                    ipProtocol,
                    ipCheckSum,
                    ipSrcAddress,
                    ipDestAddress)
    
    return ipHead


def createTcpHeader(sourcePort, destPort, sourceAddress, destAddress, seq):
    tcpSrcPort = sourcePort
    tcpDestPort = destPort
    tcpSeq = 6666
    tcpAck = seq + 1
    tcpOffset = 5
    tcpUrg = 0
    tcpAck = 1
    tcpPsh = 0
    tcpRst = 0
    tcpSyn = 1
    tcpFin = 0
    tcpWindowSize = socket.htons(5840)
    tcpCheckSum = 0
    tcpUrgPtr = 0
    tcpOffsetReserv = (tcpOffset << 4)
    tcpFlag = tcpFin + (tcpSyn << 1) + (tcpRst << 2) + (tcpPsh << 3) + (tcpAck << 4) + (tcpUrg << 5)
    tcpHead = struct.pack('!HHLLBBHHH',
                    tcpSrcPort,
                    tcpDestPort,
                    tcpSeq,
                    tcpAck,
                    tcpOffsetReserv,
                    tcpFlag,
                    tcpWindowSize,
                    tcpCheckSum,
                    tcpUrgPtr)

     # Pseudo head
    srcIp = socket.inet_aton(sourceAddress)
    destIp = socket.inet_aton(destAddress)
    padding = 0
    protocol = socket.IPPROTO_TCP
    tcpLen = len(tcpHead)
    pseudoHead = struct.pack('!4s4sBBH', srcIp, destIp, padding, protocol, tcpLen)
    pseudoHead = pseudoHead + tcpHead
    if len(pseudoHead) % 2 != 0:
        pseudoHead += '\0'

    tcpCheckSum = checkSum(pseudoHead)
    tcpHead = struct.pack('!HHLLBBHHH',
                    tcpSrcPort,
                    tcpDestPort,
                    tcpSeq,
                    tcpAck,
                    tcpOffsetReserv,
                    tcpFlag,
                    tcpWindowSize,
                    tcpCheckSum,
                    tcpUrgPtr)

    return tcpHead


def tcpSynAckBack(sourcePort, destPort, sourceAddress, destAddress, seq):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    except:
        print("You should run as root user?")
        return
    ipHeader = createIpHeader(sourceAddress, destAddress)
    tcpSynAckHeader = createTcpHeader(sourcePort, destPort, sourceAddress, destAddress, seq)
    payload = ipHeader + tcpSynAckHeader
    try:
        s.sendto(payload, (destAddress, destPort))
        print("succeed")
    except:
        print("Fail to send the tcpSynAck packet!")
    
    return


def antiTcpScan():
    try:
        sock = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
    except :
        print("You should run as root user")

    while True:
        packet, addr = sock.recvfrom(65536)
        ipHeader = packet[14:34]
        ipHeader = struct.unpack('!BBHHHBBH4s4s', ipHeader)
        protocol = ipHeader[6]
        sourceAddress = socket.inet_ntoa(ipHeader[8])
        destAddress = socket.inet_ntoa(ipHeader[9])
        
        # check if the packet is a tcp SYN packet
        if protocol == 6:
            tcpHeader = packet[34:54]
            tcpHeader = struct.unpack('!HHLLBBHHH', tcpHeader)
            info = tcpHeader[5]
            if info == 2 or info == 34:
                sourcePort = tcpHeader[0]
                destPort = tcpHeader[1]
                seq = tcpHeader[2]
                tcpSynAckBack(destPort, sourcePort, destAddress, sourceAddress, seq)

    return


if __name__ == '__main__':
    antiTcpScan()
