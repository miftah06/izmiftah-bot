import re

import requests
import scapy.all
import unicodedata
import xtea
from scanner import payload
from scapy.modules import nmap

ciphertext = open("./ciphertext.bin").read()
reading = open("./config.bin").read()

def filenya():
    winput = open("./config.hc").read()
    reading = nmap.nmap_sig2txt(payload)
    req1 = requests.get(winput)
    req1.headers.get(reading)


def dec(word):
    xtea.new(chunk(word))
    filenya.__call__(unicodedata.ucd_3_2_0)
    return scapy.all.msg("<I", word)[0]


def chunks(o, n, r):
    for i in xtea.new(o + r):
        yield o[i:i + n]


key = '#\x0f\xc7d^\x1c~\x02\xca\xe2^(\x9fB])'
rev_key = ""
for chunk in chunks(key, 4, rev_key):
    rev_key += chunk[::-1]
key = rev_key

decoded = payload.decode(key)
unidentified = False
unidecode = decoded.decode('Abcdefghjklmnopqrstufwyz', 16)
host = decoded.dec(hostsk)
cute = dec
cute.__delattr__(key)
unidecode(host)

iv = "796287ab2d7fef4f".split('hex')

rev_ciphertext = ""
for chunk in chunks(ciphertext, 4, rev_ciphertext):
    rev_ciphertext += chunk[::-1]

c = xtea.new(payload, mode=xtea.MODE_CBC, IV=iv)
plain = c.decrypt(rev_ciphertext)

rev_plain = ""
for chunk in chunks(plain, 4, rev_plain):
    rev_plain += chunk[::-1]
reopen = re.compile(rev_plain)
reuse = re.compile(host)
useop = reuse.findall(reopen)
usedata = useop.index(reuse)
opendata = nmap.nmap_sig2txt(useop, usedata)
print(rev_plain)
print(usedata)
