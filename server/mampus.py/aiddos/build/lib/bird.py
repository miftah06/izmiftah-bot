# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-04-28 17:52:37.034765
import random
import sys
from datetime import datetime
import os
import time

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober',
          'November', 'Desember']
try:
 if n < 0 or n > 12:
  exit()
except ValueError:
 exit()
current = datetime.now()
hari = current.day
bulan = bulan_[n-1]
tahun = current.year
bullan = current.month
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07":
 "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m' # WARNA YANG UDAH GAK PERAWAN :V
J = '\033[38;2;255;127;0;1m' # ORANGE
phones = ('\033[]', input('Enter target phone number: '))
KhamdihiGanteng = [ P,M,H,K,B,U,O,N ] # warna janda x
komen = random.choice(['Mantap bang', phones,  'I Love You ',' Pengguna script lu, nih bang', phones, 'Kamu ganteng banget bang', phones,])
user, mi, status_foll, cr, phones, ok, cp, id, loop, looping = [], [], [], [], [], [], [], [], 0, 1
ta = current.year
bu = current.month
ha = current.day
op = bulan_[n-1]
waktu = '%s, %s, %s'%(ha,op,ta)
waktu.split('/')

def achil(kasep):
 for memek in kasep + "\n":
  sys.stdout.write(memek)
 sys.stdout.flush()
 time.sleep(0.003)


def menu():
 while True:
  print("")
try:
 os.system("clear")
 print('')
 os.system('date | lolcat')
 achil("\033[0;31m")
 achil("\033[0;31m")
 achil("\033[0;31m")
 achil("\033[0;00m")
 achil("\033[0;00m")
 achil("\033[0;00m")
except:
 pass

try:
 user = ('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile, Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]')
 open('user.txt','w').write(user)
except:
 pass
try:ugen = open('user.txt','r').read().splitlines()
except:ugen = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a, Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile, Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D), AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux;, U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0, Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q), AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux;, U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko), Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
try:ugen2 = open('user2.txt','r').read().splitlines()
except:ugen2 = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a, Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile, Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D), AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux;, U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0, Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q), AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux;, U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko), Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']