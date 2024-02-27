# coding=utf-8
import base64
import imaplib
import os
import random
import socket
import threading
from telnetlib import IP
from typing import List
import sys
import domain
import pinject
import replace
# !/usr/bin/python
# -*-coding:Latin-1 -*
import requests
import time
from boto.route53 import domains
from bs4 import BeautifulSoup
from sys import stdout

import passnya

os.system("cls")  # if windows
# os.system("clear") # if linux or mac
# the instalation modules
try:
    from colorama import init, Fore
    from termcolor import colored

    init()
except ImportError:
    print("")
    print("Some modules not installed\n")
    quest = input("Do you want install the dependencies [Y/N] ? ")
    if quest ==("Y" or quest == "" or quest == "y"):
        os.system("pip install colorama, termcolor")  # comand to install modules
    elif quest == "N" or quest == "n":
        sys.exit()  # if not

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
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """

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

                [#] DoubleAttack  - 1-ATTACK TOOLSKIT [#]
                            [NolepArmy Version v2.5]
                            [Author Name] : Miftah45  
                                                          
one-attack!!                                                                                                                         
"""

    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)


cls()
print_logo()

hostsk = input('[+] Enter Your target (ex: https://google.com): ')  # type: str
requests.get(hostsk)
# noinspection PyTypeChecker
threads = input("Number of threads: ")
# noinspection PyTypeChecker
timeout = input("Timeout(max: 10): ")
requests.threads = (threads, timeout)
to_check = {}

url = hostsk
response = requests.get(url, timeout=10)
content = BeautifulSoup(response.content, "html.parser")

articleArr = []
for article in content.findAll('div', attrs={"class": "articlecontainer"}):
    articleObject = {
        "author": article.find('h2', attrs={"class": "author"}).text.encode('utf-8'),
        "date": article.find('h5', attrs={"class": "dateTime"}).text.encode('utf-8'),
        "article": article.find('p', attrs={"class": "content"}).text.encode('utf-8'),
        "likes": article.find('p', attrs={"class": "likes"}).text.encode('utf-8'),
        "shares": article.find('p', attrs={"class": "shares"}).text.encode('utf-8')
    }
    articleArr.append(articleObject)


def isAlive(pip, timeout):  # Check if a proxy is alive
    try:
        proxy_handler = urllib2.ProxyHandler({'http': pip})  # Setup proxy handler
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]  # Some headers
        assert isinstance(urllib2, object)
        urllib2.install_opener(opener)  # Install the opener
        req = urllib2.Request(hostsk)  # Make the request
        socked = urllib2.urlopen(req, None, timeout=timeout)  # type: object # Open url
    except urllib2.HTTPError as E:  # Catch exceptions
        error(pip + " throws: " + str(E.code))
        return False
    except Exception as details:
        error(pip + " throws: " + str(details))
        return False
    return True


# noinspection PyTypeChecker
class IMAP4_SSL(imaplib.IMAP4_SSL):
    # Similar to above, but with extended support for SSL certificate checking,
    # fingerprints, etc.
    # noinspection PyTypeChecker,PyTypeChecker,PyTypeChecker,PyTypeChecker,PyTypeChecker,PyTypeChecker,PyTypeChecker,PyTypeChecker,PyTypeChecker,PyTypeChecker,PyArgumentList
    def __init__(self, method='...', url='...', headers='...', files='...', data='...', params='...', auth='...',
                 cookies='...', hooks='...', json='...', extra_args=None, hosts=None):
        super(imaplib.IMAP4_SSL, self).__init__(url='...', method='...', headers='...', files='...', data='...',
                                                params='...', auth='...', cookies='...',
                                                hooks='...', json='...')
        super(imaplib.IMAP4_SSL, self).__init__()
        super(IMAP4_SSL, self).__init__()
        self.url = url
        self.params = params
        self.json = json
        self.method = method
        self.headers = headers
        self.hooks = hooks
        self.files = files
        self.data = data
        self.extra_args = extra_args
        self.cookies = cookies
        self.auth = self.auth
        self.sslobj = ssl.wrap_hostet(self.host, self.keyfile, self.certfile,
                                      **auth)
        self.file = self.sslobj.makefile('')
        self.port = self.port
        self.host = self.host
        self.keyfile = self.keyfile
        self.host = hosts
        self.timeout = self.timeout
        self.certfile = self.certfile

    def __main__(self, target=domain,
                 certfile=None, ssl_version=None, ca_certs=None,
                 ssl_ciphers=None, timeouts=10):
        """
        :type ssl_ciphers: object
        """
        assert isinstance(ssl_version, object)
        self.ssl_version = ssl_version
        self.ca_certs = ca_certs
        self.ssl_ciphers = ssl_ciphers
        imaplib.timeout = timeouts
        cert_reqs.append(self, target, self.port, keyfile, certfile)

    def open(self, cert_reqs=None, **kwargs):
        replace.host = socket.create_connection((self.host, self.port))
        extra_args = {}
        if imaplib.ssl_version:
            extra_args['ssl_version'] = self.ssl_version
        if cert_reqs.ca_certs:
            extra_args['cert_reqs'] = ssl.CERT_REQUIRED
            extra_args['ca_certs'] = self.ca_certs
        if self.ssl_ciphers:
            extra_args['ciphers'] = self.ssl_ciphers


class checkerr(threading.Thread):
    def __init__(self, host, user, pwd, timeout, interval):
        t = threading.Thread.__init__(self)
        self.host = host
        self.user = user
        self.pwd = pwd
        self.interval = interval
        self.timeout = timeout
        self.connected = False
        self.i = None
        self.work = True
        self.attemp = 4
        self.inbox = ''
        self.spam = ''

import genericpath
import random
import sys
import time

import colorama
import networkx
import requests
from IP2Proxy import IP2Proxy
from oauthlib.uri_validate import host


colorama.init()

# Now regular ANSI codes should work, even in Windows
CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'  # mode 31 = red forground
RESET = '\033[0m'  # mode 0  = reset
BLUE = "\033[34m"
CYAN = "\033[36m"
GREEN = "\033[32m"
BOLD = "\033[m"
REVERSE = "\033[m"


# coded by mister spy
# contact me 712083179
def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """

{}{}
--NolepArmy--@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@ /..(@@..(@@@@@@@..@@@@@@@@@@@@@@@..@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@.,..@.@@@.&..&..@....,*..../@@@#%..@@,...&.......,&..@/.%@@@@@@@@@@@
@@@@@@@@@@@@.@@...@@..@@.,..@..&@@@.&@,.&/%,#/./@&.@@@,.@,.@..@..@..&@@@@@@@@@@@
@@@@@@@@@@..@@@@(.(@@%.&@@@.@@&./@&.#,@@..@@@@(.,&#@@@,@@.@@%/@@#/(.@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%,@@@@@@@@@@@@@@@@@@@@@@@@@@@....@@@@@@@@@@@@@
--NolepArmy--@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
--NolepArmy--@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@            X>X<X>X<X>X<X>X Sniffer!! X<X>X<X>X   NOLEP ARMY
@@@@@@@            X>X<X>X<X>X<X>X Sniffer!! X<X>X<X>X<X>@     TOOLKITS By Miftah45
X>X<X>X<X>X<X>X Sniffer!! X<X>X<X>X<X>X>X<X>X<X>X<X>X Sniffer!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@

                [#] NolepArmy-sniff - Sniffer TOOLSKIT [#]
                            [NolepArmy Version v1.0]
                            [Author name] : Miftah45  
                                                          
Good luck!!                                                                                                                         
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)


logo()

time.sleep(0.05)
print("PLAYING NEW DDOS CONFIG!!")
def sniff(Nam):
    bug = i.strip()
    save = genericpath.isfile('logs.txt')
    open('logs.txt', 'w').write(Nam)
    hostnya = passnya.hostsk
    ip1: Response = requests.post(hostnya, Nam)
    neff2 = ip1.status_code
    sniffpy = networkx.NetworkXTreewidthBoundExceeded(neff2)  # returns a MIMEType object
    print("Koneksi:", sniffpy, "ok")
    print("host:", Nam, sniffpy, "status ok")  # prints "image"
    print("bug.hc is on sniffing...")
    buff = getattr(ip1, host, IP2Proxy)
    try:
        save.__add__(buff)
        if 'bug.hc' not in bug:
            "log " + Nam
            open('logs.txt', 'a').write(Nam + '\n')
        elif '' in bug:
            open('bug.hc', 'w').write('logs.txt')
            "log: " + Nam
            open('logs.txt', 'a').write(Nam + '\n')
        "log: " + Nam
        open('logs.txt', 'a').write(Nam + '\n')
        'Already sniff see your Sniffed file!!'
    except Exception(KeyboardInterrupt):
        print("Here you go!!")
        input("enter injection (pwd) file: ")

print("Mohon Ganti nama file hhtp custom ke pwd saja tanpa extensi!!")
qfile = input('Your bug/hostname config injection target (bug.hc/open wordlist.txt if is error): ')

with open(qfile) as f:
    for i in f:
        sniff(i)

successful = hostsk
tld = open('tlds.txt', 'r').read().splitlines()
tlds = cache = {domain: tld}
bads = []
cracked = sniff(qfile)
rbads = 0
host = hostsk
rcracked = open('pass.txt', 'r').read().splitlines()

try:

    passwords = open('pwd', 'r').read().splitlines()  # type: List[str]
except Exception as e:

    print("File 'pwd' missing")
    exit()
zz = input('enter Combo List Name :')
inputs = open(zz, 'r').read().splitlines()
option = '0'

if option == '1':
    try:

        users = open('usr', 'r').read().splitlines()  # type: List[str]
    except Exception as e:

        print("You chosed domains + users bruteforce and 'usr' is missing")
        exit()
if len(sys.argv) > 4:
    rbads = 1


# noinspection PyTypeChecker
def part():
    global tld, tlds
    for i in tld:  # type: str
        tlds[i] = i

part()
print('[+] All files loaded')
