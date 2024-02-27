import sys
import requests
import scapy
from networkx import reverse
from scapy.modules import nmap

from server.scanbug import payload

reading = open("config.bin").read()


def filenya():
    winput = open("config.hc").read()
    req1 = requests.get(winput)
    req1.headers.get(payload)
    winput.split(reading)


key = '#\x0f\xc7d^\x1c~\x02\xca\xe2^(\x9fB])'
unidentified = False

iv = "796287ab2d7fef4f".split('hex')

rev_ciphertext = ""
rev_key = payload
nmi = nmap.nmap_sig2txt
inmap = reverse
sys.stdout.write('hasil.txt')
print(payload)

