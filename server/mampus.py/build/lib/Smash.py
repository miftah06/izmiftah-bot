#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import random
import socket
import threading
import time

# !/usr/bin/python
# -*-coding:Latin-1 -*

from colorama import *
from colorama import Fore
from django.contrib.gis.db.backends.postgis.pgraster import pack
from future.moves import sys

# coding=utf-8

import blood

init()

la7mar = '\033[91m'
lazra9 = '\033[94m'
la5dhar = '\033[92m'
movv = '\033[95m'
lasfar = '\033[93m'
ramadi = '\033[90m'
blid = '\033[1m'
star = '\033[4m'
bigas = '\033[07m'
bigbbs = '\033[27m'
hell = '\033[05m'
saker = '\033[25m'
labyadh = '\033[00m'
cyan = '\033[0;96m'
r = Fore.RED
g = Fore.GREEN
w = Fore.WHITE
b = Fore.BLUE
y = Fore.YELLOW
m = Fore.MAGENTA


def cls():
    linux = 'clear'
    windows = 'cls'


def print_logo():
    clear = "\033[0m"
    colors = [
        36,
        32,
        34,
        35,
        31,
        37,
        ]

    x = \
        """

{}{}
X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@
X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@
X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@
X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@
@@@@@&    @@@@@(    &X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@@@@@@@
@@@@      &@ ,@      @@@   &@ @,@(@   @%X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@
@@@@       (          @@@@@@@@@@@ @..@@.@    @@@@@@@@@@@@@@@@@@@@@@@@@
@@@@                  @@@@@@@@@@@ @  @  @    @@@@@@@@@@@@@@@@@@@@@@@@@
@@@                    @@@@@@@@@@& . ,#*. (X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>
@@@@        @@       .X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@@@@@@
@@@@@@    @@@@      @@@  @@@     &     @@,  @@@@   @@  @,  @@@@@@@@@@@
@@@@@@      @@      @@  ( @@@  @@@@  @@@% @  @  @@@@@    @@@@@@@@@@@@@
@@@@@@      @@      @  @@  @@  @@@@  @@@ @@@ .@    @@  @&  @@@@@@@@@@@
@@@@@@@     @@     X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@            X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X   NOLEP ARMY
@@@@@@@            X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@     TOOLKITS By Miftah45
X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@

                [#] DoubleAttack DDOS - 1-ATTACK TOOLSKIT [#]
                            [NolepArmy Version v2.5]
                            [Author Name] : Miftah45 
                                                          
one-attack!!                                                                                                                         
"""
    for (N, line) in enumerate(x.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(colors),
                         line, clear))
        time.sleep(0.05)


cls()
print_logo()

sys.dont_write_bytecode = True

# Colours

red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
defcol = "\033[0m"


def errorExit(msg):
    sys.exit(red + '[' + yellow + '!' + red + '] - ' + defcol
             + 'Fatal - ' + msg)


def get(text):
    return input(red + '[' + blue + '#' + red + '] - ' + defcol + text)


def saveToFile(proxy):
    with open(outputfile, 'a') as file:
        file.write(proxy + '\n')


def isSocks(host, port, soc):
    proxy = host + ':' + port
    try:
        if socks5(host, port, soc):
            action('%s is socks5.' % proxy)
            return True
        if socks4(host, port, soc):
            action('%s is socks4.' % proxy)
            return True
    except socket.timeout:

        alert('Timeout during socks check: ' + proxy)
        return False
    except socket.error:
        alert('Connection refused during socks check: ' + proxy)
        return False


def socks4(host, port, soc):  # Check if a proxy is Socks4 and alive
    host = socket.inet_aton(host)
    packet4 = '\x04\x01' + pack('>H', port) + ipaddr + '\x00'
    soc.sendall(packet4)
    data = soc.recv(8)
    if len(data) < 2:

        # Null response

        return False
    if data[0] != '\x00':

        # Bad data

        return False
    if data[1] != "\x5A":

        # Server returned an error

        return False
    return True


def socks5(host, port, soc):  # Check if a proxy is Socks5 and alive
    soc.sendall('\x05\x01\x00')
    data = soc.recv(2)
    if len(data) < 2:

        # Null response

        return False
    if data[0] != '\x05':

        # Not socks5

        return False
    if data[1] != '\x00':

        # Requires authentication

        return False
    return True


def isAlive(pip, timeout):  # Check if a proxy is alive
    try:
        proxy_handler = urllib2.ProxyHandler({'http': pip})  # Setup proxy handler
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]  # Some headers
        urllib2.install_opener(opener)  # Install the opener
        req = urllib2.Request(blood)  # Make the request
        socked = urllib2.urlopen(req, None, timeout=timeout)  # type: object # Open url
    except urllib2.HTTPError as e:

                                                          # Catch exceptions

        error(pip + ' throws: ' + str(e.code))
        return False
    except Exception as details:
        error(pip + ' throws: ' + str(details))
        return False
    return True


def checkProxies():
    while len(toCheck) > 0:
        proxy = toCheck[0]
        toCheck.pop(0)
        alert('Checking %s' % proxy)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)

        host = proxy.split(':')[0]
        port = proxy.split(':')[1]
        if int(port) < 0 or int(port) > 65536:
            error('Invalid port for ' + proxy)
            continue
        if isSocks(host, port, s):
            socks.append(proxy)
            saveToFile(proxy)
        else:
            alert('%s not a working socks 4/5.' % proxy)
            if isAlive(proxy, timeout):
                action('Working http/https proxy found (%s)!' % proxy)
                working.append(proxy)
                saveToFile(proxy)
            else:
                error('%s not working.')
        s.close()


socks = []
working = []
toCheck = []
threads = []
checking = True

proxiesfile = get('New text output file (new.txt): ')
outputfile = get('Output file: ')
threadsnum = int(get('Number of threads: '))
timeout = int(get('Timeout(seconds): '))
try:
    proxiesfile = open(proxiesfile, 'r')
except:
    errorExit(' Unable to open file: %s' % proxiesfile)

for line in proxiesfile.readlines():
    toCheck.append(line.strip('\n'))
proxiesfile.close()
q = \
    input('Second Scanned  of target list txt file with port (isreal.txt): '
          )
outputfile = int(get('Threads 1: '))
threadsnum = int(get('Number of threads: '))
timeout = int(get('Timeout(seconds): '))
try:

    # noinspection PyTypeChecker

    q = open(q, 'w')  # type: object
except:
    print('Your txt file is not found  *v*')
finally:
    qpath = r'[\]'
    if not os.path.exists(qpath):
        print('File does not exist')
    errorExit(' Unable to open file: %s' % q)

for line in q.readlines():
    toCheck.append(line.strip('\n'))
    q.close()

if os.path.isfile(qpath):
    check = ''
    while check != 'yes' and check != 'y':
        error('Output file already exist, content will be overwritten!')
        check = get('Are you sure you would like to continue(y/n)?'
                    ).lower()
        if check == 'n' or check == 'no':
            errorExit('Quitting...')

    for i in xrange(threadsnum):
        threads.append(threading.Thread(target=checkProxies))
        threads[i].setDaemon(True)
        action('Starting thread n: ' + str(i + 1))
        threads[i].start()
        time.sleep(0.25)
    if len(threading.enumerate()) - 1 == 0:
        alert('All threads done.')
        action(str(len(working)) + ' alive proxies.')
        action(str(len(socks)) + ' socks proxies.')
        action(str(len(socks) + len(working)) + ' total alive proxies.')
        checking = False
    else:
        alert(str(len(working)) + ' alive proxies until now.')
        alert(str(len(socks)) + ' socks proxies until now.')
        alert(str(len(toCheck)) + ' remaining proxies.')
        alert(str(len(threading.enumerate()) - 1) + ' active threads...'
              )
